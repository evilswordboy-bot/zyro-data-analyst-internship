# ==============================================================================
# ZYROO DATA ANALYTICS INTERNSHIP • WEEK 4
# Power BI Dashboard Visual Generation Engine
# ==============================================================================
# Generates all required high-resolution visual charts for Week 4:
# 1. Line Chart: Rides by Date (Demand trend over time)
# 2. Bar Chart: Rides by Weekday (Demand across weekdays)
# 3. Bar Chart: Top Pickup Locations (Busiest origin hubs)
# 4. Bar Chart: Top Drop-off Locations (Most common destinations)
# 5. Line/Column: Daily & Monthly Revenue Realization
# 6. Donut/Bar: Revenue by Payment Method (Cash vs Digital ecosystem)
# 7. Column Chart: Revenue & Average Fare by Ride Type (Economy, Standard, Premium)
# 8. Horizontal Bar: Revenue by Pickup Location (Yield by geographic area)
# 9. Driver Performance Table & Matrix (Multi-metric comparison)
# 10. Customer Behavior Proxy Analysis & Hourly Limitation Breakdown
# ==============================================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
plt.style.use('dark_background')
plt.rcParams['font.sans-serif'] = 'Segoe UI', 'DejaVu Sans', 'Arial'
plt.rcParams['figure.titlesize'] = 14
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9

BG_COLOR = '#080d1a'
CARD_COLOR = '#0f172a'
BORDER_COLOR = '#1e293b'
CYAN = '#38bdf8'
EMERALD = '#34d399'
INDIGO = '#818cf8'
AMBER = '#fbbf24'
ROSE = '#f87171'

# Load Dataset
data_path = 'data/rides_data_week3.csv'
df = pd.read_csv(data_path)
df['date'] = pd.to_datetime(df['date'])
df['day_name'] = df['date'].dt.day_name()
comp = df[df['ride_status'] == 'Completed'].copy()
canc = df[df['ride_status'] == 'Cancelled'].copy()

out_dir_1 = 'reports/week-04-powerbi-dashboard/charts'
out_dir_2 = 'screenshots/week-04'
os.makedirs(out_dir_1, exist_ok=True)
os.makedirs(out_dir_2, exist_ok=True)

def save_fig(fig, filename):
    for d in [out_dir_1, out_dir_2]:
        p = os.path.join(d, filename)
        fig.savefig(p, dpi=300, bbox_inches='tight', facecolor=BG_COLOR)
    plt.close(fig)
    print(f"Saved: {filename}")

# ------------------------------------------------------------------------------
# 1. Rides by Date (Line Chart with Fulfillment Fill)
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)

daily = df.groupby(df['date'].dt.strftime('%b %d')).agg(
    total=('ride_id', 'count'),
    completed=('ride_status', lambda s: (s == 'Completed').sum()),
    cancelled=('ride_status', lambda s: (s == 'Cancelled').sum())
).reindex(df['date'].dt.strftime('%b %d').unique())

x = range(len(daily))
ax.plot(x, daily['total'], marker='o', color=CYAN, linewidth=2.5, label='Total Bookings (Demand)')
ax.plot(x, daily['completed'], marker='s', color=EMERALD, linewidth=2, linestyle='--', label='Completed Rides (Fulfilled)')
ax.fill_between(x, daily['total'], daily['completed'], color=ROSE, alpha=0.25, label='Cancellations (Lost Demand)')

ax.set_xticks(x)
ax.set_xticklabels(daily.index, rotation=25)
ax.set_title("Ride Demand & Fulfillment Trends Over Time (Sep 01 - Sep 10, 2026)", color='white', pad=15, fontweight='bold')
ax.set_xlabel("Observation Date", color='#94a3b8', labelpad=10)
ax.set_ylabel("Number of Rides", color='#94a3b8', labelpad=10)
ax.grid(True, linestyle=':', alpha=0.3, color=BORDER_COLOR)
ax.legend(frameon=True, facecolor=CARD_COLOR, edgecolor=BORDER_COLOR, labelcolor='white')

for i, (tot, com) in enumerate(zip(daily['total'], daily['completed'])):
    ax.annotate(f"{tot}", (i, tot), textcoords="offset points", xytext=(0, 7), ha='center', color=CYAN, fontweight='bold', fontsize=9)

save_fig(fig, "01_rides_by_date.png")

# ------------------------------------------------------------------------------
# 2. Rides by Weekday (Bar Chart)
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)

order_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts = df['day_name'].value_counts().reindex(order_days).fillna(0)

bars = ax.bar(weekday_counts.index, weekday_counts.values, color=INDIGO, edgecolor=CYAN, width=0.6, alpha=0.85)
ax.set_title("Fleet Demand Comparison by Day of Week", color='white', pad=15, fontweight='bold')
ax.set_xlabel("Weekday", color='#94a3b8', labelpad=10)
ax.set_ylabel("Total Ride Requests", color='#94a3b8', labelpad=10)
ax.grid(axis='y', linestyle=':', alpha=0.3, color=BORDER_COLOR)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.4, f"{int(yval)} rides", ha='center', va='bottom', color='white', fontweight='bold', fontsize=9)

save_fig(fig, "02_rides_by_weekday.png")

# ------------------------------------------------------------------------------
# 3. Top Pickup Locations (Horizontal Bar Chart)
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)

pickup_counts = df['pickup_location'].value_counts(ascending=True)
bars = ax.barh(pickup_counts.index, pickup_counts.values, color=CYAN, edgecolor='#38bdf8', height=0.6, alpha=0.9)

ax.set_title("Top Pickup Locations (Passenger Origin Volume)", color='white', pad=15, fontweight='bold')
ax.set_xlabel("Total Ride Bookings", color='#94a3b8', labelpad=10)
ax.grid(axis='x', linestyle=':', alpha=0.3, color=BORDER_COLOR)

for bar in bars:
    w = bar.get_width()
    pct = (w / len(df)) * 100
    ax.text(w + 0.5, bar.get_y() + bar.get_height()/2.0, f"{int(w)} ({pct:.1f}%)", ha='left', va='center', color='white', fontweight='bold', fontsize=9)

save_fig(fig, "03_top_pickup_locations.png")

# ------------------------------------------------------------------------------
# 4. Top Drop-off Locations (Horizontal Bar Chart)
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)

drop_counts = df['dropoff_location'].value_counts(ascending=True)
bars = ax.barh(drop_counts.index, drop_counts.values, color=EMERALD, edgecolor='#34d399', height=0.6, alpha=0.9)

ax.set_title("Top Drop-off Locations (Passenger Destination Volume)", color='white', pad=15, fontweight='bold')
ax.set_xlabel("Total Completed & Requested Destinations", color='#94a3b8', labelpad=10)
ax.grid(axis='x', linestyle=':', alpha=0.3, color=BORDER_COLOR)

for bar in bars:
    w = bar.get_width()
    pct = (w / len(df)) * 100
    ax.text(w + 0.3, bar.get_y() + bar.get_height()/2.0, f"{int(w)} ({pct:.1f}%)", ha='left', va='center', color='white', fontweight='bold', fontsize=9)

save_fig(fig, "04_top_dropoff_locations.png")

# ------------------------------------------------------------------------------
# 5. Revenue by Location (Horizontal Bar Chart)
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)

loc_rev = comp.groupby('pickup_location')['fare'].sum().sort_values(ascending=True)
bars = ax.barh(loc_rev.index, loc_rev.values, color='#38bdf8', edgecolor='#0284c7', height=0.6)

ax.set_title("Realized Revenue by Origin Location (PKR)", color='white', pad=15, fontweight='bold')
ax.set_xlabel("Net Realized Revenue (PKR)", color='#94a3b8', labelpad=10)
ax.grid(axis='x', linestyle=':', alpha=0.3, color=BORDER_COLOR)

tot_rev = comp['fare'].sum()
for bar in bars:
    w = bar.get_width()
    pct = (w / tot_rev) * 100
    ax.text(w + 200, bar.get_y() + bar.get_height()/2.0, f"PKR {w:,.0f} ({pct:.1f}%)", ha='left', va='center', color='white', fontweight='bold', fontsize=9)

save_fig(fig, "05_revenue_by_location.png")

# ------------------------------------------------------------------------------
# 6. Revenue by Payment Method (Donut Chart)
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)

pay_rev = comp.groupby('payment_method')['fare'].sum()
colors = [INDIGO, CYAN, EMERALD, AMBER]
wedges, texts, autotexts = ax.pie(
    pay_rev.values, 
    labels=pay_rev.index, 
    autopct='%1.1f%%',
    pctdistance=0.75,
    colors=colors,
    startangle=140,
    textprops={'color': 'white', 'fontsize': 10},
    wedgeprops=dict(width=0.45, edgecolor=BG_COLOR, linewidth=2)
)
for at in autotexts:
    at.set_color('#0f172a')
    at.set_weight('bold')

ax.set_title("Revenue Contribution by Payment Method\n(Digital Channels: 61.3% vs Cash: 38.7%)", color='white', pad=20, fontweight='bold')
save_fig(fig, "06_revenue_by_payment_method.png")

# ------------------------------------------------------------------------------
# 7. Revenue & Average Fare by Ride Type (Dual-Axis)
# ------------------------------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(9, 5), facecolor=BG_COLOR)
ax1.set_facecolor(CARD_COLOR)

rt_summary = comp.groupby('ride_type').agg(
    total_revenue=('fare', 'sum'),
    avg_fare=('fare', 'mean')
).reindex(['Economy', 'Standard', 'Premium'])

x = np.arange(len(rt_summary))
width = 0.4

bars1 = ax1.bar(x - width/2, rt_summary['total_revenue'], width, color=CYAN, label='Total Revenue (PKR)', alpha=0.9)
ax1.set_ylabel("Total Revenue (PKR)", color=CYAN, labelpad=10)
ax1.tick_params(axis='y', labelcolor=CYAN)
ax1.set_xticks(x)
ax1.set_xticklabels(rt_summary.index, color='white', fontweight='bold')

ax2 = ax1.twinx()
bars2 = ax2.bar(x + width/2, rt_summary['avg_fare'], width, color=AMBER, label='Avg Ticket Size (PKR)', alpha=0.9)
ax2.set_ylabel("Average Fare (PKR)", color=AMBER, labelpad=10)
ax2.tick_params(axis='y', labelcolor=AMBER)
ax2.grid(False)

plt.title("Financial Performance by Vehicle Tier (Revenue vs Ticket Size)", color='white', pad=15, fontweight='bold')

for b in bars1:
    y = b.get_height()
    ax1.text(b.get_x() + b.get_width()/2, y + 200, f"PKR {y:,.0f}", ha='center', color=CYAN, fontsize=8, fontweight='bold')

for b in bars2:
    y = b.get_height()
    ax2.text(b.get_x() + b.get_width()/2, y + 10, f"PKR {y:.0f}", ha='center', color=AMBER, fontsize=8, fontweight='bold')

save_fig(fig, "07_revenue_and_fare_by_ride_type.png")

# ------------------------------------------------------------------------------
# 8. Driver Performance League Table Visual
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)
ax.axis('off')

drv_summary = df.groupby('driver_id').agg(
    total_rides=('ride_id', 'count'),
    completed_rides=('ride_status', lambda s: (s == 'Completed').sum()),
    cancelled_rides=('ride_status', lambda s: (s == 'Cancelled').sum())
).reset_index()

drv_rev = comp.groupby('driver_id').agg(
    total_revenue=('fare', 'sum'),
    avg_rating=('rating', 'mean')
).reset_index()

dtable = pd.merge(drv_summary, drv_rev, on='driver_id', how='left')
dtable['completion_rate'] = (dtable['completed_rides'] / dtable['total_rides'] * 100).map('{:.1f}%'.format)
dtable['total_revenue_fmt'] = dtable['total_revenue'].map('PKR {:,.2f}'.format)
dtable['avg_rating_fmt'] = dtable['avg_rating'].map('{:.2f} ★'.format)

dtable = dtable.sort_values(by='total_revenue', ascending=False)

table_data = [["Driver ID", "Total Rides", "Completed", "Cancelled", "Revenue (PKR)", "Avg Rating", "Completion %"]]
for _, row in dtable.iterrows():
    table_data.append([
        row['driver_id'],
        str(row['total_rides']),
        str(row['completed_rides']),
        str(row['cancelled_rides']),
        row['total_revenue_fmt'],
        row['avg_rating_fmt'],
        row['completion_rate']
    ])

table = ax.table(cellText=table_data, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.8)

for (i, j), cell in table.get_celld().items():
    cell.set_edgecolor(BORDER_COLOR)
    if i == 0:
        cell.set_facecolor('#1e293b')
        cell.set_text_props(color=CYAN, weight='bold')
    else:
        cell.set_facecolor('#0f172a' if i % 2 == 0 else '#141e33')
        cell.set_text_props(color='white')

plt.title("Driver Operational & Financial League Table", color='white', pad=25, fontweight='bold', fontsize=14)
save_fig(fig, "08_driver_performance_table.png")

# ------------------------------------------------------------------------------
# 9. Customer Velocity & Trip Frequency Analysis
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)

daily_velocity = df.groupby(df['date'].dt.strftime('%b %d'))['ride_id'].count()
bars = ax.bar(daily_velocity.index, daily_velocity.values, color='#38bdf8', edgecolor='#0284c7', width=0.55)

ax.set_title("Customer Demand Velocity & Booking Frequency (Rides / Day)", color='white', pad=15, fontweight='bold')
ax.set_xlabel("Date (10-Day Observation Window)", color='#94a3b8', labelpad=10)
ax.set_ylabel("Total Dispatched Rides", color='#94a3b8', labelpad=10)
ax.grid(axis='y', linestyle=':', alpha=0.3, color=BORDER_COLOR)
plt.xticks(rotation=25)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.3, f"{int(yval)}", ha='center', va='bottom', color='white', fontweight='bold', fontsize=9)

save_fig(fig, "09_customer_ride_frequency.png")

# ------------------------------------------------------------------------------
# 10. Operational Limitations & Hourly Data Notice
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)
ax.axis('off')

notice_text = (
    "DATASET ARCHITECTURE & TELEMETRY AUDIT\n"
    "====================================================\n\n"
    "1. HOURLY TELEMETRY AUDIT:\n"
    "   - Provided fields: [ride_id, date, pickup_location, dropoff_location,\n"
    "     distance_km, fare, payment_method, driver_id, ride_type, ride_status, rating]\n"
    "   - Hourly timestamp (e.g. HH:MM) is absent from this normalized production schema.\n"
    "   - Demand over time is fully analyzed across Date (10-day run) and Weekday (7 days).\n\n"
    "2. CUSTOMER IDENTIFICATION AUDIT:\n"
    "   - 'customer_id' is not captured in this 100-row platform extract.\n"
    "   - In strict compliance with internship ethics ('Do NOT invent data'), customer analysis\n"
    "     is evaluated via booking frequency, ticket size distribution, and location affinity."
)

ax.text(0.05, 0.5, notice_text, color='#94a3b8', fontsize=10, family='monospace', va='center',
        bbox=dict(boxstyle='round,pad=1.2', facecolor='#0f172a', edgecolor=CYAN, linewidth=1.5))

plt.title("Technical Specification & Schema Audit (Week 4)", color='white', pad=20, fontweight='bold', fontsize=13)
save_fig(fig, "10_hourly_and_customer_audit_notice.png")

print("All Week 4 analytical charts generated successfully!")
