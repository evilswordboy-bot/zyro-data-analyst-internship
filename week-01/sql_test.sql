-- ==========================================================
-- ZYROO DATA ANALYST INTERNSHIP — TASK 01
-- Week 1: SQL Environment & Query Verification (SQLite)
-- Candidate: Sakthibalan
-- ==========================================================

-- ----------------------------------------------------------
-- 1. DDL: Create the Sales Table
-- ----------------------------------------------------------
DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    order_id INTEGER PRIMARY KEY,
    order_date TEXT NOT NULL,
    category TEXT NOT NULL,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    unit_price REAL NOT NULL CHECK(unit_price >= 0),
    total_sales REAL NOT NULL CHECK(total_sales >= 0)
);

-- ----------------------------------------------------------
-- 2. DML: Insert Sample Retail Transaction Data
-- ----------------------------------------------------------
INSERT INTO sales (order_id, order_date, category, product, quantity, unit_price, total_sales) VALUES
(1001, '2026-01-05', 'Electronics', 'Wireless Mouse', 2, 25.00, 50.00),
(1002, '2026-01-06', 'Electronics', 'Mechanical Keyboard', 1, 85.00, 85.00),
(1003, '2026-01-07', 'Office Supplies', 'Ergonomic Chair', 1, 150.00, 150.00),
(1004, '2026-01-08', 'Electronics', 'USB-C Hub', 3, 30.00, 90.00),
(1005, '2026-01-09', 'Office Supplies', 'Desk Organizer', 2, 20.00, 40.00),
(1006, '2026-01-10', 'Accessories', 'Laptop Sleeve', 2, 35.00, 70.00),
(1007, '2026-01-11', 'Electronics', 'Webcam HD', 1, 60.00, 60.00),
(1008, '2026-01-12', 'Accessories', 'Mousepad XL', 4, 15.00, 60.00),
(1009, '2026-01-13', 'Office Supplies', 'Whiteboard', 1, 45.00, 45.00),
(1010, '2026-01-14', 'Electronics', 'Noise-Canceling Headphones', 1, 120.00, 120.00);

-- ----------------------------------------------------------
-- 3. QUERY 1: Basic SELECT Verification
-- Purpose: Verify table creation and data ingestion by viewing all records.
-- ----------------------------------------------------------
SELECT 
    order_id, 
    order_date, 
    category, 
    product, 
    quantity, 
    unit_price, 
    total_sales
FROM sales;

-- ----------------------------------------------------------
-- 4. QUERY 2: Filtering (WHERE Clause)
-- Purpose: Filter for high-ticket orders where total_sales >= $80.
-- Demonstrates comparison operator and sorting.
-- ----------------------------------------------------------
SELECT 
    order_id, 
    order_date, 
    category, 
    product, 
    total_sales
FROM sales
WHERE total_sales >= 80.00
ORDER BY total_sales DESC;

-- ----------------------------------------------------------
-- 5. QUERY 3: Grouping & Counting (Mandatory Internship Query)
-- Purpose: Aggregate total number of transactions per product category.
-- ----------------------------------------------------------
SELECT 
    category, 
    COUNT(*) AS total
FROM sales
GROUP BY category
ORDER BY total DESC;

-- ----------------------------------------------------------
-- 6. QUERY 4: Advanced Aggregation (SUM, AVG, MIN, MAX)
-- Purpose: Calculate comprehensive business KPIs per category:
-- transaction volume, units sold, average ticket size, and total revenue.
-- ----------------------------------------------------------
SELECT 
    category,
    COUNT(*) AS transaction_count,
    SUM(quantity) AS total_units_sold,
    ROUND(AVG(total_sales), 2) AS avg_sale_value,
    ROUND(MIN(total_sales), 2) AS min_sale,
    ROUND(MAX(total_sales), 2) AS max_sale,
    ROUND(SUM(total_sales), 2) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;

-- ----------------------------------------------------------
-- 7. QUERY 5: Filtered Aggregation (HAVING Clause)
-- Purpose: Identify high-performing categories generating over $150 total revenue.
-- ----------------------------------------------------------
SELECT 
    category,
    SUM(total_sales) AS total_revenue
FROM sales
GROUP BY category
HAVING SUM(total_sales) > 150.00
ORDER BY total_revenue DESC;
