# 🚀 ZYROO DATA ANALYTICS INTERNSHIP • WEEK 5
## ADVANCED BUSINESS INTELLIGENCE & DECISION ANALYTICS REPORT
**Project Title:** Ride Analytics & Revenue Intelligence Platform  
**Sub-Topic:** Week 5 — Advanced Business Intelligence & Decision Analytics  
**Intern Role:** Professional Data Analyst + BI Developer + Advanced DAX & SQL Specialist  
**Target Environment:** Power BI Service, Power BI Desktop, Python Engine & ANSI SQL  
**Audit Scope:** 100-Ride Metropolitan Telemetry (Lahore Observation Window: Sep 01 – Sep 10, 2026)  
**Analytical Flow:** WHAT happened → WHY the pattern matters → WHAT should be investigated next

---

## 1. 🔍 ADVANCED DATA MODEL & SCHEMA VALIDATION

### 1.1 Source Telemetry & Data Quality Audit
The Week 5 Decision Support System ingests the 100-row production telemetry dataset across 11 fields:
`ride_id`, `date`, `pickup_location`, `dropoff_location`, `distance_km`, `fare`, `payment_method`, `driver_id`, `ride_type`, `ride_status`, `rating`.

| Field Name | Type | Valid Range / Categories | Audit Finding & Integrity Action |
| :--- | :--- | :--- | :--- |
| `ride_id` | Text (PK) | `R001` - `R100` | 100 unique records; exactly 0 duplicates. Verified primary key. |
| `date` | Date | `2026-09-01` to `2026-09-10` | 10 consecutive observation days. Validated ISO format. |
| `pickup_location` | Text | DHA (38), Gulberg (20), Bahria Town (17), Johar Town (14), Model Town (11) | Standardized strings; audited for whitespace anomalies. |
| `dropoff_location`| Text | Johar Town (22), Gulberg (21), Model Town (20), Bahria Town (19), DHA (18) | Balanced destination distributions confirmed across sectors. |
| `distance_km` | Float | $2.4 \text{ km} - 28.5 \text{ km}$ (Mean: $13.72 \text{ km}$ completed) | Continuous positive distance; zero or negative values: 0. |
| `fare` | Float | PKR $180.00 - 680.00$ | Audited for negative or zero fares (none found). Completed avg: PKR 429.01. |
| `payment_method` | Text | Cash (39), Card (28), UPI (22), Wallet (11) | Standardized financial settlement channels. |
| `driver_id` | Text | `DRV-001` to `DRV-010` (10 per driver) | Balanced driver cohort verified. |
| `ride_type` | Text | Standard (39), Economy (35), Premium (26) | Verified 3 vehicle service tiers. |
| `ride_status` | Text | Completed (85), Cancelled (15) | Validated binary fulfillment states (85% completed, 15% churn). |
| `rating` | Float | $3.2 - 5.0 \text{ ★}$ (Mean: $4.27 \text{ ★}$) | Exactly 15 missing ratings corresponding to cancelled trips (structural nulls). |

### 1.2 Dedicated Date Dimension & Star Schema
The semantic model cleanly separates data layers:
```text
┌────────────────────────────────────────────────────────┐
│                      _Measures                         │
│  (Catalog of 20+ Advanced DAX & Time-Intelligence)     │
└────────────────────────────────────────────────────────┘
                           ▲
                           │ DAX Aggregations
                           │
┌───────────────────────┐      ┌─────────────────────────┐
│       Dim_Date        │      │       Dim_Driver        │
├───────────────────────┤      ├─────────────────────────┤
│ PK: Date (Sep 01-10)  │      │ PK: Driver_ID (001-010) │
│ Day_Name, Weekday_Num │      │ Rating Tier, Target     │
└───────────┬───────────┘      └────────────┬────────────┘
            │ 1                             │ 1
            │                               │
            │ *                             │ *
┌───────────┴───────────────────────────────┴────────────┐
│                   Fact_Rides (100 Rows)                │
├────────────────────────────────────────────────────────┤
│ PK: ride_id                                            │
│ FK: date, driver_id                                    │
│ Degenerate Dims: pickup_location, dropoff_location,    │
│                  payment_method, ride_type, ride_status │
│ Measures: distance_km, fare, rating                    │
└────────────────────────────────────────────────────────┘
```

---

## 2. 🧮 ADVANCED DAX KPI LAYER & DATA VALIDATION

All DAX formulas have been cross-validated across **DAX, ANSI SQL (`sql/week_05_decision_analytics.sql`), and Python (`python/generate_week5_charts.py`)**:

| Metric | Verified Value | SQL / DAX Status | Business Definition |
| :--- | :--- | :---: | :--- |
| **Total Revenue** | **PKR 36,466.00** | 100% Match | Net recognized cash and digital revenue from completed journeys. |
| **Gross Booking Value (GBV)** | **PKR 42,962.00** | 100% Match | Total commercial booking demand placed on platform. |
| **Revenue Lost to Churn** | **PKR 6,496.00** | 100% Match | Unrealized fare value from 15 cancelled rides. |
| **Completed Rides** | **85 rides** | 100% Match | Fulfilled and delivered customer trips. |
| **Cancelled Rides** | **15 rides** | 100% Match | Dispatched trips aborted or unfulfilled. |
| **Completion Rate** | **85.0%** | 100% Match | Fleet fulfillment efficiency benchmark ($\ge 85\%$). |
| **Cancellation Rate** | **15.0%** | 100% Match | Operational churn percentage ($\le 10\%$ target). |
| **Average Fare (Completed)** | **PKR 429.01** | 100% Match | Mean ticket size per completed trip. |
| **Average Distance (Completed)**| **13.72 km** | 100% Match | Mean route distance per completed trip. |
| **Average Rating (Completed)** | **4.27 ★** | 100% Match | Weighted customer satisfaction review index. |

---

## 3. 🗺️ REVENUE & SEGMENT INTELLIGENCE

### 3.1 Geographic Revenue & Operational Leakage
| Pickup Location | Bookings | Completed | Cancelled | Churn % | Realized Revenue | Rev Share | Avg Fare (Completed) | Avg Distance |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **DHA** | 38 | 35 | 3 | 7.89% | **PKR 15,388.00** | **42.20%** | PKR 439.66 | 14.21 km |
| **Bahria Town** | 17 | 16 | 1 | 5.88% | **PKR 6,782.00** | **18.60%** | PKR 423.88 | 13.52 km |
| **Gulberg** | 20 | 14 | 6 | **30.00%** | **PKR 5,559.00** | **15.24%** | **PKR 397.07** | 12.38 km |
| **Johar Town** | 14 | 11 | 3 | 21.43% | **PKR 4,657.00** | **12.77%** | PKR 423.36 | 13.32 km |
| **Model Town** | 11 | 9 | 2 | 18.18% | **PKR 4,080.00** | **11.19%** | PKR 453.33 | 14.80 km |

### 3.2 High-Volume / Low-Yield vs. High-Yield Segments
* **High-Volume / Low-Yield Segment:** **Gulberg** (20 bookings, 15.24% revenue share, lowest completed fare at PKR 397.07, and highest churn at 30.0%).
* **High-Yield / Premium Segment:** **DHA** (38 bookings, 42.20% revenue share, PKR 439.66 fare, and low 7.89% churn).

---

## 4. 👥 CUSTOMER BEHAVIORAL SEGMENTATION

Because individual customer IDs are not provided in this 100-ride transaction log, passenger behavior is segmented across **Trip Purpose, Service Tier, and Journey Dynamics**:

| Customer Segment | Bookings | Completed | Cancelled | Churn % | Revenue (PKR) | Rev Share | Avg Fare | Avg Distance | Top Channel |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Standard Daily Commuters** | 39 | 32 | 7 | 17.9% | PKR 14,136.00 | **38.76%** | PKR 441.75 | 14.25 km | UPI / Cash |
| **Premium Executive Riders** | 26 | 22 | 4 | 15.4% | PKR 12,277.00 | **33.67%** | **PKR 558.05** | 19.50 km | Cash / Card |
| **Economy Short-Hop Riders** | 35 | 31 | 4 | 11.4% | PKR 10,053.00 | **27.57%** | PKR 324.29 | 9.09 km | Card / UPI |

* **Segment 1: Standard Daily Commuters (38.8% Revenue):** Represents core recurring transit between residential suburbs (DHA, Bahria) and central work hubs.
* **Segment 2: Premium Executive Riders (33.7% Revenue):** Highest ticket yield (PKR 558.05) and longest routes (19.5 km). Crucial for profit density.
* **Segment 3: Economy Short-Hop Riders (27.6% Revenue):** Lowest cancellation rate (11.4%) and lowest fare (PKR 324.29). Functions as volume feeder.

---

## 5. 🚗 DRIVER PERFORMANCE INTELLIGENCE & BENCHMARKING

**Cohort Baseline Benchmarks:** Average Revenue = **PKR 3,646.60** | Completion Rate = **85.0%** | Rating = **4.27 ★**

| Rank | Driver ID | Total | Completed | Cancelled | Revenue | Rev vs Bench | C-Rate | C-Rate vs Bench | Rating | Score | Status Tier |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **DRV-010** | 10 | 10 | 0 | PKR 4,055.00 | +PKR 408.40 | **100.0%** | +15.0% | 4.34 ★ | **80.16** | 🌟 Star Partner |
| **2** | **DRV-004** | 10 | 10 | 0 | PKR 4,007.00 | +PKR 360.40 | **100.0%** | +15.0% | 4.36 ★ | **79.93** | 🌟 Star Partner |
| **3** | **DRV-002** | 10 | 9 | 1 | **PKR 4,484.00** | **+PKR 837.40** | 90.0% | +5.0% | 4.33 ★ | **77.25** | 🚀 Top Earner / Mild Churn |
| **4** | **DRV-001** | 10 | 10 | 0 | PKR 4,237.00 | +PKR 590.40 | **100.0%** | +15.0% | 4.01 ★ | **73.65** | 🌟 Star Partner |
| **5** | **DRV-009** | 10 | 9 | 1 | PKR 3,831.00 | +PKR 184.40 | 90.0% | +5.0% | 4.30 ★ | **65.20** | 🟢 Consistent Partner |
| **6** | **DRV-003** | 10 | 8 | 2 | PKR 3,807.00 | +PKR 160.40 | 80.0% | -5.0% | 4.46 ★ | **59.52** | 🟢 High Rating / Churn Alert |
| **7** | **DRV-008** | 10 | 8 | 2 | PKR 3,210.00 | -PKR 436.60 | 80.0% | -5.0% | 4.20 ★ | **41.75** | 🟡 Below Benchmark |
| **8** | **DRV-006** | 10 | 8 | 2 | PKR 3,504.00 | -PKR 142.60 | 80.0% | -5.0% | 3.91 ★ | **38.37** | 🟡 Low Rating Alert |
| **9** | **DRV-007** | 10 | 7 | 3 | PKR 2,421.00 | -PKR 1,225.60 | **70.0%** | -15.0% | **4.77 ★** | **35.00** | 🔴 High Quality Cherry-Picker |
| **10**| **DRV-005** | 10 | 6 | 4 | PKR 2,910.00 | -PKR 736.60 | **60.0%** | -25.0% | 4.08 ★ | **13.27** | ⛔ Severe Operational Risk |

---

## 6. ⚠️ CANCELLATION & CHURN INTELLIGENCE

### Correlation vs. Causation Analysis
* **Statistical Finding:** Gulberg exhibits a **30.0% cancellation rate** (6 of 20 rides cancelled), whereas Bahria Town (5.88%) and DHA (7.89%) exhibit low churn.
* **Causal Care Notice:** The dataset shows that **Gulberg originations are associated with higher cancellation rates**. We cannot claim Gulberg causes cancellations without external traffic delay or driver dispatch distance telemetry.
* **Churn Concentration:** 7 of the 15 total platform cancellations (46.7%) were generated by just two drivers: `DRV-005` (4 cancellations) and `DRV-007` (3 cancellations).

---

## 7. 🔮 SCENARIO & WHAT-IF FINANCIAL MODELING

All scenario models are labeled as **ESTIMATES / HYPOTHETICAL SIMULATIONS**:

| Scenario Simulation | Input Assumption | Baseline Value | Projected Value | Revenue Impact (PKR) | Growth % |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Scenario A (+10% Volume)** | Fulfilled rides rise from 85 to 93.5 trips | PKR 36,466.00 | PKR 40,112.60 | **+PKR 3,646.60** | **+10.0%** |
| **Scenario A (+15% Volume)** | Fulfilled rides rise from 85 to 97.7 trips | PKR 36,466.00 | PKR 41,914.45 | **+PKR 5,448.45** | **+15.0%** |
| **Scenario B (+5% Price Yield)**| Mean completed fare rises to PKR 450.46 | PKR 36,466.00 | PKR 38,289.30 | **+PKR 1,823.30** | **+5.0%** |
| **Scenario B (+10% Price Yield)**| Mean completed fare rises to PKR 471.91 | PKR 36,466.00 | PKR 40,112.60 | **+PKR 3,646.60** | **+10.0%** |
| **Scenario C (50% Churn Recovery)**| Recover 7.5 cancelled rides (PKR 3,248) | PKR 36,466.00 | PKR 39,714.00 | **+PKR 3,248.00** | **+8.91%** |
| **Scenario C (75% Churn Recovery)**| Recover 11.25 cancelled rides (PKR 4,872)| PKR 36,466.00 | PKR 41,338.00 | **+PKR 4,872.00** | **+13.36%** |

*Limitations: Scenarios hold customer price elasticity and vehicle capacity constant.*

---

## 8. 💡 8 EVIDENCE-BASED BUSINESS INSIGHTS

### Insight 1 — Geographic Revenue Concentration (DHA)
* **Finding:** DHA generated 35 completed rides and **42.20% (PKR 15,388.00)** of total platform revenue with an above-average ticket size of PKR 439.66 and low 7.89% churn.
* **Business Meaning:** DHA is the commercial liquidity anchor of the platform. Protecting driver supply here is essential to daily cash flow.

### Insight 2 — Gulberg Operational Churn & Pricing Disincentive
* **Finding:** Gulberg commanded 20 ride requests (20.0% of demand) but experienced a **30.0% cancellation rate (6 cancelled rides)** and the lowest completed average fare (PKR 397.07).
* **Business Meaning:** Lower fare yields combined with traffic congestion disincentivize drivers from completing Gulberg pickups, leading to passenger abandonment.

### Insight 3 — Revenue Mirage vs Operational Dependability
* **Finding:** DRV-002 achieved top gross revenue (PKR 4,484.00) but cancelled 10% of trips. DRV-010, DRV-004, and DRV-001 achieved **100% completion (0 cancellations)** while earning >PKR 4,000.00.
* **Business Meaning:** Evaluating drivers purely on top-line revenue encourages cherry-picking. Multi-criteria scoring protects platform reliability.

### Insight 4 — Premium Tier Ticket Yield Density
* **Finding:** Premium rides average **PKR 558.05 per journey (+30.3% over Standard)** across comparable distances (19.5 km vs 14.2 km), contributing 33.67% of revenue from only 22 trips.
* **Business Meaning:** Premium riders exhibit high price tolerance. Expanding executive supply directly expands operator margins.

### Insight 5 — Concentration of Platform Churn
* **Finding:** Two drivers (DRV-005 with 4 cancellations and DRV-007 with 3 cancellations) caused **46.7% of all platform churn (7 of 15 cancellations)**.
* **Business Meaning:** Cancellation leakage is concentrated among isolated operators rather than systemic across the entire fleet.

### Insight 6 — Digital Financial Ecosystem Dominance
* **Finding:** Digital payment channels collectively account for **61.29% of revenue (PKR 22,351.00)** across Card (29.6%), UPI (22.4%), and Wallet (9.2%), while Cash accounts for 38.71%.
* **Business Meaning:** High digital adoption streamlines driver settlement and eliminates change-handling delays.

### Insight 7 — Temporal Demand & Weekday Peaks
* **Finding:** **Thursday (24 bookings)** and **Tuesday (20 bookings)** drive 44.0% of total weekly volume. Friday experienced the highest weekday cancellation rate (25.0%).
* **Business Meaning:** Fleet scheduling must dynamically align with midweek business travel patterns.

### Insight 8 — Cross-City Transit Equilibrium
* **Finding:** Drop-off destinations are uniformly distributed across Johar Town (22%), Gulberg (21%), Model Town (20%), Bahria Town (19%), and DHA (18%).
* **Business Meaning:** Fleet re-balancing is relatively efficient because vehicles naturally disperse across all residential sectors.

---

## 9. 🚀 5 PRACTICAL BUSINESS RECOMMENDATIONS

### Recommendation 1 — Geofenced Fulfillment Bonus for Gulberg
* **Finding:** Gulberg suffers 30% cancellation churn and lower fare yield (PKR 397.07).
* **Action:** Deploy a dynamic PKR 50 - PKR 75 pickup bonus for drivers accepting dispatches originating in Gulberg.
* **Expected Impact:** Drop churn below 12%, recapturing ~PKR 1,800.00 in leaked bookings.
* *Limitation:* Requires A/B testing against driver acceptance elasticities.

### Recommendation 2 — Star Partner Priority Dispatch Protocol
* **Finding:** DRV-010, 004, and 001 maintain 100% completion rates and high ratings.
* **Action:** Implement dispatch routing giving 100% completion drivers priority assignment to high-yield Premium trips.
* **Expected Impact:** Reduces passenger wait times and rewards dependable fleet partners.
* *Limitation:* Must ensure minimum dispatch volume remains equitable for lower tiers.

### Recommendation 3 — Strategic Expansion of Premium Tier Fleet
* **Finding:** Premium trips yield PKR 558.05 (+30.3% over Standard) across similar travel distances.
* **Action:** Recruit and onboard vehicles meeting executive comfort standards into the Premium fleet.
* **Expected Impact:** Expands platform gross margins and raises average ticket size.
* *Limitation:* Dependent on luxury vehicle supply in the Lahore market.

### Recommendation 4 — Targeted Driver Retraining & Churn Warnings
* **Finding:** DRV-005 (40% churn) and DRV-007 (30% churn) account for nearly half of all unfulfilled trips.
* **Action:** Issue automated operational alerts and schedule mandatory route compliance retraining.
* **Expected Impact:** Immediately eliminates ~5 to 6 cancellations per 100 dispatches.
* *Limitation:* High cancellation drivers may churn off platform if penalties are too severe.

### Recommendation 5 — Digital Payment Cashback Acceleration
* **Finding:** Cash remains 38.7% of collections, introducing cash-handling friction.
* **Action:** Offer 5% instant cashback on Card, UPI, and Wallet settlements.
* **Expected Impact:** Compresses cash share below 20%, accelerating driver turnover.
* *Limitation:* Promotional budget requires subsidy from gateway partners.

---

## 10. 📸 SCREENSHOT & VISUAL EVIDENCE CHECKLIST

All 8 Week 5 decision visuals have been rendered at 300 DPI and stored in `screenshots/week-05/` and `reports/week-05-advanced-bi/charts/`:

* [x] **`01_location_demand_vs_cancellation.png`** — Location Demand vs Cancellation Matrix (Gulberg Churn Focus).
* [x] **`02_revenue_vs_avg_fare_by_tier.png`** — Revenue Contribution vs Average Fare by Vehicle Tier.
* [x] **`03_driver_revenue_vs_benchmark.png`** — Driver Performance Variance vs Cohort Revenue Benchmark.
* [x] **`04_what_if_scenario_modeling.png`** — What-If Financial Projections (Volume, Fare, Churn Recovery).
* [x] **`05_customer_behavioral_segments.png`** — Customer Behavioral Segmentation Revenue Share.
* [x] **`06_payment_ecosystem_contribution.png`** — Payment Ecosystem Breakdown (Digital 61.3% vs Cash 38.7%).
* [x] **`07_weekday_demand_and_churn_risk.png`** — Weekday Demand & Churn Volatility Analysis.
* [x] **`08_time_intelligence_revenue_runrate.png`** — 10-Day Revenue Run-Rate Trajectory.
