# 🚀 Zyroo Data Analyst Internship Portfolio

Welcome to my official portfolio repository for the **Zyroo Data Analyst Internship**. This repository serves as a centralized hub documenting weekly technical deliverables, automated data pipelines, exploratory data analyses, production SQL pipelines, executive Business Intelligence dashboards, and multi-criteria operational rankings.

---

## 📋 Table of Contents
* [Week 3 — Revenue & Driver Performance Analysis (Python, SQL & BI)](#-week-3--revenue--driver-performance-analysis)
* [Week 2 — Ride Analytics & Revenue Intelligence Platform (Power BI)](#-week-2--ride-analytics--revenue-intelligence-platform)
* [Week 1 — Onboarding & Environment Setup](#-week-1--onboarding--environment-setup)
* [Repository Structure](#-repository-structure)
* [Technical Environment](#-technical-environment)

---

## 🏆 Week 3 — Revenue & Driver Performance Analysis

**Project Title**: Ride Analytics & Revenue Intelligence Platform  
**Sub-Topic**: Week 3 — Revenue & Driver Performance Analysis  
**Program**: ZYROO Data Analytics Internship • Week 3  
**Level**: Professional Data Analyst & Business Intelligence Specialist  
**Deliverables**: Cleaned 100-Row Production Dataset, Production SQL Script (`sql/week_03_revenue_driver_analysis.sql`), Executed Python Engine & Jupyter Notebook (`week-03/week_03_revenue_driver_analysis.ipynb`), 10 High-Resolution Analytical Charts, and Comprehensive 16-Section Executive Markdown Report (`reports/week-03/week_03_revenue_driver_analysis_report.md`).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/evilswordboy-bot/zyro-data-analyst-internship/blob/main/week-03/week_03_revenue_driver_analysis.ipynb)
[![SQL Script](https://img.shields.io/badge/SQL-Production%20Pipeline-blue?logo=postgresql&logoColor=white)](sql/week_03_revenue_driver_analysis.sql)
[![Executive Report](https://img.shields.io/badge/Report-Executive%20PDF%2FMD-success?logo=markdown&logoColor=white)](reports/week-03/week_03_revenue_driver_analysis_report.md)

---

### 🎯 Business Objective
Move from baseline passenger demand into **granular revenue intelligence and driver operational performance**:
1. How much revenue is generated, across which locations, payment methods, and ride tiers?
2. Which drivers drive real platform profitability vs. who incurs severe operational churn?
3. Design a **Multi-Criteria Composite Driver Score** to avoid misleading revenue-only rankings and reward service reliability.

---

### 📊 Core Revenue KPIs (Verified Exact Numbers)
Calculated from the standardized 100-ride production dataset (`rides_data_week3.csv`):

| Metric | Verified Value | Business Meaning |
| :--- | :--- | :--- |
| **Total Realized Revenue** | **PKR 36,466.00** | Net recognized revenue from 85 completed trips |
| **Gross Booking Value (GBV)**| **PKR 42,962.00** | Total value of all 100 booking requests |
| **Revenue Lost to Churn** | **PKR 6,496.00** | Unrealized revenue from 15 cancelled rides (15.1% leakage) |
| **Average Fare per Trip** | **PKR 429.01** | Average financial ticket size per fulfilled trip |
| **Average Revenue / Day** | **PKR 3,646.60** | Normalized daily run-rate across the 10-day audit period |
| **Peak Revenue Day** | **Sep 05, 2026 (PKR 5,411)** | Highest utilization day (12 completed trips) |
| **Lowest Revenue Day** | **Sep 07, 2026 (PKR 2,427)** | Trough day with only 6 completed trips |
| **Top Revenue Location** | **DHA (PKR 15,388.00)** | Generates **42.20%** of total platform earnings |
| **Top Payment Method** | **Cash (PKR 14,115.00)** | Represents **38.71%** of revenue (Digital = 61.29%) |
| **Top Ride Type** | **Standard (PKR 14,136.00)**| Generates **38.76%** of revenue; Premium has highest fare (PKR 558.05) |

---

### 🥇 Multi-Criteria Driver Performance League Table
To ensure driver evaluation is fair and actionable, drivers were evaluated across four weighted dimensions:
$$\text{Composite Score} = 0.35 \times S_{\text{rev}} + 0.25 \times S_{\text{comp}} + 0.25 \times S_{\text{rating}} + 0.15 \times S_{\text{rate}}$$

*Each metric is min-max normalized ($0-100$) before weighting.*

| Rank | Driver ID | Total Rides | Completed | Cancelled | Comp Rate | Canc Rate | Total Revenue (PKR) | Avg Rating | Avg Dist (km) | Composite Score | Tier Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **DRV-010** | 10 | 10 | 0 | **100.0%** | 0.0% | PKR 4,055.00 | 4.34 ★ | 12.80 | **93.35** | 🌟 Top Performer |
| **2** | **DRV-001** | 10 | 10 | 0 | **100.0%** | 0.0% | PKR 4,237.00 | 4.01 ★ | 13.08 | **93.12** | 🌟 Top Performer |
| **3** | **DRV-004** | 10 | 10 | 0 | **100.0%** | 0.0% | PKR 4,007.00 | 4.36 ★ | 12.75 | **93.08** | 🌟 Top Performer |
| **4** | **DRV-002** | 10 | 9 | 1 | 90.0% | 10.0% | **PKR 4,484.00** | 4.23 ★ | 14.17 | **86.13** | 🚀 High Revenue / Warning |
| **5** | **DRV-003** | 10 | 9 | 1 | 90.0% | 10.0% | PKR 4,047.00 | 4.39 ★ | 12.92 | **82.38** | 🟢 Consistent |
| **6** | **DRV-008** | 10 | 9 | 1 | 90.0% | 10.0% | PKR 3,846.00 | 4.24 ★ | 12.24 | **80.00** | 🟢 Consistent |
| **7** | **DRV-006** | 10 | 8 | 2 | 80.0% | 20.0% | PKR 3,369.00 | **4.64 ★** | 11.85 | **73.49** | ⭐ Highest Quality / Churn Risk |
| **8** | **DRV-009** | 10 | 8 | 2 | 80.0% | 20.0% | PKR 3,257.00 | 4.19 ★ | 11.84 | **68.61** | 🟡 Needs Improvement |
| **9** | **DRV-007** | 10 | 7 | 3 | 70.0% | 30.0% | PKR 2,829.00 | 4.29 ★ | 12.00 | **54.99** | 🔴 High Cancellation |
| **10**| **DRV-005** | 10 | 6 | 4 | **60.0%** | **40.0%** | PKR 2,235.00 | 4.08 ★ | 10.70 | **37.75** | ⛔ Severe Operational Risk |

---

### 📈 Visual Gallery (10 Required Analytical Charts)
All charts are rendered at high resolution (300 DPI) with executive styling:

| Chart | Preview | Description |
| :--- | :--- | :--- |
| **1. Revenue by Month** | `01_revenue_by_month.png` | September 2026 monthly baseline (PKR 36,466) |
| **2. Revenue by Location** | `02_revenue_by_location.png` | DHA leads (PKR 15.4k), followed by Bahria Town (PKR 6.6k) |
| **3. Revenue by Payment** | `03_revenue_by_payment_method.png` | Cash (38.7%) vs. Digital ecosystem (61.3%) |
| **4. Revenue by Ride Type** | `04_revenue_by_ride_type.png` | Standard tier generates 38.8% of total revenue |
| **5. Avg Fare by Ride Type**| `05_average_fare_by_ride_type.png` | Premium yields PKR 558.05 vs. Mini PKR 336.56 |
| **6. Top Drivers by Revenue**| `06_top_drivers_by_revenue.png` | DRV-002 leads raw revenue (PKR 4,484) |
| **7. Top Drivers by Volume** | `07_top_drivers_by_completed_rides.png` | DRV-001, 004, 010 achieve 100% completion (10 rides) |
| **8. Driver Rating Comparison**| `08_driver_rating_comparison.png` | DRV-006 tops customer satisfaction at 4.64 ★ |
| **9. Driver Completion Rate**| `09_driver_completion_rate.png` | 3 drivers at 100%, 3 at 90%, 2 at 80%, 1 at 70%, 1 at 60% |
| **10. Driver Cancellation Rate**| `10_driver_cancellation_rate.png` | DRV-005 flags critical operational leakage (40% cancel) |

*Inspect all chart images in [reports/week-03/charts/](reports/week-03/charts/) and [screenshots/week-03/](screenshots/week-03/).*

---

### 💡 Executive Insights & Strategic Recommendations
1. **The "Revenue Mirage" vs. True Operational Excellence**: While `DRV-002` yielded the highest gross revenue (PKR 4,484.00), they incurred cancellations. `DRV-010` and `DRV-004` deliver 100% fulfillment, zero customer disappointment, and superior overall value.
2. **Geographic Yield Imbalance**: **DHA** drives 42.2% of platform revenue with an above-average fare of PKR 439.66 and only 7.9% cancellation. Conversely, **Gulberg** experiences a **30.0% cancellation rate** and lowest average fare (PKR 397.07), suffering severe driver supply mismatch.
3. **Cash Dependency & Leakage Mitigation**: Cash makes up 38.7% of collections. Transitioning users to digital wallets through 5% cash-back incentives will curb unrecorded driver disputes and shorten passenger onboarding delays.
4. **Targeted Driver Intervention**: `DRV-005` (40% cancellation, PKR 2,235 revenue) and `DRV-007` (30% cancellation) require immediate schedule adjustments, re-training, or platform warnings before deactivation.

---

## 🚕 Week 2 — Ride Analytics & Revenue Intelligence Platform

**Project Title**: Ride Analytics & Revenue Intelligence Platform  
**Program**: ZYROO Data Analytics Internship • Week 2  
**Deliverables**: Cleaned Dataset, Data Pipeline Script, DAX Measure Catalog, Interactive Dashboard, and Power BI Report Specification

![Week 2 Dashboard Preview](week-02/assets/dashboard_preview.png)

* **Completed Rides**: `85 rides` (85.0% fulfillment)
* **Cancelled Rides**: `15 rides` (15.0% churn)
* **Realized Revenue**: `PKR 36,466.00`
* **Average Fare**: `PKR 429.01`
* **Average Rating**: `4.27 ★`

---

## 🛠️ Week 1 — Onboarding & Environment Setup

The objective of **Task 01** was establishing an isolated analytics environment, verifying Python, SQL, Excel, and Power BI environments, benchmark testing on structured datasets, and publishing to GitHub.

---

## 📁 Repository Structure

```text
zyro-data-analyst-internship/
│
├── week-03/                                # Week 3: Revenue & Driver Performance Analysis
│   ├── rides_data_week3.csv               # Standardized 100-row production dataset
│   ├── week_03_revenue_driver_analysis.sql# Production SQL pipeline (SQLite/PostgreSQL)
│   ├── week_03_revenue_driver_analysis.ipynb# Executed Jupyter Notebook with outputs
│   ├── reports/
│   │   ├── week_03_revenue_driver_analysis_report.md # 16-section executive report
│   │   ├── location_revenue_analysis.csv  # Location financial breakdown
│   │   ├── payment_revenue_analysis.csv   # Payment method share breakdown
│   │   ├── ride_type_revenue_analysis.csv # Tier financial breakdown
│   │   └── driver_performance_ranking.csv # Full multi-criteria driver ranking table
│   └── charts/                            # 10 High-resolution analytical charts (PNG)
│       ├── 01_revenue_by_month.png
│       ├── 02_revenue_by_location.png
│       ├── 03_revenue_by_payment_method.png
│       ├── 04_revenue_by_ride_type.png
│       ├── 05_average_fare_by_ride_type.png
│       ├── 06_top_drivers_by_revenue.png
│       ├── 07_top_drivers_by_completed_rides.png
│       ├── 08_driver_rating_comparison.png
│       ├── 09_driver_completion_rate.png
│       └── 10_driver_cancellation_rate.png
│
├── data/                                   # Centralized data directory
│   ├── rides_data_week3.csv
│   └── rides_data_cleaned.csv
│
├── sql/                                    # Centralized SQL repository
│   └── week_03_revenue_driver_analysis.sql
│
├── python/                                 # Centralized Python code repository
│   └── week-03-revenue-driver-analysis/
│       ├── analyze_week3.py
│       └── week_03_revenue_driver_analysis.ipynb
│
├── reports/                                # Centralized executive reporting
│   └── week-03/
│       ├── week_03_revenue_driver_analysis_report.md
│       ├── location_revenue_analysis.csv
│       ├── payment_revenue_analysis.csv
│       ├── ride_type_revenue_analysis.csv
│       ├── driver_performance_ranking.csv
│       └── charts/ (10 PNGs)
│
├── screenshots/                            # Visual evidence for evaluations
│   ├── week-01/ (7 PNGs)
│   └── week-03/ (10 PNGs)
│
├── week-02/                                # Week 2: Power BI Ride Analytics Platform
│   ├── rides_data_cleaned.csv
│   ├── clean_and_analyze.py
│   ├── dax_measures.dax
│   ├── dashboard_interactive.html
│   └── assets/dashboard_preview.png
│
├── week-01/                                # Week 1: Environment & Tooling Verification
│   ├── environment_test.ipynb
│   ├── sql_test.sql
│   ├── sales_data.csv
│   ├── sales_test.xlsx
│   └── evidence/
│
├── README.md                              # Portfolio master documentation
├── requirements.txt                       # Pinned Python package dependencies
└── .gitignore                             # Git exclusion rules
```

---

## 💻 Technical Environment
* **Platform**: Windows 11 / PowerShell 5.1 / Python 3.13.15
* **Analytics Stack**: Pandas, NumPy, Matplotlib, Seaborn, OpenPyXL, SQLite3, nbclient, nbformat
* **Business Intelligence**: Power BI Desktop, Microsoft Excel 2016/365, Google Looker Studio
* **Version Control**: Git 2.55 & GitHub CLI
