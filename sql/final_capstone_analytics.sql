-- ==============================================================================
-- ZYROO DATA ANALYTICS FINAL CAPSTONE PROJECT
-- Ride Analytics & Revenue Intelligence Platform
-- Production SQL Analytics & Star Schema Layer
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- 1. FACT TABLE & BASE TRANSACTION VALIDATION
-- ------------------------------------------------------------------------------
-- Validates ride status, realized revenue, lost fares, and rating null handling
SELECT 
    COUNT(*) AS total_rides,
    SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_rides,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_rides,
    ROUND(CAST(SUM(CASE WHEN ride_status = 'Completed' THEN 1.0 ELSE 0 END) / COUNT(*) * 100 AS NUMERIC), 2) AS completion_rate_pct,
    ROUND(CAST(SUM(CASE WHEN ride_status = 'Cancelled' THEN 1.0 ELSE 0 END) / COUNT(*) * 100 AS NUMERIC), 2) AS cancellation_rate_pct,
    SUM(fare) AS gross_booked_revenue,
    SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) AS realized_revenue,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN fare ELSE 0 END) AS lost_cancellation_revenue,
    ROUND(AVG(fare), 2) AS avg_booked_fare,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN fare END), 2) AS avg_completed_fare,
    ROUND(AVG(CASE WHEN ride_status = 'Cancelled' THEN fare END), 2) AS avg_cancelled_fare,
    ROUND(AVG(distance_km), 2) AS avg_distance_km,
    ROUND(AVG(rating), 2) AS avg_customer_rating
FROM rides_data;

-- ------------------------------------------------------------------------------
-- 2. TEMPORAL & DEMAND INTELLIGENCE (DAILY & DAY OF WEEK)
-- ------------------------------------------------------------------------------
SELECT 
    date,
    TO_CHAR(date::DATE, 'Day') AS day_name,
    CASE 
        WHEN EXTRACT(ISODOW FROM date::DATE) IN (6, 7) THEN 'Weekend'
        ELSE 'Weekday'
    END AS day_type,
    COUNT(*) AS ride_volume,
    SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_volume,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_volume,
    SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) AS daily_realized_revenue,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN fare END), 2) AS daily_avg_fare,
    ROUND(CAST(SUM(CASE WHEN ride_status = 'Cancelled' THEN 1.0 ELSE 0 END) / COUNT(*) * 100 AS NUMERIC), 2) AS daily_cancellation_rate_pct
FROM rides_data
GROUP BY date, TO_CHAR(date::DATE, 'Day'), day_type
ORDER BY date ASC;

-- ------------------------------------------------------------------------------
-- 3. LOCATION INTELLIGENCE & CORRIDOR CONCENTRATION
-- ------------------------------------------------------------------------------
-- Pickup Location Performance & Cancellation Hotspots
SELECT 
    pickup_location,
    COUNT(*) AS total_pickup_requests,
    SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_pickups,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_pickups,
    ROUND(CAST(SUM(CASE WHEN ride_status = 'Cancelled' THEN 1.0 ELSE 0 END) / COUNT(*) * 100 AS NUMERIC), 2) AS pickup_cancellation_rate_pct,
    SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) AS pickup_realized_revenue,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN fare ELSE 0 END) AS pickup_lost_fare,
    ROUND(AVG(distance_km), 2) AS avg_trip_distance_km
FROM rides_data
GROUP BY pickup_location
ORDER BY total_pickup_requests DESC;

-- Origin-Destination (OD) Corridor Flow Analysis
SELECT 
    pickup_location || ' -> ' || dropoff_location AS route_corridor,
    COUNT(*) AS corridor_ride_volume,
    SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_volume,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_volume,
    SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) AS corridor_realized_revenue,
    ROUND(AVG(fare), 2) AS avg_corridor_fare
FROM rides_data
GROUP BY pickup_location, dropoff_location
ORDER BY corridor_ride_volume DESC
LIMIT 10;

-- ------------------------------------------------------------------------------
-- 4. DRIVER PERFORMANCE BENCHMARKING & ROI QUADRANT
-- ------------------------------------------------------------------------------
SELECT 
    driver_id,
    COUNT(*) AS rides_assigned,
    SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS rides_completed,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS rides_cancelled,
    ROUND(CAST(SUM(CASE WHEN ride_status = 'Completed' THEN 1.0 ELSE 0 END) / COUNT(*) * 100 AS NUMERIC), 2) AS driver_completion_rate_pct,
    ROUND(CAST(SUM(CASE WHEN ride_status = 'Cancelled' THEN 1.0 ELSE 0 END) / COUNT(*) * 100 AS NUMERIC), 2) AS driver_cancellation_rate_pct,
    SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) AS realized_driver_revenue,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN fare ELSE 0 END) AS lost_driver_revenue,
    ROUND(AVG(rating), 2) AS driver_avg_rating,
    CASE 
        WHEN SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) = 0 AND AVG(rating) >= 4.30 THEN 'Tier 1: Elite Performer'
        WHEN SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) <= 1 AND AVG(rating) >= 4.20 THEN 'Tier 2: Strong Performer'
        WHEN SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) <= 2 THEN 'Tier 3: Core Fleet'
        ELSE 'Tier 4: Operational Attention Required'
    END AS performance_segment
FROM rides_data
GROUP BY driver_id
ORDER BY driver_cancellation_rate_pct ASC, realized_driver_revenue DESC;

-- ------------------------------------------------------------------------------
-- 5. RIDE TYPE & SERVICE TIER CONTRIBUTION
-- ------------------------------------------------------------------------------
SELECT 
    ride_type,
    COUNT(*) AS total_rides,
    SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_rides,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_rides,
    ROUND(CAST(SUM(CASE WHEN ride_status = 'Cancelled' THEN 1.0 ELSE 0 END) / COUNT(*) * 100 AS NUMERIC), 2) AS cancellation_rate_pct,
    SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) AS realized_revenue,
    ROUND(CAST(SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) / 36466.0 * 100 AS NUMERIC), 2) AS revenue_share_pct,
    ROUND(AVG(fare), 2) AS avg_booked_fare,
    ROUND(AVG(distance_km), 2) AS avg_trip_distance_km,
    ROUND(AVG(rating), 2) AS avg_customer_rating
FROM rides_data
GROUP BY ride_type
ORDER BY realized_revenue DESC;

-- ------------------------------------------------------------------------------
-- 6. PAYMENT METHOD RISK & FRICTION ANALYSIS
-- ------------------------------------------------------------------------------
SELECT 
    payment_method,
    COUNT(*) AS total_transactions,
    SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_transactions,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_transactions,
    ROUND(CAST(SUM(CASE WHEN ride_status = 'Cancelled' THEN 1.0 ELSE 0 END) / COUNT(*) * 100 AS NUMERIC), 2) AS method_cancellation_rate_pct,
    SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) AS realized_revenue,
    ROUND(CAST(SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) / 36466.0 * 100 AS NUMERIC), 2) AS revenue_share_pct,
    ROUND(AVG(fare), 2) AS avg_fare
FROM rides_data
GROUP BY payment_method
ORDER BY total_transactions DESC;

-- ------------------------------------------------------------------------------
-- 7. SCENARIO SIMULATION ENGINE (WHAT-IF MODELING)
-- ------------------------------------------------------------------------------
-- Scenario A: Baseline vs 92% Target Completion Rate (+7 Completed Rides)
WITH Baseline AS (
    SELECT 
        COUNT(*) AS base_total_rides,
        SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS base_completed_rides,
        SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) AS base_realized_revenue,
        AVG(CASE WHEN ride_status = 'Completed' THEN fare END) AS base_avg_completed_fare
    FROM rides_data
)
SELECT 
    'Scenario A: Target 92% Completion Rate' AS scenario_name,
    base_completed_rides,
    ROUND(base_completed_rides::NUMERIC / base_total_rides * 100, 1) AS base_completion_pct,
    base_realized_revenue,
    92 AS simulated_completed_rides,
    92.0 AS simulated_completion_pct,
    ROUND(base_realized_revenue + ((92 - base_completed_rides) * base_avg_completed_fare), 2) AS simulated_revenue,
    ROUND((92 - base_completed_rides) * base_avg_completed_fare, 2) AS incremental_revenue_gain,
    ROUND((((92 - base_completed_rides) * base_avg_completed_fare) / base_realized_revenue) * 100, 2) AS revenue_lift_pct
FROM Baseline;

-- Scenario B: Baseline vs 50% Cancellation Reduction (Cut from 15 to 7 Cancellations)
WITH Baseline AS (
    SELECT 
        SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS base_cancellations,
        SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) AS base_realized_revenue,
        AVG(CASE WHEN ride_status = 'Cancelled' THEN fare END) AS base_avg_cancelled_fare
    FROM rides_data
)
SELECT 
    'Scenario B: 50% Cancellation Reduction' AS scenario_name,
    base_cancellations,
    15.0 AS base_cancellation_pct,
    base_realized_revenue,
    7 AS simulated_cancellations,
    7.0 AS simulated_cancellation_pct,
    ROUND(base_realized_revenue + ((base_cancellations - 7) * base_avg_cancelled_fare), 2) AS simulated_revenue,
    ROUND((base_cancellations - 7) * base_avg_cancelled_fare, 2) AS incremental_revenue_recaptured,
    ROUND((((base_cancellations - 7) * base_avg_cancelled_fare) / base_realized_revenue) * 100, 2) AS revenue_lift_pct
FROM Baseline;
