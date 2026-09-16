-- ==========================================================
-- ZYROO DATA ANALYTICS INTERNSHIP — WEEK 3
-- Task 03: Revenue & Driver Performance Analysis (SQL Engine)
-- Database Engine: SQLite / PostgreSQL Compatible
-- ==========================================================

-- ----------------------------------------------------------
-- 1. DDL: Create the Week 3 Extended Table Schema
-- ----------------------------------------------------------
DROP TABLE IF EXISTS rides;

CREATE TABLE rides (
    ride_id TEXT PRIMARY KEY,
    date TEXT NOT NULL,
    pickup_location TEXT NOT NULL,
    dropoff_location TEXT NOT NULL,
    distance_km REAL NOT NULL CHECK(distance_km > 0),
    fare REAL NOT NULL CHECK(fare >= 0),
    payment_method TEXT NOT NULL,
    driver_id TEXT NOT NULL,
    ride_type TEXT NOT NULL,
    ride_status TEXT NOT NULL,
    rating REAL CHECK(rating IS NULL OR (rating >= 1.0 AND rating <= 5.0))
);

-- ----------------------------------------------------------
-- 2. QUERY 1: Core Revenue KPIs
-- Calculates total completed rides, total realized revenue,
-- average fare, and average revenue per completed ride.
-- ----------------------------------------------------------
SELECT 
    COUNT(*) AS total_bookings,
    SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_rides,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_rides,
    ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END), 2) AS total_realized_revenue,
    ROUND(SUM(fare), 2) AS gross_booking_value,
    ROUND(SUM(CASE WHEN ride_status = 'Cancelled' THEN fare ELSE 0 END), 2) AS lost_revenue,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN fare ELSE NULL END), 2) AS avg_fare_completed,
    ROUND(
        SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) * 1.0 / 
        NULLIF(SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END), 0), 
        2
    ) AS avg_revenue_per_completed_ride
FROM rides;

-- ----------------------------------------------------------
-- 3. QUERY 2: Revenue by Payment Method (Mandatory Internship Query)
-- Demonstrates volume, realized revenue, average ticket size,
-- and percentage share of total revenue.
-- ----------------------------------------------------------
SELECT 
    payment_method,
    COUNT(*) AS completed_rides,
    ROUND(SUM(fare), 2) AS total_revenue,
    ROUND(AVG(fare), 2) AS average_fare,
    ROUND(
        SUM(fare) * 100.0 / (SELECT SUM(fare) FROM rides WHERE ride_status = 'Completed'), 
        2
    ) AS revenue_share_pct
FROM rides
WHERE ride_status = 'Completed'
GROUP BY payment_method
ORDER BY total_revenue DESC;

-- ----------------------------------------------------------
-- 4. QUERY 3: Revenue by Pickup Location (Demand vs Revenue)
-- Evaluates which hubs drive top-line revenue and identifies
-- locations with high demand but relatively low ticket yields.
-- ----------------------------------------------------------
SELECT 
    r.pickup_location,
    COUNT(r.ride_id) AS total_bookings,
    SUM(CASE WHEN r.ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_rides,
    ROUND(SUM(CASE WHEN r.ride_status = 'Completed' THEN r.fare ELSE 0 END), 2) AS realized_revenue,
    ROUND(AVG(CASE WHEN r.ride_status = 'Completed' THEN r.fare ELSE NULL END), 2) AS avg_fare,
    ROUND(
        SUM(CASE WHEN r.ride_status = 'Completed' THEN r.fare ELSE 0 END) * 100.0 / 
        (SELECT SUM(fare) FROM rides WHERE ride_status = 'Completed'), 
        2
    ) AS revenue_contribution_pct
FROM rides r
GROUP BY r.pickup_location
ORDER BY realized_revenue DESC;

-- ----------------------------------------------------------
-- 5. QUERY 4: Revenue & Fare Yield by Ride Type Tier
-- Compares product tier usage (Economy, Standard, Premium)
-- against realized revenue and average fare yield.
-- ----------------------------------------------------------
SELECT 
    ride_type,
    COUNT(*) AS completed_rides,
    ROUND(SUM(fare), 2) AS total_revenue,
    ROUND(AVG(fare), 2) AS avg_fare,
    ROUND(
        SUM(fare) * 100.0 / (SELECT SUM(fare) FROM rides WHERE ride_status = 'Completed'), 
        2
    ) AS revenue_pct
FROM rides
WHERE ride_status = 'Completed'
GROUP BY ride_type
ORDER BY total_revenue DESC;

-- ----------------------------------------------------------
-- 6. QUERY 5: Driver Performance Summary (Mandatory Internship Query)
-- Measures total rides, completed rides, cancelled rides,
-- realized revenue, average rating, completion & cancellation rates.
-- ----------------------------------------------------------
SELECT 
    driver_id,
    COUNT(*) AS total_rides,
    SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_rides,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_rides,
    ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END), 2) AS revenue,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN rating ELSE NULL END), 2) AS average_rating,
    ROUND(AVG(distance_km), 2) AS average_distance_km,
    ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS completion_rate_pct,
    ROUND(SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS cancellation_rate_pct,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN fare ELSE NULL END), 2) AS avg_fare
FROM rides
GROUP BY driver_id
ORDER BY revenue DESC;

-- ----------------------------------------------------------
-- 7. QUERY 6: Multi-Criteria Driver Performance Ranking
-- Avoids ranking on revenue alone. Implements a weighted
-- composite formula combining Revenue (35%), Completed Rides (25%),
-- Rating (25%), and Completion Rate (15%).
-- ----------------------------------------------------------
WITH DriverAggregates AS (
    SELECT 
        driver_id,
        COUNT(*) AS total_rides,
        SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_rides,
        SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_rides,
        ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END), 2) AS revenue,
        ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN rating ELSE NULL END), 2) AS average_rating,
        ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS completion_rate,
        ROUND(SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS cancellation_rate
    FROM rides
    GROUP BY driver_id
),
MaxBounds AS (
    SELECT 
        MAX(revenue) AS max_rev,
        MAX(completed_rides) AS max_comp
    FROM DriverAggregates
)
SELECT 
    d.driver_id,
    d.total_rides,
    d.completed_rides,
    d.cancelled_rides,
    d.revenue,
    d.average_rating,
    d.completion_rate,
    d.cancellation_rate,
    ROUND((
        0.35 * (d.revenue / m.max_rev) +
        0.25 * (d.completed_rides * 1.0 / m.max_comp) +
        0.25 * (COALESCE(d.average_rating, 4.0) / 5.0) +
        0.15 * (d.completion_rate / 100.0)
    ) * 100, 2) AS composite_score,
    RANK() OVER (ORDER BY (
        0.35 * (d.revenue / m.max_rev) +
        0.25 * (d.completed_rides * 1.0 / m.max_comp) +
        0.25 * (COALESCE(d.average_rating, 4.0) / 5.0) +
        0.15 * (d.completion_rate / 100.0)
    ) DESC) AS performance_rank
FROM DriverAggregates d
CROSS JOIN MaxBounds m
ORDER BY performance_rank ASC;

-- ----------------------------------------------------------
-- 8. QUERY 7: Monthly & Daily Revenue Trajectory
-- Tracks revenue over time to identify peak earnings windows.
-- ----------------------------------------------------------
SELECT 
    date,
    COUNT(*) AS total_bookings,
    SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_rides,
    ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END), 2) AS daily_realized_revenue,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN fare ELSE NULL END), 2) AS daily_avg_fare
FROM rides
GROUP BY date
ORDER BY date ASC;
