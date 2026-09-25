# 🚀 Zyroo Data Analyst Internship Portfolio

Welcome to my official portfolio repository for the **Zyroo Data Analyst Internship**. This repository serves as a centralized hub documenting weekly technical deliverables, automated data pipelines, exploratory data analyses, production SQL pipelines, executive Business Intelligence dashboards, and multi-criteria operational rankings.

---

## 📋 Table of Contents
* [Week 4 — Power BI Dashboard Development](#-week-4--power-bi-dashboard-development)
* [Week 3 — Revenue & Driver Performance Analysis (Python, SQL & BI)](#-week-3--revenue--driver-performance-analysis)
* [Week 2 — Ride Analytics & Revenue Intelligence Platform (Power BI)](#-week-2--ride-analytics--revenue-intelligence-platform)
* [Week 1 — Onboarding & Environment Setup](#-week-1--onboarding--environment-setup)
* [Repository Structure](#-repository-structure)
* [Technical Environment](#-technical-environment)

---

## 📊 Week 4 — Power BI Dashboard Development

**Project Title**: Ride Analytics & Revenue Intelligence Platform  
**Sub-Topic**: Week 4 — Power BI Dashboard Development  
**Program**: ZYROO Data Analytics Internship • Week 4  
**Level**: Professional Data Analyst & Power BI Developer  
**Deliverables**: Cleaned Production Dataset, Power BI DAX Measures Dictionary (`powerbi/ride-analytics-dashboard/dax_measures_week4.dax`), Interactive Power BI Dashboard (`powerbi/ride-analytics-dashboard/index.html`), 10 High-Resolution Analytical Charts (`screenshots/week-04/`), and Comprehensive Executive Report (`reports/week-04-powerbi-dashboard/week_04_powerbi_report.md`).

[![Interactive Power BI Dashboard](https://img.shields.io/badge/Power%20BI-Interactive%20Dashboard-yellow?logo=powerbi&logoColor=black)](powerbi/ride-analytics-dashboard/index.html)
[![DAX Measures Catalog](https://img.shields.io/badge/DAX-Measures%20Catalog-blue?logo=microsoft&logoColor=white)](powerbi/ride-analytics-dashboard/dax_measures_week4.dax)
[![Week 4 Executive Report](https://img.shields.io/badge/Report-Executive%20BI%20Audit-success?logo=markdown&logoColor=white)](reports/week-04-powerbi-dashboard/week_04_powerbi_report.md)

---

### 🎯 Dashboard Purpose & Business Capabilities
The Week 4 Power BI Dashboard converts the multi-dimensional analytical findings from Week 2 (Demand & Passenger behavior) and Week 3 (Revenue intelligence & Driver productivity) into an executive-grade operational command center.

1. **Executive KPI Section**: Real-time evaluation of Total Demand (100 rides), Completed Trips (85), Operational Churn (15 cancellations), Realized Inflow (PKR 36,466.00), Average Ticket Size (PKR 429.01), Fulfillment Efficiency (85.0%), and Customer Satisfaction (4.27 ★).
2. **Ride Demand Dynamics**: Analyzes booking volume trends over time (Sep 01 - 10) and weekday distributions, pinpointing peak operational days (Thursday & Tuesday).
3. **Geographic Origin-Destination Matrix**: Evaluates top passenger origin hubs (DHA commanding 38% volume) versus cross-city drop-off flows.
4. **Financial Settlement & Vehicle Tier Intelligence**: Quantifies cash dependency (38.7%) versus the digital payment ecosystem (61.3%), alongside Premium tier yield superiority (PKR 558.05 avg fare).
5. **Driver League Table**: Multi-metric evaluation of all 10 fleet operators across completed rides, revenue, passenger ratings, and completion percentages.
6. **Six Interactive Executive Slicers**: Multi-dimensional filtering across Date, Ride Status, Pickup Location, Vehicle Tier, Payment Method, and Driver ID.

---

### 📊 Implemented Power BI KPI Metrics

| KPI Metric Card | Verified Value | Benchmark / Target | Operational Interpretation |
| :--- | :--- | :--- | :--- |
| **Total Rides** | **100 rides** | Baseline demand | Gross platform bookings dispatched over 10-day period |
| **Completed Rides** | **85 rides** | $\ge 85\%$ | Successful billable fulfillment count |
| **Cancelled Rides** | **15 rides** | $\le 10\%$ | Operational churn count |
| **Total Revenue** | **PKR 36,466.00** | Net recognized inflow | Net realized cash & digital revenue from completed journeys |
| **Average Fare** | **PKR 429.01** | PKR 400.00 | Average transaction ticket size per fulfilled trip |
| **Completion Rate** | **85.0%** | $\ge 85\%$ | Platform fulfillment efficiency |
| **Average Rating** | **4.27 ★** | $\ge 4.20 \text{ ★}$ | Weighted customer review rating on completed journeys |
| **Average Distance** | **13.8 km** | $12.0 - 15.0 \text{ km}$| Mean completed route length |

---

### 📈 Dashboard Visuals & Evidence Gallery
All 10 charts are rendered at high resolution (300 DPI) inside `screenshots/week-04/` and `reports/week-04-powerbi-dashboard/charts/`:

| Chart # | Visual Type | Title & Business Focus |
| :---: | :--- | :--- |
| **01** | Line Chart | **Rides by Date**: Ride Demand & Fulfillment Trends Over Time (Peak: Sep 05) |
| **02** | Bar Chart | **Rides by Weekday**: Fleet Demand Comparison (Thursday 24, Tuesday 20) |
| **03** | Horizontal Bar | **Top Pickup Locations**: Passenger Origin Volume Share (DHA 38.0%) |
| **04** | Horizontal Bar | **Top Drop-off Locations**: Passenger Destination Distribution |
| **05** | Horizontal Bar | **Revenue by Location**: Realized Earnings by Pickup Hub (DHA PKR 15.4k) |
| **06** | Donut Chart | **Revenue by Payment Method**: Cash (38.7%) vs. Digital Channels (61.3%) |
| **07** | Dual-Axis Bar | **Revenue & Avg Fare by Ride Type**: Standard volume vs. Premium ticket yield |
| **08** | Table / Matrix | **Driver Performance Table**: Sortable Multi-Metric Operational League Table |
| **09** | Column Chart | **Customer Ride Frequency**: Daily booking velocity and habituation proxy |
| **10** | Architecture Card | **Technical Schema Audit**: Schema verification and telemetry documentation |

---

### 💡 Top 5 Data-Driven Business Insights
1. **The DHA Revenue Engine**: DHA drives **38.0% of total bookings** and **42.2% of total platform revenue (PKR 15,388.00)** with a low 7.9% cancellation rate, serving as the business's core financial engine.
2. **The "Revenue Mirage" vs. Fleet Dependability**: While `DRV-002` achieved top raw revenue (PKR 4,484.00), they incurred cancellations. `DRV-001`, `DRV-004`, and `DRV-010` delivered **100% fulfillment** with zero cancellations while each earning over PKR 4,000.00.
3. **Severe Operational Friction in Gulberg**: Gulberg represents the second largest origin hub (20 requests) but suffers an alarming **30.0% cancellation rate** and lowest average fare (PKR 397.07), leading to PKR 2,367.00 in leaked gross bookings.
4. **Premium Tier Profit Density**: Premium rides command an average fare of **PKR 558.05** (+30.3% over Standard) across similar travel distances (13.5 km vs 12.5 km), proving high passenger willingness-to-pay.
5. **Concentrated Cancellation Leakage**: Two drivers (`DRV-005` with 40% churn and `DRV-007` with 30% churn) caused **46.7% of all platform cancellations**, confirming that service friction is localized to specific drivers.

---

### 🚀 Top 3 Practical Business Recommendations
1. **Geofenced Surge / Fulfillment Bonus for Gulberg**: Deploy an automated **PKR 50 - PKR 75 incentive** for drivers accepting dispatches in Gulberg during peak afternoon windows to drop churn below 12%.
2. **Multi-Factor Driver Priority Allocation**: Reserve high-ticket Premium dispatches for drivers maintaining $\ge 90\%$ completion and $\ge 4.3 \text{ ★}$ ratings (`DRV-001`, `DRV-004`, `DRV-010`).
3. **5% Instant Digital Settlement Discount**: Partner with digital payment providers to offer 5% instant cashback on Card, UPI, and Wallet payments to drive cash dependency below 20%.

---

## 🏆 Week 3 — Revenue & Driver Performance Analysis

**Project Title**: Ride Analytics & Revenue Intelligence Platform  
**Sub-Topic**: Week 3 — Revenue & Driver Performance Analysis  
**Program**: ZYROO Data Analytics Internship • Week 3  
**Deliverables**: Cleaned 100-Row Production Dataset, Production SQL Script (`sql/week_03_revenue_driver_analysis.sql`), Executed Python Engine & Jupyter Notebook (`week-03/week_03_revenue_driver_analysis.ipynb`), 10 High-Resolution Analytical Charts, and Comprehensive 16-Section Executive Markdown Report (`reports/week-03/week_03_revenue_driver_analysis_report.md`).

---

## 🚕 Week 2 — Ride Analytics & Revenue Intelligence Platform

**Project Title**: Ride Analytics & Revenue Intelligence Platform  
**Program**: ZYROO Data Analytics Internship • Week 2  
**Deliverables**: Cleaned Dataset, Data Pipeline Script, DAX Measure Catalog, Interactive Dashboard, and Power BI Report Specification

---

## 🛠️ Week 1 — Onboarding & Environment Setup

The objective of **Task 01** was establishing an isolated analytics environment, verifying Python, SQL, Excel, and Power BI environments, benchmark testing on structured datasets, and publishing to GitHub.

---

## 📁 Repository Structure

```text
zyro-data-analyst-internship/
│
├── powerbi/                                # Week 4: Power BI Dashboard & Models
│   └── ride-analytics-dashboard/
│       ├── dax_measures_week4.dax          # Power BI DAX Measures Catalog
│       ├── index.html                      # Interactive Power BI Dashboard Emulator
│       └── tailwindcss.min.js              # Offline-bundled stylesheet engine
│
├── reports/                                # Centralized executive reporting
│   ├── week-04-powerbi-dashboard/
│   │   ├── week_04_powerbi_report.md       # Comprehensive 11-section executive report
│   │   └── charts/                         # 10 High-resolution analytical charts (PNG)
│   └── week-03/
│       ├── week_03_revenue_driver_analysis_report.md
│       ├── driver_performance_ranking.csv
│       ├── location_revenue_analysis.csv
│       └── charts/
│
├── screenshots/                            # Visual evidence for internship evaluations
│   ├── week-04/ (10 PNGs - Power BI Visual Evidence)
│   ├── week-03/ (10 PNGs - Driver & Revenue Analysis)
│   └── week-01/ (7 PNGs - Tooling & Environment Verification)
│
├── data/                                   # Cleaned & standardized production datasets
│   ├── rides_data_week3.csv                # Primary 100-row production telemetry
│   └── rides_data_cleaned.csv
│
├── sql/                                    # Centralized SQL pipelines
│   └── week_03_revenue_driver_analysis.sql
│
├── python/                                 # Automated data engines & scripts
│   ├── generate_week4_charts.py            # High-resolution chart generator
│   ├── build_pbi_html.py                   # Power BI dashboard compiler
│   └── week-03-revenue-driver-analysis/
│
├── week-04/                                # Week 4 Quick-Launch Directory
│   ├── index.html                          # Standalone offline dashboard
│   └── tailwindcss.min.js
│
├── week-03/                                # Week 3 Deliverables
├── week-02/                                # Week 2 Deliverables
├── week-01/                                # Week 1 Deliverables
│
├── index.html                              # Root interactive web dashboard (offline-ready)
├── README.md                               # Master portfolio documentation
├── requirements.txt                        # Pinned dependencies
└── .gitignore                              # Git exclusion rules
```

---

## 💻 Technical Environment
* **Platform**: Windows 11 / PowerShell 5.1 / Python 3.13.15
* **Analytics Stack**: Pandas, NumPy, Matplotlib, Seaborn, OpenPyXL, SQLite3, nbclient, nbformat
* **Business Intelligence**: Power BI Desktop, Microsoft Excel 2016/365, Google Looker Studio
* **Version Control**: Git 2.55 & GitHub CLI
