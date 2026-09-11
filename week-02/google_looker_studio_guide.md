# 🌐 Google Ecosystem Integration Guide
## ZYROO Ride Analytics & Revenue Intelligence Platform

This guide documents the full integration of our Week 2 dataset with **Google Cloud, Google Sheets, Google Looker Studio, and Google Colab**.

---

## 1. 🚀 Google Colab (One-Click Cloud Execution)

We have created an executed, self-contained cloud analytics notebook:
👉 **[`ride_analytics_google_colab.ipynb`](ride_analytics_google_colab.ipynb)**

### How to Run in Google Colab:
1. Click the official badge on GitHub or open [Google Colab](https://colab.research.google.com/).
2. Select **GitHub** tab, enter repository:
   ```text
   evilswordboy-bot/zyro-data-analyst-internship
   ```
3. Open `week-02/ride_analytics_google_colab.ipynb`.
4. Run all cells (`Ctrl + F9`) to stream the dataset live from GitHub and re-calculate the entire executive dashboard!

---

## 2. 📊 Google Sheets Live Integration

We have created a native spreadsheet workbook with Google Sheets formulas:
👉 **[`rides_data_google_sheets.xlsx`](rides_data_google_sheets.xlsx)**

### Steps to Open in Google Sheets:
1. Go to [drive.google.com](https://drive.google.com) or [sheets.new](https://sheets.new).
2. Click **File ➔ Import ➔ Upload** and select `rides_data_google_sheets.xlsx` (or `rides_data_cleaned.csv`).
3. You get two sheets:
   * **`Cleaned Rides Data`**: Clean tabular dataset with 100 rows.
   * **`Executive KPIs & Formulas`**: Live Google Sheets formulas:
     * Total Rides: `=COUNTA('Cleaned Rides Data'!A2:A101)`
     * Completed Rides: `=COUNTIF('Cleaned Rides Data'!G2:G101, "Completed")`
     * Cancelled Rides: `=COUNTIF('Cleaned Rides Data'!G2:G101, "Cancelled")`
     * Realized Revenue: `=SUMIF('Cleaned Rides Data'!G2:G101, "Completed", 'Cleaned Rides Data'!E2:E101)`
     * Average Fare: `=AVERAGEIF('Cleaned Rides Data'!G2:G101, "Completed", 'Cleaned Rides Data'!E2:E101)`
     * Average Rating: `=AVERAGEIF('Cleaned Rides Data'!G2:G101, "Completed", 'Cleaned Rides Data'!H2:H101)`

---

## 3. 📈 Google Looker Studio (Cloud BI Dashboard)

You can build the cloud twin of your Power BI dashboard on Google Looker Studio (100% free, shareable via link):

### Step-by-Step Setup:
1. Go to **[lookerstudio.google.com](https://lookerstudio.google.com)**.
2. Click **Create ➔ Report**.
3. Choose **Google Sheets** as your connector and select your uploaded `rides_data_google_sheets` sheet (or use **CSV Upload**).
4. Configure the Visuals matching our Power BI layout:
   * **Theme:** Theme and Layout ➔ Dark Theme (Background `#0B1329`, Text `#FFFFFF`).
   * **Scorecards (Top KPIs):**
     * Metric: `Record Count` (Total Rides: 100)
     * Metric: `Fare` (Aggregation: SUM)
     * Metric: `Fare` (Aggregation: AVG)
     * Metric: `Rating` (Aggregation: AVG)
   * **Time Series Chart:** Dimension = `Date`, Metric = `Record Count` & `Fare`.
   * **Donut Charts:**
     * Donut 1: Dimension = `Payment Method`, Metric = `Record Count`.
     * Donut 2: Dimension = `Ride Status`, Metric = `Record Count`.
   * **Bar Chart:** Dimension = `Pickup Location`, Metric = `Record Count` (Sorted descending).
   * **Controls / Slicers:** Add Drop-down list controls for `Date`, `Pickup Location`, `Payment Method`, and `Ride Status`.

---

## 4. ⚡ Power BI Live Connection to Google Sheets

If your team maintains the dataset in Google Sheets, Power BI Desktop can connect directly to it:

1. In Google Sheets, click **File ➔ Share ➔ Publish to web**.
2. Select **Link ➔ Entire Document ➔ Comma-separated values (.csv)**.
3. Copy the generated Google URL.
4. In Power BI Desktop:
   * Click **Get data ➔ Web**.
   * Paste your Google Sheets Web CSV URL.
   * Click **OK ➔ Load**.
5. Power BI will now refresh automatically whenever new rides are added to Google Sheets!
