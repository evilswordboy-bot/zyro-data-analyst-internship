-- ==============================================================================
-- ZYROO DATA ANALYTICS INTERNSHIP • WEEK 5
-- Advanced Business Intelligence & Decision Analytics Validation Pipeline
-- Database dialect: SQLite / PostgreSQL ANSI SQL Compatible
-- ==============================================================================

-- 1. BASELINE REVENUE & KPI RECONCILIATION
-- Validates: Total Revenue, Completed Rides, Cancellations, Completion Rate
SELECT 
    COUNT(*) AS total_dispatched_rides,
    SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_rides,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_rides,
    ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN 1.0 ELSE 0.0 END) / COUNT(*) * 100, 2) AS completion_rate_pct,
    ROUND(SUM(CASE WHEN ride_status = 'Cancelled' THEN 1.0 ELSE 0.0 END) / COUNT(*) * 100, 2) AS cancellation_rate_pct,
    ROUND(SUM(fare), 2) AS gross_booking_value,
    ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END), 2) AS net_realized_revenue,
    ROUND(SUM(CASE WHEN ride_status = 'Cancelled' THEN fare ELSE 0 END), 2) AS revenue_lost_to_churn,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN fare END), 2) AS avg_fare_completed,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN distance_km END), 2) AS avg_distance_completed,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN rating END), 2) AS avg_rating_completed
FROM rides_data;


-- 2. LOCATION INTELLIGENCE & REVENUE LEAKAGE
-- Highlights High Volume vs High Churn (Gulberg 30% Churn vs DHA 7.89% Churn)
SELECT 
    pickup_location,
    COUNT(*) AS total_rides,
    SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_rides,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_rides,
    ROUND(SUM(CASE WHEN ride_status = 'Cancelled' THEN 1.0 ELSE 0.0 END) / COUNT(*) * 100, 2) AS cancellation_rate_pct,
    ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END), 2) AS realized_revenue,
    ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) / (SELECT SUM(fare) FROM rides_data WHERE ride_status = 'Completed') * 100, 2) AS revenue_share_pct,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN fare END), 2) AS avg_fare_completed,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN distance_km END), 2) AS avg_distance_completed
FROM rides_data
GROUP BY pickup_location
ORDER BY realized_revenue DESC;


-- 3. VEHICLE TIER & BEHAVIORAL SEGMENTATION
-- Analyzes: Standard (Core Volume), Premium (High Yield Margin), Economy (Utility)
SELECT 
    ride_type AS segment_name,
    COUNT(*) AS total_rides,
    SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_rides,
    SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_rides,
    ROUND(SUM(CASE WHEN ride_status = 'Cancelled' THEN 1.0 ELSE 0.0 END) / COUNT(*) * 100, 2) AS cancellation_rate_pct,
    ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END), 2) AS realized_revenue,
    ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) / (SELECT SUM(fare) FROM rides_data WHERE ride_status = 'Completed') * 100, 2) AS revenue_share_pct,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN fare END), 2) AS avg_fare_completed,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN distance_km END), 2) AS avg_distance_completed,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN rating END), 2) AS avg_rating_completed
FROM rides_data
GROUP BY ride_type
ORDER BY realized_revenue DESC;


-- 4. FINANCIAL SETTLEMENT CHANNEL BREAKDOWN
SELECT 
    payment_method,
    COUNT(*) AS total_bookings,
    SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_rides,
    ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END), 2) AS realized_revenue,
    ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END) / (SELECT SUM(fare) FROM rides_data WHERE ride_status = 'Completed') * 100, 2) AS revenue_share_pct,
    ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN fare END), 2) AS avg_fare
FROM rides_data
GROUP BY payment_method
ORDER BY realized_revenue DESC;


-- 5. DRIVER PERFORMANCE INTELLIGENCE & BENCHMARK COMPARISON
-- Benchmarks: Cohort Average Revenue = PKR 3,646.60; Cohort Completion Rate = 85.0%
WITH DriverStats AS (
    SELECT 
        driver_id,
        COUNT(*) AS total_rides,
        SUM(CASE WHEN ride_status = 'Completed' THEN 1 ELSE 0 END) AS completed_rides,
        SUM(CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_rides,
        ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN 1.0 ELSE 0.0 END) / COUNT(*) * 100, 1) AS completion_rate,
        ROUND(SUM(CASE WHEN ride_status = 'Completed' THEN fare ELSE 0 END), 2) AS realized_revenue,
        ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN rating END), 2) AS avg_rating,
        ROUND(AVG(CASE WHEN ride_status = 'Completed' THEN distance_km END), 2) AS avg_distance
    FROM rides_data
    GROUP BY driver_id
),
CohortBenchmark AS (
    SELECT 
        ROUND(AVG(realized_revenue), 2) AS bench_rev,
        ROUND(AVG(completion_rate), 1) AS bench_crate,
        ROUND(AVG(avg_rating), 2) AS bench_rating
    FROM DriverStats
)
SELECT 
    d.driver_id,
    d.total_rides,
    d.completed_rides,
    d.cancelled_rides,
    d.realized_revenue,
    ROUND(d.realized_revenue - b.bench_rev, 2) AS rev_diff_vs_bench,
    d.completion_rate,
    ROUND(d.completion_rate - b.bench_crate, 1) AS crate_diff_vs_bench,
    d.avg_rating,
    ROUND(d.avg_rating - b.bench_rating, 2) AS rating_diff_vs_bench,
    d.avg_distance,
    CASE 
        WHEN d.completion_rate = 100.0 THEN '🌟 Star Tier (100% Dependability)'
        WHEN d.completion_rate >= 80.0 THEN '🟢 Reliable Core'
        WHEN d.completion_rate >= 70.0 THEN '🟡 Churn Alert'
        ELSE '🔴 Critical Risk (Action Required)'
    END AS operational_status
FROM DriverStats d
CROSS JOIN CohortBenchmark b
ORDER BY d.realized_revenue DESC;
