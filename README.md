# 🚀 ZYROO DATA ANALYTICS INTERNSHIP — FINAL CAPSTONE
# Ride Analytics & Revenue Intelligence Platform
### An Enterprise Business Intelligence, Operations Optimization & Decision Analytics System

[![Live Dashboard Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-success?style=for-the-badge&logo=github)](https://evilswordboy-bot.github.io/zyro-data-analyst-internship/)
[![Interactive Presentation](https://img.shields.io/badge/Presentation-15%20Slide%20Deck-cyan?style=for-the-badge&logo=slides)](presentation/index.html)
[![Offline Zip Package](https://img.shields.io/badge/Download-Chrome%20Offline%20ZIP-orange?style=for-the-badge&logo=zip)](zyroo_ride_analytics_live_demo.zip)
[![Quality Gate](https://img.shields.io/badge/Quality%20Audit-100%25%20Verified-blue?style=for-the-badge&logo=checkmarx)](python/validate_all_kpis.py)

---

## 📌 Executive Summary & Project Mandate

The **Ride Analytics & Revenue Intelligence Platform** is the capstone Business Intelligence product developed for the **ZYROO Data Analytics Internship**. 

Designed for **C-suite executives, VP Operations, and Fleet Directors**, the platform transforms 100 urban mobility transactions across 5 metropolitan sectors (DHA, Gulberg, Bahria Town, Johar Town, Model Town) over a 10-day period (September 1–10, 2026) into defensible operational interventions, driver performance benchmarks, and top-line revenue recovery.

```
Raw Telemetry ➔ Data Cleaning ➔ Star Schema ➔ Multi-Engine Triangulation ➔ Executive BI ➔ What-If Simulation ➔ ROI Roadmap
```

---

## 🎯 Primary Business Findings (100% Empirically Validated)

| Core Metric | Baseline Value | Operational Meaning |
| :--- | :---: | :--- |
| **Gross Booked Value** | **$42,962.00** | Total commercial booking demand generated (100 ride requests) |
| **Net Realized Cash** | **$36,466.00** | Net recognized platform revenue from 85 completed trips |
| **Operational Leakage**| **$6,496.00** | Unrealized gross fare lost to 15 pre-trip cancellations (15.1% leakage) |
| **Completion Rate** | **85.0%** | Baseline platform fulfillment efficiency (85 of 100 fulfilled) |
| **Cancellation Rate** | **15.0%** | Operational booking failure rate (15 of 100 cancelled) |
| **Average Realized Fare** | **$429.01** | Mean ticket yield per completed trip ($429.62 overall) |
| **Average Trip Distance** | **13.76 km** | Mean journey distance across all dispatched trips |
| **Fleet Customer Rating**| **4.27 ★** | Mean customer satisfaction rating on completed trips (1.0–5.0 scale) |
| **Active Fleet Drivers** | **10 Drivers** | 10 assigned drivers (`DRV-001` through `DRV-010`, 10 rides each) |

---

## 🔍 The 4 Key Operational Breakthroughs

1. **Driver Risk Asymmetry (The 20/50 Rule):**
   * Exactly 2 drivers (`DRV-005` with 40% cancellations and `DRV-007` with 30% cancellations) account for **46.7% of all platform cancellations** (7 of 15) and **$3,410.00 in lost revenue** (52.5% of total platform leakage).
   * Interestingly, `DRV-007` maintains the highest customer rating in the fleet (**4.77 ★**), indicating vehicle maintenance or dispatch radius issues rather than customer demeanor.
2. **The Weekend Operational Cliff:**
   * Weekend cancellation rate spikes to **23.81%** (almost double the weekday rate of 12.66%). On Sunday, Sept 6, cancellations hit **42.86%** (nearly 1 in 2 rides failed).
3. **The Gulberg Hotspot Bottleneck:**
   * Gulberg suffers from a **30.0% cancellation rate** (6 cancellations out of 20 rides), losing **$2,443.00** in revenue. A passenger booking in Gulberg is **3.8 times more likely to experience a cancellation** than a passenger in DHA (7.89% cancellation rate).
4. **Payment Channel Friction:**
   * Digital payment methods (**UPI at 9.09%** and **Card at 10.71%**) experience dramatically lower cancellation rates than **Cash (17.95%)** and **Digital Wallet (27.27%)**.

---

## 🧮 What-If Business Scenario Simulations

Two mathematical simulations demonstrate the financial return of targeted operational interventions:

```
┌────────────────────────────────────────────────────────────────────────┐
│ BASELINE: 100 Rides | 85 Completed | $36,466 Net Rev | $6,496 Leakage │
└───────────────────┬────────────────────────────────┬───────────────────┘
                    │                                │
         SCENARIO A (Target 92% Comp)      SCENARIO B (50% Canc Reduction)
                    │                                │
         ▼                                  ▼
┌────────────────────────────────┐ ┌────────────────────────────────┐
│ +7 Completed Rides             │ │ -8 Cancelled Rides (15 -> 7)   │
│ +$3,003.08 Realized Revenue    │ │ +$3,464.53 Recaptured Revenue  │
│ New Net: $39,469.08 (+8.24%)   │ │ New Net: $39,930.53 (+9.50%)   │
│ Lost Rev: Drops to $3,492.92   │ │ Lost Rev: Drops to $3,031.47   │
└────────────────────────────────┘ └────────────────────────────────┘
```

* **Scenario A (Target 92% Completion Rate):** Re-allocating weekend driver shifts adds **+$3,003.08 in top-line revenue (+8.24%)**.
* **Scenario B (50% Cancellation Reduction):** Coaching `DRV-005` & `DRV-007` and staging vehicles in Gulberg recaptures **+$3,464.53 in top-line revenue (+9.50%)**.

---

## 🛠️ Multi-Engine Verification & Quality Gate

Every KPI was audited and triangulated with zero discrepancy across 3 independent analytical engines:
$$\text{Python (Pandas)} \equiv \text{PostgreSQL (SQL)} \equiv \text{Power BI (DAX)} \implies \Delta = 0.000\%$$

Run the automated test suite locally:
```powershell
python python/validate_all_kpis.py
```

### Data Quality Scorecard Summary:
* **Missing Values:** Exactly 15 nulls in `rating`, verified to correlate 100% with `Cancelled` status. Preserved as structural NULLs; passengers cannot rate cancelled trips.
* **Duplicates:** 0 duplicate rows; 0 duplicate primary keys (`ride_id`).
* **Boundary Validation:** Distance (3.10–25.80 km) and Fare ($120.00–$780.00) strictly adhere to physical constraints.

---

## 🚀 7 Strategic Recommendations & Implementation Roadmap

1. **Targeted Driver Coaching (`DRV-005` & `DRV-007`):** Re-align dispatch radii and navigation support to eliminate 46.7% of platform cancellations. *(Priority: HIGH)*
2. **Weekend Driver Fulfillment Incentive:** Deploy a 15% completion bonus during Friday–Sunday peak hours to curb the 23.8% cancellation cliff. *(Priority: HIGH)*
3. **Dedicated Gulberg Staging Hubs:** Pre-position vehicles near commercial centers in Gulberg to reduce the 30% cancellation rate. *(Priority: HIGH)*
4. **Digital Payment Migration Discount:** 5% instant discount on UPI and Card pre-authorizations to shift riders away from high-friction cash/wallet settlement. *(Priority: MEDIUM)*
5. **Standard Service Tier Recalibration:** Rebalance dispatch thresholds on 10–18 km journeys ($3,099 in lost bookings). *(Priority: MEDIUM)*
6. **Driver Service Floor Governance:** Institute customer service refresher coaching for drivers below 4.10 rating (e.g. `DRV-006` at 3.91). *(Priority: MEDIUM)*
7. **Telemetry Infrastructure Modernization:** Mandate unique `customer_id`, rider app timestamps, and cancellation reason codes in Phase 2 schema. *(Strategic Enabler)*

---

## 📂 Production Repository Structure

```text
zyro-data-analyst-internship/
├── data/
│   ├── rides_data_week3.csv          # Ground-truth production dataset (100 rows, 11 cols)
│   └── rides_data_cleaned.csv        # Pre-processed clean dataset
├── sql/
│   ├── final_capstone_analytics.sql  # Production SQL analytics & star schema layer
│   ├── week_05_decision_analytics.sql# Week 5 decision intelligence queries
│   └── week_03_revenue_driver_analysis.sql
├── python/
│   ├── validate_all_kpis.py          # Automated multi-engine KPI triangulation script
│   ├── build_week5_html.py           # Multi-page dashboard compiler
│   ├── generate_week5_charts.py      # High-resolution chart generator
│   └── build_pbi_html.py             # Week 4 dashboard builder
├── powerbi/
│   ├── week-05-advanced-analytics/   # Advanced Decision Intelligence Dashboard
│   ├── week-04-dashboard/            # Preserved Week 4 Power BI Production Dashboard
│   └── ride-analytics-dashboard/     # Initial Power BI wireframes
├── reports/
│   ├── final-capstone/
│   │   └── final_masterpiece_business_intelligence_report.md # 21-section Master Capstone Report
│   ├── week-05-advanced-bi/          # Week 5 executive decision report
│   ├── week-04-powerbi-dashboard/    # Week 4 dashboard design report
│   ├── week-03/                      # Week 3 revenue & driver report
│   └── week-02/                      # Week 2 demand & customer report
├── presentation/
│   ├── index.html                    # 15-Slide interactive HTML5 presentation deck (Chrome ready)
│   └── final_executive_presentation.md # Master 15-slide presentation speaker deck
├── screenshots/
│   ├── week-05/                      # 8 high-res decision analytics charts
│   ├── week-04/                      # Week 4 dashboard visual captures
│   └── week-03/                      # Week 3 exploratory charts
├── app.py                            # Streamlit BI application
├── index.html                        # Production root live decision dashboard
├── start_dashboard_offline.bat       # 1-click offline launcher (Google Chrome)
├── start_streamlit.bat               # 1-click Streamlit launcher
├── tailwindcss.min.js                # Bundled local offline styling engine
├── requirements.txt                  # Python runtime dependencies
├── zyroo_ride_analytics_live_demo.zip# Standalone offline Chrome-ready ZIP package
└── README.md                         # Portfolio documentation hub
```

---

## 💻 How to Run Locally

### Option 1: Double-Click (100% Offline in Google Chrome)
1. Extract `zyroo_ride_analytics_live_demo.zip`.
2. Double-click `start_dashboard_offline.bat` (or open `index.html` directly in Chrome).
3. To view the presentation deck, double-click `presentation/index.html`.

### Option 2: Live Cloud Deployment
* Open the live web app: [GitHub Pages Live Demo](https://evilswordboy-bot.github.io/zyro-data-analyst-internship/)

### Option 3: Streamlit Application
```powershell
pip install -r requirements.txt
streamlit run app.py
```

---

## 🏆 Portfolio Summary & Author

* **Author:** Senior Business Intelligence Consultant & Lead Data Analyst
* **Internship:** ZYROO Data Analytics Internship — Final Capstone
* **Core Competencies:** Business Intelligence, Power BI, Advanced DAX, PostgreSQL, Python/Pandas, Dimensional Modeling, Operations Research, What-If Modeling.
