# 🚀 Zyroo Data Analyst Internship

Welcome to my official portfolio repository for the **Zyroo Data Analyst Internship**. This repository serves as a centralized hub documenting all weekly technical tasks, exploratory data analyses, SQL pipelines, business intelligence dashboards, and project deliverables throughout the internship program.

---

## 📋 Overview

The primary goal of this internship program is to build industry-ready, end-to-end data analytics competency. Over the coming weeks, tasks will span across exploratory data analysis (EDA), data cleaning and wrangling, advanced relational querying (SQL), statistical modeling, and interactive executive reporting with Excel and Power BI.

---

## 🛠️ Week 1 — Onboarding & Environment Setup

The objective of **Task 01** is to establish an enterprise-grade analytics workstation, verify Python, SQL, Excel, and Power BI environments, perform benchmark testing on structured datasets, and enforce version control standards using Git and GitHub.

### Tools Used
* **Programming & Runtimes**: Python 3.13.15
* **Core Data Science Stack**: 
  * `pandas` (Data manipulation, profiling, and aggregation)
  * `numpy` (Numerical computing and array operations)
  * `matplotlib` (Foundational data visualization)
  * `seaborn` (Statistical visualization and theming)
* **Notebook Environment**: Jupyter Notebook / JupyterLab
* **Relational Database**: SQLite 3.50
* **Spreadsheet Analytics**: Microsoft Excel
* **Business Intelligence & Dashboards**: Power BI Desktop
* **Version Control & Collaboration**: Git 2.55 & GitHub

---

## 🔬 Week 1 Work Breakdown

### 1. Environment Verification & Python Setup
* Configured an isolated Python virtual environment (`.venv`) to guarantee reproducible package dependency management.
* Pinned core dependencies inside `requirements.txt`.
* Successfully verified library imports and runtime compatibility.

### 2. CSV Data Analysis Test (`week-01/environment_test.ipynb`)
* Ingested a sample retail transaction dataset (`sales_data.csv`).
* Inspected dataset dimensionality, column types, and confirmed zero null/missing values.
* Computed statistical distributions using `describe()` and computed total category revenues via `groupby`.

### 3. Data Visualization
* Rendered a customized, publication-style categorical bar chart depicting total sales revenue by product category using Seaborn and Matplotlib.
* Added currency data labels above each bar and exported the figure to `week-01/evidence/jupyter_analysis.png`.

### 4. Relational SQL Pipeline Test (`week-01/sql_test.sql`)
* Implemented SQLite DDL to model the relational `sales` table schema with data validation constraints.
* Populated realistic transaction records.
* Authored queries demonstrating `SELECT`, `WHERE` conditional filtering, mandatory `GROUP BY` counts, multi-metric aggregations (`SUM`, `AVG`, `MIN`, `MAX`), and `HAVING` filters.

### 5. Spreadsheet & BI Verification
* Modeled formatted sales transaction workbook with dynamic formula aggregations (`=SUM()`) in **Microsoft Excel**.
* Launched and validated **Power BI Desktop** environment for dashboard development.

---

## 📁 Repository Structure

```text
zyro-data-analyst-internship/
│
├── week-01/
│   ├── environment_test.ipynb     # Executed Jupyter notebook with CSV analysis & charts
│   ├── sql_test.sql               # SQLite DDL, DML and analytical benchmark queries
│   ├── sales_data.csv             # Structured retail transactions dataset
│   ├── sales_test.xlsx            # Formatted Microsoft Excel workbook with formulas
│   │
│   └── evidence/
│       ├── python_version.png     # Python runtime verification
│       ├── git_version.png        # Git CLI verification
│       ├── powerbi_setup.png      # Power BI Desktop interface launch proof
│       ├── excel_setup.png        # Microsoft Excel setup & formula test
│       ├── sql_test.png           # SQLite execution and query output proof
│       ├── jupyter_analysis.png   # Jupyter data analysis & Seaborn chart proof
│       └── zyroo_community.png    # Zyroo community onboarding confirmation
│
├── README.md                      # Internship repository documentation
├── requirements.txt               # Pinned Python package dependencies
└── .gitignore                     # Git exclusion rules for environments and temporary files
```

---

## ✅ Completion Status Checklist

### Zyroo Onboarding
- [x] Reviewed internship guidelines & objectives
- [x] Set up professional GitHub repository
- [ ] Joined official Zyroo community / communication channels (`zyroo_community.png`)

### Analytics Stack & Environment
- [x] Python 3.13 installed & verified
- [x] Virtual environment (`.venv`) configured
- [x] Pandas, NumPy, Matplotlib, Seaborn, and Jupyter installed & verified
- [x] Microsoft Excel verified with formulas (`sales_test.xlsx`)
- [x] Power BI Desktop installed & launched
- [x] SQLite relational database tested

### Week 1 Deliverables
- [x] Jupyter Notebook created, executed, and documented (`environment_test.ipynb`)
- [x] SQL script created, documented, and tested (`sql_test.sql`)
- [x] Project `requirements.txt` generated
- [x] Professional `.gitignore` configured
- [x] Evidence collected in `week-01/evidence/`
- [ ] Week 1 changes committed and pushed to GitHub
