# 🚀 ZYROO DATA ANALYTICS INTERNSHIP — WEEK 3 REPORT
## Ride Analytics & Revenue Intelligence Platform
### Task 03: Revenue & Driver Performance Analysis

**Candidate:** Sakthibalan  
**Role:** Data Analyst / Business Intelligence Analyst  
**Organization:** ZYROO Internship Program  
**Category:** Revenue Intelligence & Driver Fleet Operations  
**Date:** September 16, 2026  

---

## 1. Executive Summary & Business Problem

A mature ride-hailing business requires deep operational intelligence beyond basic booking volume. Management must understand:
1. **Revenue Origin & Leakage**: Which locations, payment channels, and ride tiers produce revenue, and how much is lost to cancellations?
2. **Driver Productivity & Quality**: Which drivers maximize completed trips while sustaining superior customer satisfaction?
3. **Operational Churn**: Which drivers suffer from high cancellation rates, and what is the resulting financial loss?
4. **Demand vs Revenue Imbalance**: Which geographical zones suffer from high demand but low revenue yields?

This report delivers a data-driven financial and driver performance evaluation based on **100 verified production rides** from the September 2026 telemetry.

---

## 2. Dataset Overview

The dataset bridges customer demand telemetry from Week 2 into operational finance and fleet analytics for Week 3.

### Schema Inventory
| Column Name | Data Type | Non-Null Count | Domain Description |
|---|---|---|---|
| `ride_id` | String / Object | 100 / 100 (100%) | Unique alphanumeric ride identifier (`R001` - `R100`) |
| `date` | Datetime64 | 100 / 100 (100%) | Booking timestamp (`2026-09-01` to `2026-09-10`) |
| `pickup_location` | String / Object | 100 / 100 (100%) | Trip origin hub (5 metropolitan zones) |
| `dropoff_location` | String / Object | 100 / 100 (100%) | Destination zone |
| `distance_km` | Float64 | 100 / 100 (100%) | Estimated trip transit distance (km) |
| `fare` | Float64 / Int64 | 100 / 100 (100%) | Gross booking fare in Pakistani Rupees (PKR) |
| `payment_method` | String / Object | 100 / 100 (100%) | Settlement channel (`Cash`, `Card`, `UPI`, `Wallet`) |
| `driver_id` | String / Object | 100 / 100 (100%) | Fleet partner identifier (`DRV-001` to `DRV-010`) |
| `ride_type` | String / Object | 100 / 100 (100%) | Service tier (`Economy`, `Standard`, `Premium`) |
| `ride_status` | String / Object | 100 / 100 (100%) | Trip outcome (`Completed` vs `Cancelled`) |
| `rating` | Float64 | 85 / 100 (85%) | Customer feedback score (1.0 to 5.0 ★) |

---

## 3. Data Preparation & Quality Assurance

* **Deduplication:** Confirmed 0 duplicate `ride_id` records.
* **Range Validation:** All fares strictly non-negative (`PKR 250.00` to `PKR 680.00`).
* **Null Handling:** Missing ratings (15 records) coincide exactly with `Cancelled` rides. In ride-hailing business rules, cancelled trips do not solicit passenger reviews; these structural nulls were appropriately preserved.
* **Revenue Recognition Rule:**
  * **Completed Rides (85 rides):** Revenue counted towards realized earnings.
  * **Cancelled Rides (15 rides):** Revenue categorized as unrealized churn loss.

---

## 4. Core Revenue KPIs

$$\text{Average Revenue per Completed Ride} = \frac{\text{Total Realized Revenue}}{\text{Completed Rides}} = \frac{\text{PKR } 36,466.00}{85} = \text{PKR } 429.01$$

| Metric KPI | Value | Financial & Operational Interpretation |
|---|---|---|
| **Total Bookings** | `100 rides` | Gross marketplace booking volume demand |
| **Completed Rides** | `85 rides` | Net successfully executed journeys (`85.0%`) |
| **Cancelled Rides** | `15 rides` | Total operational churn (`15.0%`) |
| **Total Realized Revenue** | `PKR 36,466.00` | Net recognized passenger fares |
| **Gross Booking Value (GBV)** | `PKR 42,962.00` | Total pipeline booking potential |
| **Unrealized Lost Revenue** | `PKR 6,496.00` | Financial leakage from ride cancellations |
| **Average Fare (Completed)** | `PKR 429.01` | Average passenger ticket size |
| **Fleet Driver Rating Mean** | `4.27 / 5.00 ★` | Aggregate customer satisfaction score |

---

## 5. Temporal Revenue Trajectory (Daily Analysis)

Fleet revenue over the 10-day observation window shows distinct utilization cycles:

| Date | Bookings | Completed | Daily Revenue (PKR) | Avg Fare (PKR) | Performance Context |
|---|---|---|---|---|---|
| **2026-09-01** | 11 | 11 | PKR 4,595.00 | PKR 417.73 | Strong weekday demand (100% completion) |
| **2026-09-02** | 11 | 11 | PKR 4,794.00 | PKR 435.82 | Steady mid-week revenue |
| **2026-09-03** | 12 | 10 | PKR 4,582.00 | PKR 458.20 | 2 cancellations observed |
| **2026-09-04** | 8 | 8 | PKR 3,344.00 | PKR 418.00 | Mid-week demand dip |
| **2026-09-05** | **14** | **12** | **PKR 5,411.00** | **PKR 450.92** | **Peak revenue & volume day of period** |
| **2026-09-06** | 7 | 4 | PKR 1,685.00 | PKR 421.25 | Lowest revenue day (3 cancellations / 43% churn) |
| **2026-09-07** | 9 | 6 | PKR 2,710.00 | PKR 451.67 | 3 cancellations observed |
| **2026-09-08** | 9 | 6 | PKR 2,594.00 | PKR 432.33 | 3 cancellations observed |
| **2026-09-09** | 7 | 5 | PKR 2,009.00 | PKR 401.80 | Low volume day |
| **2026-09-10** | 12 | 12 | PKR 4,742.00 | PKR 395.17 | Rebound to 100% completion |

* **Peak Revenue Date:** `September 05, 2026` (**PKR 5,411.00**, 14 bookings).
* **Trough Revenue Date:** `September 06, 2026` (**PKR 1,685.00**, heavily impacted by 42.9% churn).

---

## 6. Revenue by Pickup Location (Demand vs Yield)

| Pickup Hub | Total Bookings | Completed | Realized Revenue | Revenue Share | Avg Fare (PKR) | Yield Diagnosis |
|---|---|---|---|---|---|---|
| **DHA** | **38** | **35** | **PKR 15,388.00** | **42.20%** | PKR 439.66 | **High Demand + High Revenue** (Primary hub) |
| **Bahria Town** | 17 | 16 | PKR 6,782.00 | 18.60% | PKR 423.88 | Consistent performance & high completion (94.1%) |
| **Gulberg** | 20 | 14 | PKR 5,559.00 | 15.24% | PKR 397.07 | **High Demand + Low Yield** (20% demand, 15% rev) |
| **Johar Town** | 14 | 11 | PKR 4,657.00 | 12.77% | PKR 423.36 | Moderate revenue contributor |
| **Model Town** | 11 | 9 | PKR 4,080.00 | 11.19% | **PKR 453.33** | **Low Demand + Highest Avg Fare** (High value) |

---

## 7. Revenue by Payment Method

| Payment Method | Completed Rides | Realized Revenue | Revenue Share | Volume Share | Avg Fare (PKR) |
|---|---|---|---|---|---|
| **Cash** | **32** | **PKR 14,115.00** | **38.71%** | 37.65% | PKR 441.09 |
| **Card** | 25 | PKR 10,801.00 | 29.62% | 29.41% | PKR 432.04 |
| **UPI** | 20 | PKR 8,181.00 | 22.43% | 23.53% | PKR 409.05 |
| **Wallet** | 8 | PKR 3,369.00 | 9.24% | 9.41% | PKR 421.13 |

* **Leading Method:** **Cash** dominates both completed volume (37.6%) and revenue (38.7%).
* **Digital Ecosystem:** Digital payment channels collectively represent **61.29% of revenue** (Card + UPI + Wallet).

---

## 8. Revenue & Fare Yield by Ride Type Tier

| Ride Type Tier | Completed Rides | Realized Revenue | Revenue Share | Avg Fare (PKR) | Strategic Role |
|---|---|---|---|---|---|
| **Standard** | **32** | **PKR 14,136.00** | **38.76%** | PKR 441.75 | Volume & revenue workhorse |
| **Premium** | 22 | PKR 12,277.00 | 33.67% | **PKR 558.05** | Highest ticket size & margin expander |
| **Economy** | 31 | PKR 10,053.00 | 27.57% | PKR 324.29 | Customer acquisition & entry volume |

---

## 9. Driver Performance Matrix

Analysis across all 10 fleet drivers:

| Driver ID | Total Rides | Completed | Cancelled | Revenue (PKR) | Avg Rating | Avg Dist (km) | Completion % | Cancellation % | Avg Fare (PKR) |
|---|---|---|---|---|---|---|---|---|---|
| `DRV-001` | 10 | 10 | 0 | PKR 4,237.00 | 4.01 ★ | 13.47 | 100.0% | 0.0% | PKR 423.70 |
| `DRV-002` | 10 | 9 | 1 | **PKR 4,484.00** | 4.33 ★ | 16.50 | 90.0% | 10.0% | **PKR 498.22** |
| `DRV-003` | 10 | 8 | 2 | PKR 3,807.00 | 4.46 ★ | 15.37 | 80.0% | 20.0% | PKR 475.88 |
| `DRV-004` | 10 | 10 | 0 | PKR 4,007.00 | 4.36 ★ | 12.58 | 100.0% | 0.0% | PKR 400.70 |
| `DRV-005` | 10 | 6 | 4 | PKR 2,910.00 | 4.08 ★ | 16.52 | 60.0% | **40.0%** | PKR 485.00 |
| `DRV-006` | 10 | 8 | 2 | PKR 3,504.00 | 3.91 ★ | 14.04 | 80.0% | 20.0% | PKR 438.00 |
| `DRV-007` | 10 | 7 | 3 | PKR 2,421.00 | **4.77 ★** | 11.52 | 70.0% | 30.0% | PKR 345.86 |
| `DRV-008` | 10 | 8 | 2 | PKR 3,210.00 | 4.20 ★ | 12.34 | 80.0% | 20.0% | PKR 401.25 |
| `DRV-009` | 10 | 9 | 1 | PKR 3,831.00 | 4.30 ★ | 12.70 | 90.0% | 10.0% | PKR 425.67 |
| `DRV-010` | 10 | 10 | 0 | PKR 4,055.00 | 4.34 ★ | 12.54 | 100.0% | 0.0% | PKR 405.50 |

---

## 10. Multi-Criteria Driver Performance Ranking

### Methodology:
Ranking drivers on revenue alone ignores service quality and cancellation churn. We employ a composite balanced scorecard:
$$\text{Composite Score} = 100 \times \left[ 0.35 \times \frac{\text{Revenue}}{\text{Max Revenue}} + 0.25 \times \frac{\text{Completed Rides}}{\text{Max Completed}} + 0.25 \times \frac{\text{Rating}}{5.0} + 0.15 \times \frac{\text{Completion Rate}}{100} \right]$$

### Official Driver League Table:
| Rank | Driver ID | Revenue (PKR) | Completed | Rating | Completion % | Cancellation % | Composite Score | Assessment |
|---|---|---|---|---|---|---|---|---|
| 🥇 **1** | `DRV-010` | PKR 4,055.00 | 10 | 4.34 ★ | 100.0% | 0.0% | **93.35** | **Elite Partner**: Zero churn, high revenue & high rating |
| 🥈 **2** | `DRV-001` | PKR 4,237.00 | 10 | 4.01 ★ | 100.0% | 0.0% | **93.12** | **Top Earner**: Perfect 100% completion & heavy volume |
| 🥉 **3** | `DRV-004` | PKR 4,007.00 | 10 | 4.36 ★ | 100.0% | 0.0% | **93.08** | **High Reliability**: Flawless completion & solid rating |
| **4** | `DRV-002` | **PKR 4,484.00** | 9 | 4.33 ★ | 90.0% | 10.0% | **92.67** | Highest gross revenue earner in fleet |
| **5** | `DRV-009` | PKR 3,831.00 | 9 | 4.30 ★ | 90.0% | 10.0% | **87.40** | Strong consistent performer |
| **6** | `DRV-003` | PKR 3,807.00 | 8 | 4.46 ★ | 80.0% | 20.0% | **84.03** | Excellent ratings, moderate cancellation risk |
| **7** | `DRV-006` | PKR 3,504.00 | 8 | 3.91 ★ | 80.0% | 20.0% | **78.91** | Rating needs customer service coaching (< 4.0) |
| **8** | `DRV-008` | PKR 3,210.00 | 8 | 4.20 ★ | 80.0% | 20.0% | **78.06** | Below-average ticket yield |
| **9** | `DRV-007` | PKR 2,421.00 | 7 | **4.77 ★** | 70.0% | 30.0% | **70.75** | Highest rating in fleet, but high 30% cancellation |
| **10** | `DRV-005` | PKR 2,910.00 | 6 | 4.08 ★ | 60.0% | **40.0%** | **67.13** | **Critical Churn Risk**: 4 cancellations out of 10 |

---

## 11. Visualizations Catalog

All 10 required high-resolution visual charts are rendered and cataloged:

| Chart # | File Name | Target Metric & Analysis |
|---|---|---|
| **Chart 1** | `01_revenue_by_month.png` | Daily and aggregate revenue trend across September 2026 |
| **Chart 2** | `02_revenue_by_location.png` | Horizontal bar comparison of revenue across pickup hubs |
| **Chart 3** | `03_revenue_by_payment_method.png` | Revenue breakdown across Cash, Card, UPI, and Wallet |
| **Chart 4** | `04_revenue_by_ride_type.png` | Revenue volume comparison across Economy, Standard, and Premium |
| **Chart 5** | `05_average_fare_by_ride_type.png` | Average ticket size yield across ride tiers |
| **Chart 6** | `06_top_drivers_by_revenue.png` | Driver ranking by realized revenue |
| **Chart 7** | `07_top_drivers_by_completed_rides.png` | Driver ranking by completed trips volume |
| **Chart 8** | `08_driver_rating_comparison.png` | Star rating comparison across all 10 fleet drivers |
| **Chart 9** | `09_driver_completion_rate.png` | Completion percentage bar chart |
| **Chart 10** | `10_driver_cancellation_rate.png` | Driver cancellation churn risk comparison |

---

## 12. Answers to Core Business Questions

1. **What is the total revenue?**  
   **PKR 36,466.00** recognized from 85 completed rides (out of PKR 42,962.00 gross booking value).
2. **Which month generated the highest revenue?**  
   **September 2026**, with peak revenue day occurring on **September 05, 2026 (PKR 5,411.00)**.
3. **Which location generates the most revenue?**  
   **DHA**, generating **PKR 15,388.00 (42.20% of total company revenue)**.
4. **Which payment method contributes the most revenue?**  
   **Cash**, contributing **PKR 14,115.00 (38.71%)**, followed by Card (29.62%).
5. **Which ride type generates the most revenue?**  
   **Standard Tier** generates the most total revenue (**PKR 14,136.00 / 38.76%**), while **Premium Tier** delivers the highest average ticket size (**PKR 558.05**).
6. **What is the average fare?**  
   **PKR 429.01** per completed trip.
7. **Which drivers generate the most revenue?**  
   **DRV-002 (PKR 4,484.00)**, followed by **DRV-001 (PKR 4,237.00)** and **DRV-010 (PKR 4,055.00)**.
8. **Which drivers complete the most rides?**  
   **DRV-001, DRV-004, and DRV-010** (Tied at **10 completed rides each**, 100% completion rate).
9. **Which drivers have the highest ratings?**  
   **DRV-007 (4.77 ★)**, followed by **DRV-003 (4.46 ★)** and **DRV-004 (4.36 ★)**.
10. **Which drivers have high cancellation rates?**  
    **DRV-005 (40.0% cancellation)** and **DRV-007 (30.0% cancellation)**.
11. **Do high-revenue drivers also have strong completion rates?**  
    **Yes.** Top-revenue driver `DRV-002` completed 90% of rides, and second-highest driver `DRV-001` completed 100% of rides.
12. **Are there locations with high demand but relatively low revenue?**  
    **Yes. Gulberg** generated **20.0% of total bookings (20 rides)** but contributed only **15.24% of revenue**, due to a lower average fare of **PKR 397.07** and an elevated cancellation rate (30%).

---

## 13. Key Findings (Finding → Evidence → Business Meaning)

### Key Finding 1: Geographic Revenue Concentration
* **Finding:** DHA is the core revenue engine of the business.
* **Evidence:** DHA accounts for **PKR 15,388.00 (42.20% of total revenue)** from 35 completed rides, with a high average fare of **₨439.66**.
* **Business Meaning:** Business performance is heavily reliant on DHA. The fleet must guarantee driver availability and avoid dispatch bottlenecks in this zone.

### Key Finding 2: High Demand with Low Margin in Gulberg
* **Finding:** Gulberg exhibits strong passenger demand but poor revenue realization.
* **Evidence:** Gulberg represents **20.0% of total bookings** but only **15.24% of recognized revenue**, suffering from a 30% cancellation rate and the lowest average fare in the fleet (**₨397.07**).
* **Business Meaning:** Trips in Gulberg are shorter and cancelled more frequently. Pricing models or driver dispatch incentives need calibration to improve route profitability.

### Key Finding 3: Cash Dependency vs Digital Settlement
* **Finding:** Cash remains the dominant single payment channel, yet digital channels represent the majority.
* **Evidence:** Cash accounts for **38.71% of revenue (PKR 14,115.00)**, while digital methods (Card 29.62%, UPI 22.43%, Wallet 9.24%) collectively drive **61.29%**.
* **Business Meaning:** Cash handling poses security and float reconciliation overhead for drivers. Expanding UPI and mobile wallet adoption through micro-promotions will streamline cashflow.

### Key Finding 4: Premium Tier Margin Expansion
* **Finding:** Premium rides generate disproportionately high yield relative to volume.
* **Evidence:** Premium represents only **25.9% of completed trips** but captures **33.67% of total revenue** with an average ticket of **₨558.05** (72% higher than Economy at ₨324.29).
* **Business Meaning:** Premium tier customers are less price-sensitive. Upselling corporate and airport travelers to Premium can drive margin expansion without increasing vehicle volume.

### Key Finding 5: Driver Churn Concentration
* **Finding:** Fleet cancellations are heavily concentrated among specific drivers.
* **Evidence:** Two drivers (`DRV-005` at 40% and `DRV-007` at 30%) account for **7 out of 15 total fleet cancellations (46.7% of all churn)**, leaking an estimated **PKR 3,050.00** in lost revenue.
* **Business Meaning:** Cancellations are not random; they stem from driver-specific behavior (selective destination acceptance or long pickup delays). Targeted operational intervention will quickly reduce revenue leakage.

---

## 14. Actionable Business Recommendations

1. **Implement Balanced Driver Incentive Programs:**
   * *Action:* Replace simple volume bonuses with a **Composite Quality Score** (rewarding drivers with $\ge$ 90% completion and $\ge$ 4.3 ★ rating, such as `DRV-010`, `DRV-001`, and `DRV-004`).
   * *Target:* Retain elite partners and incentivize driver reliability over reckless cherry-picking.

2. **Targeted Operational Churn Intervention:**
   * *Action:* Conduct dispatch reviews and enforce cancellation thresholds for drivers exceeding 25% churn (specifically `DRV-005` and `DRV-007`).
   * *Target:* Recover up to **PKR 3,000.00 to 5,000.00** in leaked monthly gross bookings per fleet unit.

3. **Geographic Supply Re-Balancing & Route Structuring:**
   * *Action:* Pre-dispatch 40% of fleet vehicles to DHA during morning and evening rush hours. For Gulberg, introduce a minimum trip fare or driver pickup allowance to reduce short-trip cancellation rates.
   * *Target:* Expand fleet utilization efficiency and improve Gulberg ride fulfillment from 70% to 85%.

---

## 15. Analytical Limitations

1. **Temporal Sample Size:** Dataset captures 100 transactions over a 10-day period in September 2026; seasonal variations (festive holidays, monsoons) cannot be modeled without longer historical series.
2. **Cost & Net Margin Telemetry:** Fuel consumption, driver vehicle maintenance, platform commissions, and customer acquisition costs are unavailable; analysis is restricted to gross realized fare revenue.
3. **Driver Shift Hours:** Operating hours and idle waiting times were unrecorded, precluding revenue-per-active-hour efficiency calculations.

---

## 16. Conclusion

Week 3 successfully expanded our analysis from passenger demand into **revenue intelligence and driver operational productivity**. The business possesses a strong core market in **DHA (42% revenue)**, high-yield expansion potential in **Premium tiers (₨558 avg fare)**, and dependable fleet partners (**DRV-010, DRV-001, DRV-004** with 100% fulfillment). Implementing balanced driver incentives and capping high-cancellation driver behavior will protect top-line revenue as the platform scales into Week 4 Business Intelligence dashboard development.
