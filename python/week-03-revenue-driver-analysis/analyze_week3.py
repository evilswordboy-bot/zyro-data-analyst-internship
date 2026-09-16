"""
ZYROO DATA ANALYTICS INTERNSHIP — WEEK 3
Revenue & Driver Performance Analysis Engine
Generates Core KPIs, Driver Performance Matrices, Visualizations & Insights
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json

# Ensure target directories
os.makedirs("reports/week-03/charts", exist_ok=True)
os.makedirs("screenshots/week-03", exist_ok=True)

# 1. LOAD DATASET
print("=" * 70)
print("1. DATA INGESTION & DATA QUALITY AUDIT")
print("=" * 70)
df = pd.read_csv("data/rides_data_week3.csv")
df['date'] = pd.to_datetime(df['date'])

print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print("\nFirst 5 Records:")
print(df.head())

print("\nMissing Values per Column:")
print(df.isnull().sum())

print("\nDuplicate Records Count:", df.duplicated(subset=['ride_id']).sum())

# Only completed rides count as realized revenue
completed_df = df[df['ride_status'] == 'Completed'].copy()
cancelled_df = df[df['ride_status'] == 'Cancelled'].copy()

# 2. CORE REVENUE KPIS
total_rides = len(df)
completed_rides = len(completed_df)
cancelled_rides = len(cancelled_df)
completion_rate = (completed_rides / total_rides) * 100
cancellation_rate = (cancelled_rides / total_rides) * 100

realized_revenue = completed_df['fare'].sum()
gross_booking_value = df['fare'].sum()
unrealized_revenue_loss = gross_booking_value - realized_revenue
avg_fare_completed = completed_df['fare'].mean()
avg_fare_overall = df['fare'].mean()
avg_revenue_per_completed_ride = realized_revenue / completed_rides
avg_rating_completed = completed_df['rating'].dropna().mean()

print("\n" + "=" * 70)
print("2. CORE REVENUE & OPERATIONAL KPIS")
print("=" * 70)
print(f"• Total Booked Rides           : {total_rides}")
print(f"• Total Completed Rides        : {completed_rides} ({completion_rate:.1f}%)")
print(f"• Total Cancelled Rides        : {cancelled_rides} ({cancellation_rate:.1f}%)")
print(f"• Total Realized Revenue       : PKR {realized_revenue:,.2f}")
print(f"• Gross Booking Value (GBV)    : PKR {gross_booking_value:,.2f}")
print(f"• Churn Leakage (Lost Revenue) : PKR {unrealized_revenue_loss:,.2f}")
print(f"• Average Fare (Completed)     : PKR {avg_fare_completed:,.2f}")
print(f"• Avg Revenue / Completed Ride : PKR {avg_revenue_per_completed_ride:,.2f}")
print(f"• Average Driver Rating        : {avg_rating_completed:.2f} / 5.00")

# 3. REVENUE BY LOCATION
print("\n" + "=" * 70)
print("3. REVENUE BY PICKUP LOCATION")
print("=" * 70)
loc_revenue = completed_df.groupby('pickup_location').agg(
    completed_rides=('ride_id', 'count'),
    total_revenue=('fare', 'sum'),
    avg_fare=('fare', 'mean')
).reset_index()

# Merge with total bookings for demand-to-revenue comparison
loc_demand = df.groupby('pickup_location').agg(total_rides=('ride_id', 'count')).reset_index()
loc_analysis = pd.merge(loc_demand, loc_revenue, on='pickup_location', how='left').fillna(0)
loc_analysis['revenue_pct'] = (loc_analysis['total_revenue'] / realized_revenue) * 100
loc_analysis['rides_pct'] = (loc_analysis['total_rides'] / total_rides) * 100
loc_analysis = loc_analysis.sort_values(by='total_revenue', ascending=False)
print(loc_analysis.to_string(index=False))

# 4. REVENUE BY PAYMENT METHOD
print("\n" + "=" * 70)
print("4. REVENUE BY PAYMENT METHOD")
print("=" * 70)
pay_analysis = completed_df.groupby('payment_method').agg(
    completed_rides=('ride_id', 'count'),
    total_revenue=('fare', 'sum'),
    avg_fare=('fare', 'mean')
).reset_index()
pay_analysis['revenue_pct'] = (pay_analysis['total_revenue'] / realized_revenue) * 100
pay_analysis['completed_rides_pct'] = (pay_analysis['completed_rides'] / completed_rides) * 100
pay_analysis = pay_analysis.sort_values(by='total_revenue', ascending=False)
print(pay_analysis.to_string(index=False))

# 5. REVENUE BY RIDE TYPE
print("\n" + "=" * 70)
print("5. REVENUE BY RIDE TYPE")
print("=" * 70)
ride_type_analysis = completed_df.groupby('ride_type').agg(
    completed_rides=('ride_id', 'count'),
    total_revenue=('fare', 'sum'),
    avg_fare=('fare', 'mean')
).reset_index()
ride_type_analysis['revenue_pct'] = (ride_type_analysis['total_revenue'] / realized_revenue) * 100
ride_type_analysis = ride_type_analysis.sort_values(by='total_revenue', ascending=False)
print(ride_type_analysis.to_string(index=False))

# 6. DRIVER PERFORMANCE TABLE
print("\n" + "=" * 70)
print("6. DRIVER PERFORMANCE MATRIX")
print("=" * 70)
driver_summary = df.groupby('driver_id').agg(
    total_rides=('ride_id', 'count'),
    completed_rides=('ride_status', lambda x: (x == 'Completed').sum()),
    cancelled_rides=('ride_status', lambda x: (x == 'Cancelled').sum()),
    revenue=('fare', lambda x: df.loc[x.index][df.loc[x.index, 'ride_status'] == 'Completed']['fare'].sum()),
    avg_rating=('rating', 'mean'),
    avg_distance_km=('distance_km', 'mean'),
    avg_fare=('fare', lambda x: df.loc[x.index][df.loc[x.index, 'ride_status'] == 'Completed']['fare'].mean())
).reset_index()

driver_summary['completion_rate'] = (driver_summary['completed_rides'] / driver_summary['total_rides']) * 100
driver_summary['cancellation_rate'] = (driver_summary['cancelled_rides'] / driver_summary['total_rides']) * 100

# 7. DRIVER COMPOSITE RANKING METHODOLOGY
# We do not rank by revenue alone. We use an explicit multi-factor weighting:
# - Revenue Normalized (35%): Measures top-line financial contribution
# - Completed Rides Normalized (25%): Measures volume and driver capacity
# - Driver Rating Normalized (25%): Measures passenger satisfaction and service quality
# - Completion Rate Normalized (15%): Measures fleet reliability and low churn
max_rev = driver_summary['revenue'].max()
max_comp = driver_summary['completed_rides'].max()

driver_summary['composite_score'] = (
    0.35 * (driver_summary['revenue'] / max_rev) +
    0.25 * (driver_summary['completed_rides'] / max_comp) +
    0.25 * (driver_summary['avg_rating'].fillna(4.0) / 5.0) +
    0.15 * (driver_summary['completion_rate'] / 100.0)
) * 100

driver_summary = driver_summary.sort_values(by='composite_score', ascending=False).reset_index(drop=True)
driver_summary['rank'] = driver_summary.index + 1

# Reorder columns
driver_cols = [
    'rank', 'driver_id', 'total_rides', 'completed_rides', 'cancelled_rides',
    'revenue', 'avg_rating', 'avg_distance_km', 'completion_rate',
    'cancellation_rate', 'avg_fare', 'composite_score'
]
driver_summary = driver_summary[driver_cols]
print(driver_summary.to_string(index=False))

# Export summary datasets
loc_analysis.to_csv("reports/week-03/location_revenue_analysis.csv", index=False)
pay_analysis.to_csv("reports/week-03/payment_revenue_analysis.csv", index=False)
ride_type_analysis.to_csv("reports/week-03/ride_type_revenue_analysis.csv", index=False)
driver_summary.to_csv("reports/week-03/driver_performance_ranking.csv", index=False)
driver_summary.to_csv("week-03/driver_performance_ranking.csv", index=False)

# 8. GENERATE ALL 10 REQUIRED VISUALIZATIONS
print("\n" + "=" * 70)
print("7. RENDERING ALL 10 REQUIRED CHARTS")
print("=" * 70)

# Set clean, professional visual style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
palette_blue = sns.color_palette("Blues_r", 10)

def save_dual_chart(fig, filename):
    p1 = f"reports/week-03/charts/{filename}"
    p2 = f"screenshots/week-03/{filename}"
    fig.savefig(p1, dpi=180, bbox_inches='tight')
    fig.savefig(p2, dpi=180, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved: {filename}")

# Chart 1: Revenue by Month / Day
fig, ax = plt.subplots(figsize=(9, 4.5))
daily_rev = completed_df.groupby(completed_df['date'].dt.strftime('%d %b'))['fare'].sum().reindex(
    [d.strftime('%d %b') for d in sorted(completed_df['date'].unique())]
)
ax.plot(daily_rev.index, daily_rev.values, marker='o', color='#0284c7', linewidth=2.5, markersize=7)
ax.fill_between(daily_rev.index, daily_rev.values, color='#0284c7', alpha=0.18)
ax.set_title("Revenue by Observation Period (September 2026)", fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel("Date", fontsize=11, labelpad=8)
ax.set_ylabel("Realized Revenue (PKR)", fontsize=11, labelpad=8)
for i, v in enumerate(daily_rev.values):
    ax.text(i, v + 90, f"₨{v:,}", ha='center', fontsize=8.5, fontweight='bold', color='#0369a1')
ax.set_ylim(0, max(daily_rev.values) * 1.18)
save_dual_chart(fig, "01_revenue_by_month.png")

# Chart 2: Revenue by Location
fig, ax = plt.subplots(figsize=(9, 4.5))
bars = ax.barh(loc_analysis['pickup_location'][::-1], loc_analysis['total_revenue'][::-1], color='#0284c7', height=0.6)
ax.set_title("Total Realized Revenue by Pickup Location", fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel("Realized Revenue (PKR)", fontsize=11, labelpad=8)
ax.set_ylabel("Pickup Location", fontsize=11, labelpad=8)
for bar in bars:
    w = bar.get_width()
    ax.text(w + 200, bar.get_y() + bar.get_height()/2, f"₨{int(w):,} ({w/realized_revenue*100:.1f}%)", va='center', fontsize=9, fontweight='semibold')
ax.set_xlim(0, max(loc_analysis['total_revenue']) * 1.25)
save_dual_chart(fig, "02_revenue_by_location.png")

# Chart 3: Revenue by Payment Method
fig, ax = plt.subplots(figsize=(8, 4.5))
sns.barplot(data=pay_analysis, x='payment_method', y='total_revenue', palette='Blues_d', ax=ax, hue='payment_method', legend=False)
ax.set_title("Revenue Contribution by Payment Method", fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel("Payment Method", fontsize=11, labelpad=8)
ax.set_ylabel("Realized Revenue (PKR)", fontsize=11, labelpad=8)
for bar in ax.patches:
    h = bar.get_height()
    ax.annotate(f"₨{int(h):,}\n({h/realized_revenue*100:.1f}%)",
                xy=(bar.get_x() + bar.get_width()/2, h), xytext=(0, 6),
                textcoords="offset points", ha='center', fontsize=9, fontweight='bold')
ax.set_ylim(0, max(pay_analysis['total_revenue']) * 1.22)
save_dual_chart(fig, "03_revenue_by_payment_method.png")

# Chart 4: Revenue by Ride Type
fig, ax = plt.subplots(figsize=(8, 4.5))
sns.barplot(data=ride_type_analysis, x='ride_type', y='total_revenue', palette=['#0284c7', '#38bdf8', '#0ea5e9'], ax=ax, hue='ride_type', legend=False)
ax.set_title("Total Revenue by Ride Type Tier", fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel("Ride Type Tier", fontsize=11, labelpad=8)
ax.set_ylabel("Realized Revenue (PKR)", fontsize=11, labelpad=8)
for bar in ax.patches:
    h = bar.get_height()
    ax.annotate(f"₨{int(h):,}\n({h/realized_revenue*100:.1f}%)",
                xy=(bar.get_x() + bar.get_width()/2, h), xytext=(0, 6),
                textcoords="offset points", ha='center', fontsize=9, fontweight='bold')
ax.set_ylim(0, max(ride_type_analysis['total_revenue']) * 1.22)
save_dual_chart(fig, "04_revenue_by_ride_type.png")

# Chart 5: Average Fare by Ride Type
fig, ax = plt.subplots(figsize=(8, 4.5))
sns.barplot(data=ride_type_analysis, x='ride_type', y='avg_fare', palette='Purples_r', ax=ax, hue='ride_type', legend=False)
ax.set_title("Average Fare Yield by Ride Type", fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel("Ride Type Tier", fontsize=11, labelpad=8)
ax.set_ylabel("Average Fare (PKR)", fontsize=11, labelpad=8)
for bar in ax.patches:
    h = bar.get_height()
    ax.annotate(f"₨{h:.2f}",
                xy=(bar.get_x() + bar.get_width()/2, h), xytext=(0, 6),
                textcoords="offset points", ha='center', fontsize=9.5, fontweight='bold')
ax.set_ylim(0, max(ride_type_analysis['avg_fare']) * 1.20)
save_dual_chart(fig, "05_average_fare_by_ride_type.png")

# Chart 6: Top Drivers by Revenue
fig, ax = plt.subplots(figsize=(9, 4.8))
top_rev_drivers = driver_summary.sort_values(by='revenue', ascending=True)
bars = ax.barh(top_rev_drivers['driver_id'], top_rev_drivers['revenue'], color='#0369a1', height=0.6)
ax.set_title("Fleet Drivers Ranked by Realized Revenue", fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel("Total Realized Revenue (PKR)", fontsize=11, labelpad=8)
ax.set_ylabel("Driver ID", fontsize=11, labelpad=8)
for bar in bars:
    w = bar.get_width()
    ax.text(w + 80, bar.get_y() + bar.get_height()/2, f"₨{int(w):,}", va='center', fontsize=8.5, fontweight='bold')
ax.set_xlim(0, max(top_rev_drivers['revenue']) * 1.20)
save_dual_chart(fig, "06_top_drivers_by_revenue.png")

# Chart 7: Top Drivers by Completed Rides
fig, ax = plt.subplots(figsize=(9, 4.8))
top_comp_drivers = driver_summary.sort_values(by='completed_rides', ascending=True)
bars = ax.barh(top_comp_drivers['driver_id'], top_comp_drivers['completed_rides'], color='#0d9488', height=0.6)
ax.set_title("Fleet Drivers Ranked by Completed Rides Volume", fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel("Completed Rides Count", fontsize=11, labelpad=8)
ax.set_ylabel("Driver ID", fontsize=11, labelpad=8)
for bar in bars:
    w = bar.get_width()
    ax.text(w + 0.15, bar.get_y() + bar.get_height()/2, f"{int(w)} rides", va='center', fontsize=8.5, fontweight='bold')
ax.set_xlim(0, max(top_comp_drivers['completed_rides']) * 1.25)
save_dual_chart(fig, "07_top_drivers_by_completed_rides.png")

# Chart 8: Driver Rating Comparison
fig, ax = plt.subplots(figsize=(9, 4.8))
driver_rating_sorted = driver_summary.sort_values(by='avg_rating', ascending=True)
bars = ax.barh(driver_rating_sorted['driver_id'], driver_rating_sorted['avg_rating'], color='#f59e0b', height=0.6)
ax.set_title("Driver Customer Rating Comparison (Out of 5.00 ★)", fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel("Average Rating (★)", fontsize=11, labelpad=8)
ax.set_ylabel("Driver ID", fontsize=11, labelpad=8)
for bar in bars:
    w = bar.get_width()
    ax.text(w + 0.08, bar.get_y() + bar.get_height()/2, f"{w:.2f} ★", va='center', fontsize=8.5, fontweight='bold')
ax.set_xlim(0, 5.5)
save_dual_chart(fig, "08_driver_rating_comparison.png")

# Chart 9: Driver Completion Rate
fig, ax = plt.subplots(figsize=(9, 4.8))
driver_comp_sorted = driver_summary.sort_values(by='completion_rate', ascending=True)
bars = ax.barh(driver_comp_sorted['driver_id'], driver_comp_sorted['completion_rate'], color='#10b981', height=0.6)
ax.set_title("Driver Completion Rate (%) — Fleet Reliability", fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel("Completion Rate (%)", fontsize=11, labelpad=8)
ax.set_ylabel("Driver ID", fontsize=11, labelpad=8)
for bar in bars:
    w = bar.get_width()
    ax.text(w + 1.2, bar.get_y() + bar.get_height()/2, f"{w:.1f}%", va='center', fontsize=8.5, fontweight='bold')
ax.set_xlim(0, 115)
save_dual_chart(fig, "09_driver_completion_rate.png")

# Chart 10: Driver Cancellation Rate
fig, ax = plt.subplots(figsize=(9, 4.8))
driver_canc_sorted = driver_summary.sort_values(by='cancellation_rate', ascending=False)
bars = ax.barh(driver_canc_sorted['driver_id'], driver_canc_sorted['cancellation_rate'], color='#f43f5e', height=0.6)
ax.set_title("Driver Cancellation Rate (%) — Operational Churn Risk", fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel("Cancellation Rate (%)", fontsize=11, labelpad=8)
ax.set_ylabel("Driver ID", fontsize=11, labelpad=8)
for bar in bars:
    w = bar.get_width()
    ax.text(w + 0.8, bar.get_y() + bar.get_height()/2, f"{w:.1f}%", va='center', fontsize=8.5, fontweight='bold', color='#be123c')
ax.set_xlim(0, max(driver_canc_sorted['cancellation_rate']) * 1.35)
save_dual_chart(fig, "10_driver_cancellation_rate.png")

print("\nSUCCESS: All 10 charts rendered and saved to reports/week-03/charts and screenshots/week-03.")
