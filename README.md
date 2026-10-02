# 🚀 Zyroo Data Analyst Internship Portfolio

Welcome to my official portfolio repository for the **Zyroo Data Analyst Internship**. This repository serves as a centralized hub documenting weekly technical deliverables, automated data pipelines, exploratory data analyses, production SQL pipelines, executive Business Intelligence dashboards, multi-criteria operational rankings, customer behavioral segmentation, and What-If financial simulations.

---

## 📋 Table of Contents
* [Week 5 — Advanced Business Intelligence & Decision Analytics](#-week-5--advanced-business-intelligence--decision-analytics)
* [Week 4 — Power BI Dashboard Development](#-week-4--power-bi-dashboard-development)
* [Week 3 — Revenue & Driver Performance Analysis (Python, SQL & BI)](#-week-3--revenue--driver-performance-analysis)
* [Week 2 — Ride Analytics & Revenue Intelligence Platform (Power BI)](#-week-2--ride-analytics--revenue-intelligence-platform)
* [Week 1 — Onboarding & Environment Setup](#-week-1--onboarding--environment-setup)
* [Repository Structure](#-repository-structure)
* [Technical Environment](#-technical-environment)

---

## 🔮 Week 5 — Advanced Business Intelligence & Decision Analytics

**Project Title**: Ride Analytics & Revenue Intelligence Platform  
**Sub-Topic**: Week 5 — Advanced Business Intelligence & Decision Analytics  
**Program**: ZYROO Data Analytics Internship • Week 5  
**Level**: Senior Data Analyst, BI Specialist & Decision Modeler  
**Deliverables**: Cleaned Production Dataset, Advanced DAX Measures Dictionary (`powerbi/week-05-advanced-analytics/dax_measures_week5.dax`), SQL Validation Pipeline (`sql/week_05_decision_analytics.sql`), Interactive Multi-Page Decision Dashboard (`powerbi/week-05-advanced-analytics/index.html`), 8 High-Resolution Analytical Charts (`screenshots/week-05/`), and Comprehensive Executive Report (`reports/week-05-advanced-bi/week_05_decision_analytics_report.md`).

[![Live Decision Dashboard](https://img.shields.io/badge/Power%20BI-Multi--Page%20Decision%20System-yellow?logo=powerbi&logoColor=black)](powerbi/week-05-advanced-analytics/index.html)
[![Advanced DAX Catalog](https://img.shields.io/badge/DAX-20%2B%20Measures-blue?logo=microsoft&logoColor=white)](powerbi/week-05-advanced-analytics/dax_measures_week5.dax)
[![SQL Validation Pipeline](https://img.shields.io/badge/SQL-Decision%20Audit-00758F?logo=sqlite&logoColor=white)](sql/week_05_decision_analytics.sql)
[![Executive BI Report](https://img.shields.io/badge/Report-Executive%20BI%20Audit-success?logo=markdown&logoColor=white)](reports/week-05-advanced-bi/week_05_decision_analytics_report.md)

---

### 🎯 Business Intelligence & Analytical Framework
Week 5 upgrades the descriptive dashboard into an evidence-based **Decision Analytics & Management Decision Support System**:
$$\textbf{WHAT happened} \longrightarrow \textbf{WHY the pattern matters} \longrightarrow \textbf{WHAT should be investigated next}$$

1. **Advanced Star-Schema Model**: Separates `Fact_Rides` (100 rows) with a dedicated `Dim_Date` dimension table, isolating source data, calculated dimensions, and DAX aggregation layers.
2. **Behavioral Customer Segmentation**: Formulates 3 distinct passenger profiles (Standard Daily Commuters, Premium Executive Riders, and Economy Short-Hop Riders) to model price elasticity and journey purpose.
3. **Driver Benchmark Variance**: Compares all 10 fleet operators against cohort baseline benchmarks (Revenue: PKR 3,646.60 | Completion: 85.0% | Rating: 4.27 ★), uncovering cherry-picking behaviors vs true dependability.
4. **Cancellation Analytics & Causal Rigor**: Identifies geographic churn concentration in Gulberg (30.0% cancellation rate), strictly differentiating correlation from causation.
5. **What-If Financial Simulation Engine**: Models dynamic scenarios evaluating volume expansion (+10% rides $\rightarrow$ +PKR 3,646.60), pricing shifts (+5% fare $\rightarrow$ +PKR 1,823.30), and churn recovery (50% recovered $\rightarrow$ +PKR 3,248.00).

---

### 📊 Verified Executive Baseline KPIs (100% Validated)

| KPI Metric Card | Verified Baseline Value | SQL / DAX Status | Business Meaning |
| :--- | :--- | :---: | :--- |
| **Total Demand** | **100 rides** | 100% Match | Gross ride requests dispatched over the 10-day period |
| **Fulfilled Rides** | **85 rides** | 100% Match | Successful completed journeys delivered |
| **Operational Churn** | **15 rides** | 100% Match | Dispatched rides aborted or unfulfilled |
| **Realized Revenue** | **PKR 36,466.00** | 100% Match | Net recognized cash & digital revenue from completed journeys |
| **Gross Booking Value** | **PKR 42,962.00** | 100% Match | Total commercial booking demand placed on platform |
| **Lost to Cancellations**| **PKR 6,496.00** | 100% Match | Unrealized gross commercial bookings from 15 cancelled rides |
| **Average Ticket Size** | **PKR 429.01** | 100% Match | Mean ticket size per completed trip |
| **Completion Rate** | **85.0%** | 100% Match | Platform fulfillment efficiency benchmark ($\ge 85\%$) |
| **Cancellation Rate** | **15.0%** | 100% Match | Operational churn percentage ($\le 10\%$ target) |
| **Customer CSAT** | **4.27 ★** | 100% Match | Weighted customer satisfaction rating on fulfilled trips |
| **Mean Route Distance**| **13.72 km** | 100% Match | Mean travel distance per completed trip |

---

### 👥 Customer Behavioral Segmentation Matrix

| Customer Segment | Total Rides | Completed | Churn % | Realized Revenue | Revenue Share | Avg Ticket Size | Avg Distance | Top Channel |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Standard Daily Commuters** | 39 | 32 | 17.9% | PKR 14,136.00 | **38.76%** | PKR 441.75 | 14.25 km | UPI / Cash |
| **Premium Executive Riders** | 26 | 22 | 15.4% | PKR 12,277.00 | **33.67%** | **PKR 558.05** | 19.50 km | Cash / Card |
| **Economy Short-Hop Riders** | 35 | 31 | 11.4% | PKR 10,053.00 | **27.57%** | PKR 324.29 | 9.09 km | Card / UPI |

---

### 🏎️ Driver Performance & Benchmark Variance League Table

| Rank | Driver ID | Completed | Cancelled | Realized Revenue | Rev vs Benchmark | Completion Rate | C-Rate vs Benchmark | Rating | Composite Score | Operational Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **DRV-010** | 10 | 0 | PKR 4,055.00 | +PKR 408.40 | **100.0%** | +15.0% | 4.34 ★ | **80.16** | 🌟 Star Partner (Zero Churn) |
| **2** | **DRV-004** | 10 | 0 | PKR 4,007.00 | +PKR 360.40 | **100.0%** | +15.0% | 4.36 ★ | **79.93** | 🌟 Star Partner (Zero Churn) |
| **3** | **DRV-002** | 9 | 1 | **PKR 4,484.00** | **+PKR 837.40** | 90.0% | +5.0% | 4.33 ★ | **77.25** | 🚀 Top Earner / Mild Churn |
| **4** | **DRV-001** | 10 | 0 | PKR 4,237.00 | +PKR 590.40 | **100.0%** | +15.0% | 4.01 ★ | **73.65** | 🌟 Star Partner (Zero Churn) |
| **5** | **DRV-009** | 9 | 1 | PKR 3,831.00 | +PKR 184.40 | 90.0% | +5.0% | 4.30 ★ | **65.20** | 🟢 Consistent Partner |
| **6** | **DRV-003** | 8 | 2 | PKR 3,807.00 | +PKR 160.40 | 80.0% | -5.0% | 4.46 ★ | **59.52** | 🟢 High Rating / Churn Alert |
| **7** | **DRV-008** | 8 | 2 | PKR 3,210.00 | -PKR 436.60 | 80.0% | -5.0% | 4.20 ★ | **41.75** | 🟡 Below Benchmark |
| **8** | **DRV-006** | 8 | 2 | PKR 3,504.00 | -PKR 142.60 | 80.0% | -5.0% | 3.91 ★ | **38.37** | 🟡 Low Rating Alert |
| **9** | **DRV-007** | 7 | 3 | PKR 2,421.00 | -PKR 1,225.60 | **70.0%** | -15.0% | **4.77 ★** | **35.00** | 🔴 High Quality Cherry-Picker |
| **10**| **DRV-005** | 6 | 4 | PKR 2,910.00 | -PKR 736.60 | **60.0%** | -25.0% | 4.08 ★ | **13.27** | ⛔ Severe Operational Risk |

---

### 🔮 What-If Financial Simulation Matrix

| Simulation Model | Key Assumption | Baseline Actual | Simulated Outcome | Revenue Delta (PKR) | Delta % |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Scenario A (+10% Volume)** | Fulfilled trips rise from 85 to 93.5 | PKR 36,466.00 | PKR 40,112.60 | **+PKR 3,646.60** | **+10.0%** |
| **Scenario B (+5% Price Yield)**| Average completed fare rises to PKR 450.46| PKR 36,466.00 | PKR 38,289.30 | **+PKR 1,823.30** | **+5.0%** |
| **Scenario C (50% Churn Recovery)**| Reclaim 7.5 cancelled rides (PKR 3,248) | PKR 36,466.00 | PKR 39,714.00 | **+PKR 3,248.00** | **+8.91%** |

---

### 📈 Week 5 Decision Visuals Gallery (300 DPI)
All 8 decision charts are rendered inside `screenshots/week-05/` and `reports/week-05-advanced-bi/charts/`:

* [x] **`01_location_demand_vs_cancellation.png`** — Location Demand vs Cancellation Matrix (Gulberg Churn Focus).
* [x] **`02_revenue_vs_avg_fare_by_tier.png`** — Revenue Contribution vs Average Fare by Vehicle Tier.
* [x] **`03_driver_revenue_vs_benchmark.png`** — Driver Performance Variance vs Cohort Revenue Benchmark.
* [x] **`04_what_if_scenario_modeling.png`** — What-If Financial Projections (Volume, Fare, Churn Recovery).
* [x] **`05_customer_behavioral_segments.png`** — Customer Behavioral Segmentation Revenue Share.
* [x] **`06_payment_ecosystem_contribution.png`** — Payment Ecosystem Breakdown (Digital 61.3% vs Cash 38.7%).
* [x] **`07_weekday_demand_and_churn_risk.png`** — Weekday Demand & Churn Volatility Analysis.
* [x] **`08_time_intelligence_revenue_runrate.png`** — 10-Day Revenue Run-Rate Trajectory.

---

### 💡 8 Evidence-Based Business Insights Summary
1. **DHA Geographic Revenue Dominance:** Generates 35 completed rides and **42.20% (PKR 15,388.00)** of total realized revenue with an above-average ticket size of PKR 439.66 and low 7.89% churn.
2. **Gulberg Operational Churn Anomaly:** Commanded 20 ride requests (20.0% of demand) but experienced a **30.0% cancellation rate (6 cancelled rides)** and the lowest completed average fare (PKR 397.07).
3. **Revenue Mirage vs Dependability:** DRV-002 achieved top gross revenue (PKR 4,484.00) but cancelled 10% of trips. DRV-010, 004, and 001 achieved **100% completion (0 cancellations)** while earning >PKR 4,000.00.
4. **Premium Tier Ticket Yield Density:** Premium rides average **PKR 558.05 per journey (+30.3% over Standard)** across comparable distances (19.5 km vs 14.2 km), contributing 33.67% of revenue from only 22 trips.
5. **Concentration of Platform Churn:** Two drivers (DRV-005 with 4 cancellations and DRV-007 with 3 cancellations) caused **46.7% of all platform churn (7 of 15 cancellations)**.
6. **Digital Payment Ecosystem:** Digital payment channels collectively account for **61.29% of revenue (PKR 22,351.00)** across Card (29.6%), UPI (22.4%), and Wallet (9.2%), while Cash accounts for 38.71%.
7. **Temporal Demand & Weekday Peaks:** **Thursday (24 bookings)** and **Tuesday (20 bookings)** drive 44.0% of total weekly volume. Friday experienced the highest weekday cancellation rate (25.0%).
8. **Cross-City Transit Equilibrium:** Drop-off destinations are uniformly distributed across Johar Town (22%), Gulberg (21%), Model Town (20%), Bahria Town (19%), and DHA (18%).

---

### 🚀 5 Actionable Business Recommendations Summary
1. **Geofenced Fulfillment Bonus for Gulberg:** Deploy a dynamic PKR 50 - PKR 75 pickup bonus for drivers accepting dispatches originating in Gulberg to drop churn below 12%.
2. **Star Partner Priority Dispatch Protocol:** Implement dispatch routing giving 100% completion drivers priority assignment to high-yield Premium trips.
3. **Strategic Expansion of Premium Tier Fleet:** Recruit and onboard vehicles meeting executive comfort standards to capitalize on high pricing tolerance.
4. **Targeted Driver Retraining & Churn Warnings:** Issue automated operational alerts and schedule mandatory route compliance retraining for DRV-005 and DRV-007.
5. **Digital Payment Cashback Acceleration:** Offer 5% instant cashback on Card, UPI, and Wallet settlements to compress cash share below 20%.

---

## 📊 Week 4 — Power BI Dashboard Development

**Project Title**: Ride Analytics & Revenue Intelligence Platform  
**Program**: ZYROO Data Analytics Internship • Week 4  
**Deliverables**: Cleaned Production Dataset, Power BI DAX Measures Dictionary, Interactive Power BI Dashboard (`powerbi/week-04-dashboard/index.html`), 10 High-Resolution Analytical Charts (`screenshots/week-04/`), and Comprehensive Executive Report (`reports/week-04-powerbi-dashboard/week_04_powerbi_report.md`).

---

## 🏆 Week 3 — Revenue & Driver Performance Analysis

**Project Title**: Ride Analytics & Revenue Intelligence Platform  
**Sub-Topic**: Week 3 — Revenue & Driver Performance Analysis  
**Deliverables**: Cleaned 100-Row Production Dataset, Production SQL Script (`sql/week_03_revenue_driver_analysis.sql`), Executed Python Engine & Jupyter Notebook, and 10 Analytical Charts.

---

## 🚕 Week 2 — Ride Analytics & Revenue Intelligence Platform

**Project Title**: Ride Analytics & Revenue Intelligence Platform  
**Deliverables**: Cleaned Dataset, Data Pipeline Script, DAX Measure Catalog, Interactive Dashboard, and Power BI Report Specification.

---

## 🛠️ Week 1 — Onboarding & Environment Setup

The objective of **Task 01** was establishing an isolated analytics environment, verifying Python, SQL, Excel, and Power BI environments, benchmark testing on structured datasets, and publishing to GitHub.

---

## 📁 Repository Structure

```text
zyro-data-analyst-internship/
│
├── powerbi/
│   ├── week-05-advanced-analytics/        # Week 5: Advanced Decision Support Platform
│   │   ├── dax_measures_week5.dax          # 20+ Advanced DAX & Scenario Measures
│   │   ├── index.html                      # Multi-Page Decision Dashboard
│   │   └── tailwindcss.min.js              # Offline-bundled stylesheet
│   └── week-04-dashboard/                  # Week 4: Preserved Executive Dashboard
│       ├── dax_measures_week4.dax
│       ├── index.html
│       └── tailwindcss.min.js
│
├── reports/
│   ├── week-05-advanced-bi/
│   │   ├── week_05_decision_analytics_report.md # Comprehensive 10-section BI report
│   │   └── charts/                         # 8 High-resolution decision charts (PNG)
│   ├── week-04-powerbi-dashboard/
│   │   └── week_04_powerbi_report.md
│   └── week-03/
│       └── week_03_revenue_driver_analysis_report.md
│
├── screenshots/
│   ├── week-05/ (8 PNGs - Decision Intelligence & Scenarios)
│   ├── week-04/ (10 PNGs - Power BI Visual Evidence)
│   ├── week-03/ (10 PNGs - Driver & Revenue Analysis)
│   └── week-01/ (7 PNGs - Tooling Verification)
│
├── data/
│   ├── rides_data_week3.csv                # Primary 100-row production telemetry
│   └── rides_data_cleaned.csv
│
├── sql/
│   ├── week_05_decision_analytics.sql      # Advanced ANSI SQL decision validation
│   └── week_03_revenue_driver_analysis.sql
│
├── python/
│   ├── generate_week5_charts.py            # Week 5 300 DPI chart engine
│   ├── build_week5_html.py                 # Multi-page dashboard compiler
│   └── build_pbi_html.py
│
├── app.py                                  # Local Streamlit BI application
├── index.html                              # Root interactive web dashboard (offline-ready)
├── README.md                               # Master portfolio documentation
├── requirements.txt                        # Pinned dependencies
└── vercel.json                             # 1-Click Vercel cloud deployment config
```

---

## 💻 Technical Environment
* **Platform**: Windows 11 / PowerShell 5.1 / Python 3.13.15
* **Analytics Stack**: Pandas, NumPy, Matplotlib, Seaborn, OpenPyXL, SQLite3, Streamlit, Plotly
* **Business Intelligence**: Power BI Desktop, Microsoft Excel 2016/365, Google Looker Studio
* **Version Control**: Git 2.55 & GitHub CLI
