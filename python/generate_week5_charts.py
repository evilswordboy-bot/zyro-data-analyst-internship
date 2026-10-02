# ==============================================================================
# ZYROO DATA ANALYTICS INTERNSHIP • WEEK 5
# Advanced Business Intelligence Visual Generator
# ==============================================================================
# Generates all required charts for Week 5:
# 1. Location Demand vs Cancellation Matrix (Highlighting Gulberg high-risk zone)
# 2. Revenue Contribution vs Average Fare by Vehicle Tier (Standard vs Premium)
# 3. Driver Performance vs Cohort Benchmark (Revenue and completion deltas)
# 4. What-If Scenario Modeling (Hypothetical volume, fare, and churn recovery)
# 5. Customer Behavioral Segments (Premium Commuters, Standard Daily, Budget Hops)
# 6. Payment Ecosystem Contribution (Cash vs Cards, UPI, Wallets)
# 7. Day of Week Demand & Operational Risk Analysis
# 8. Time-Intelligence Revenue Trajectory & Daily Volatility
# ==============================================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

df = pd.read_csv('data/rides_data_week3.csv')
df['date'] = pd.to_datetime(df['date'])
df['day_name'] = df['date'].dt.day_name()
comp = df[df['ride_status'] == 'Completed'].copy()
canc = df[df['ride_status'] == 'Cancelled'].copy()

out_dirs = [
    'reports/week-05-advanced-bi/charts',
    'screenshots/week-05'
]
for d in out_dirs:
    os.makedirs(d, exist_ok=True)

def save_fig(fig, filename):
    for d in out_dirs:
        p = os.path.join(d, filename)
        fig.savefig(p, dpi=300, bbox_inches='tight', facecolor=BG_COLOR)
    plt.close(fig)
    print(f"Saved: {filename}")

# ------------------------------------------------------------------------------
# 1. Location Demand vs Cancellation Matrix (Highlighting Gulberg high-risk zone)
# ------------------------------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(10, 5.5), facecolor=BG_COLOR)
ax1.set_facecolor(CARD_COLOR)

loc_summary = df.groupby('pickup_location').agg(
    total_rides=('ride_id', 'count'),
    completed_rides=('ride_status', lambda s: (s == 'Completed').sum()),
    cancelled_rides=('ride_status', lambda s: (s == 'Cancelled').sum())
).sort_values(by='total_rides', ascending=False)
loc_summary['cancellation_rate'] = (loc_summary['cancelled_rides'] / loc_summary['total_rides'] * 100)

x = np.arange(len(loc_summary))
width = 0.45

bars1 = ax1.bar(x, loc_summary['total_rides'], width, color=CYAN, alpha=0.85, label='Total Demand Bookings')
ax1.set_ylabel('Total Dispatched Rides', color=CYAN, labelpad=10)
ax1.tick_params(axis='y', labelcolor=CYAN)
ax1.set_xticks(x)
ax1.set_xticklabels(loc_summary.index, color='white', fontweight='bold')

ax2 = ax1.twinx()
line2 = ax2.plot(x, loc_summary['cancellation_rate'], color=ROSE, marker='o', linewidth=3, markersize=8, label='Cancellation Rate (%)')
ax2.set_ylabel('Cancellation Rate (%)', color=ROSE, labelpad=10)
ax2.tick_params(axis='y', labelcolor=ROSE)
ax2.axhline(15.0, color='yellow', linestyle='--', alpha=0.5, label='Platform Mean (15%)')
ax2.grid(False)

for b in bars1:
    y = b.get_height()
    ax1.text(b.get_x() + b.get_width()/2, y + 0.8, f"{int(y)}", ha='center', color='white', fontweight='bold', fontsize=9)

for i, txt in enumerate(loc_summary['cancellation_rate']):
    ax2.annotate(f"{txt:.1f}%", (x[i], txt), textcoords="offset points", xytext=(0, 10), ha='center', color=ROSE, fontweight='bold', fontsize=9)

plt.title("Location Operational Matrix: Total Demand vs Cancellation Churn Rate\n(Notice Gulberg: High 20-Ride Demand combined with severe 30.0% Churn)", color='white', pad=20, fontweight='bold')
save_fig(fig, "01_location_demand_vs_cancellation.png")

# ------------------------------------------------------------------------------
# 2. Revenue Contribution vs Average Fare by Vehicle Tier
# ------------------------------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(9, 5.5), facecolor=BG_COLOR)
ax1.set_facecolor(CARD_COLOR)

vt_summary = comp.groupby('ride_type').agg(
    realized_revenue=('fare', 'sum'),
    avg_fare=('fare', 'mean')
).reindex(['Economy', 'Standard', 'Premium'])

x = np.arange(len(vt_summary))
width = 0.4

bars1 = ax1.bar(x - width/2, vt_summary['realized_revenue'], width, color=CYAN, label='Realized Revenue (PKR)', alpha=0.9)
ax1.set_ylabel("Realized Net Revenue (PKR)", color=CYAN, labelpad=10)
ax1.tick_params(axis='y', labelcolor=CYAN)
ax1.set_xticks(x)
ax1.set_xticklabels(vt_summary.index, color='white', fontweight='bold')

ax2 = ax1.twinx()
bars2 = ax2.bar(x + width/2, vt_summary['avg_fare'], width, color=AMBER, label='Average Ticket Size (PKR)', alpha=0.9)
ax2.set_ylabel("Average Fare per Journey (PKR)", color=AMBER, labelpad=10)
ax2.tick_params(axis='y', labelcolor=AMBER)
ax2.grid(False)

tot_rev = comp['fare'].sum()
for b in bars1:
    y = b.get_height()
    pct = (y / tot_rev) * 100
    ax1.text(b.get_x() + b.get_width()/2, y + 200, f"PKR {y:,.0f}\n({pct:.1f}%)", ha='center', color=CYAN, fontsize=8, fontweight='bold')

for b in bars2:
    y = b.get_height()
    ax2.text(b.get_x() + b.get_width()/2, y + 10, f"PKR {y:.0f}", ha='center', color=AMBER, fontsize=8, fontweight='bold')

plt.title("Vehicle Tier Yield Intelligence: Total Revenue vs. Average Ticket Size\n(Premium drives ₨558 avg ticket; Standard commands 38.8% total volume revenue)", color='white', pad=20, fontweight='bold')
save_fig(fig, "02_revenue_vs_avg_fare_by_tier.png")

# ------------------------------------------------------------------------------
# 3. Driver Performance vs Cohort Benchmark
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 5.5), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)

drv_summary = comp.groupby('driver_id')['fare'].sum().reset_index()
bench_rev = drv_summary['fare'].mean() # 3646.60
drv_summary['delta_vs_bench'] = drv_summary['fare'] - bench_rev
drv_summary = drv_summary.sort_values(by='delta_vs_bench', ascending=True)

colors = [EMERALD if x >= 0 else ROSE for x in drv_summary['delta_vs_bench']]
bars = ax.barh(drv_summary['driver_id'], drv_summary['delta_vs_bench'], color=colors, height=0.6)

ax.axvline(0, color='white', linestyle='-', linewidth=1.2)
ax.set_title("Driver Performance vs Cohort Revenue Benchmark (Baseline = PKR 3,646.60)\n(DRV-002: +PKR 837.40 vs DRV-007: -PKR 1,225.60)", color='white', pad=20, fontweight='bold')
ax.set_xlabel("Revenue Variance from Cohort Average (PKR)", color='#94a3b8', labelpad=10)
ax.grid(axis='x', linestyle=':', alpha=0.3, color=BORDER_COLOR)

for bar in bars:
    w = bar.get_width()
    offset = 25 if w >= 0 else -180
    ax.text(w + offset, bar.get_y() + bar.get_height()/2.0, f"{w:+,.1f}", ha='left', va='center', color='white', fontweight='bold', fontsize=8)

save_fig(fig, "03_driver_revenue_vs_benchmark.png")

# ------------------------------------------------------------------------------
# 4. What-If Scenario Analysis Model
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.5), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)

scenarios = [
    "Baseline Historical\n(85 Completed)",
    "Scenario A: +5%\nCompleted Rides",
    "Scenario A: +10%\nCompleted Rides",
    "Scenario A: +15%\nCompleted Rides",
    "Scenario B: +5%\nAverage Fare",
    "Scenario B: +10%\nAverage Fare",
    "Scenario C: 25%\nChurn Recovery",
    "Scenario C: 50%\nChurn Recovery"
]

revenues = [
    36466.0,
    38267.85,
    40112.60,
    41914.45,
    38289.30,
    40112.60,
    38090.00,
    39714.00
]

bar_colors = [INDIGO, CYAN, CYAN, CYAN, AMBER, AMBER, EMERALD, EMERALD]
bars = ax.bar(scenarios, revenues, color=bar_colors, width=0.6, alpha=0.9)

ax.set_ylim(32000, 44000)
ax.axhline(36466.0, color='white', linestyle='--', alpha=0.6, label='Baseline Actual (PKR 36,466)')
ax.set_ylabel("Projected Total Platform Revenue (PKR)", color='#94a3b8', labelpad=10)
ax.set_title("Executive What-If Scenario Analytics: Financial Impact Modeling\n(Hypothetical Volume Growth, Pricing Elasticity, and Churn Recovery)", color='white', pad=20, fontweight='bold')
ax.grid(axis='y', linestyle=':', alpha=0.3, color=BORDER_COLOR)

for bar in bars:
    y = bar.get_height()
    diff = y - 36466.0
    diff_text = f"+₨{diff:,.0f}" if diff > 0 else "Baseline"
    ax.text(bar.get_x() + bar.get_width()/2, y + 250, f"₨{y:,.0f}\n({diff_text})", ha='center', color='white', fontweight='bold', fontsize=8)

plt.xticks(rotation=15)
save_fig(fig, "04_what_if_scenario_modeling.png")

# ------------------------------------------------------------------------------
# 5. Customer Behavioral Segments Visual
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.5), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)

segs = ['Standard Daily\n(Commuters)', 'Premium Executive\n(High Yield)', 'Economy Utility\n(Short Hops)']
rev_shares = [38.76, 33.67, 27.57]
avg_fares = [441.75, 558.05, 324.29]
colors = [INDIGO, AMBER, CYAN]

bars = ax.bar(segs, rev_shares, color=colors, width=0.55, alpha=0.85)
ax.set_ylabel("Share of Total Realized Revenue (%)", color='#94a3b8', labelpad=10)
ax.set_title("Customer Behavioral Segmentation: Revenue Share & Mean Ticket Size\n(Standard: Volume anchor 38.8% | Premium: High value ₨558 ticket | Economy: Accessible)", color='white', pad=20, fontweight='bold')
ax.grid(axis='y', linestyle=':', alpha=0.3, color=BORDER_COLOR)

for i, bar in enumerate(bars):
    y = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, y + 0.8, f"{y:.1f}%\n(Avg: ₨{avg_fares[i]:.0f})", ha='center', color='white', fontweight='bold', fontsize=9)

save_fig(fig, "05_customer_behavioral_segments.png")

# ------------------------------------------------------------------------------
# 6. Payment Ecosystem Contribution
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5.5), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)

pm_rev = comp.groupby('payment_method')['fare'].sum().sort_values(ascending=False)
colors = [CYAN, INDIGO, EMERALD, AMBER]
wedges, texts, autotexts = ax.pie(
    pm_rev.values, 
    labels=pm_rev.index, 
    autopct='%1.1f%%',
    pctdistance=0.75,
    colors=colors,
    startangle=130,
    textprops={'color': 'white', 'fontsize': 10},
    wedgeprops=dict(width=0.45, edgecolor=BG_COLOR, linewidth=2)
)
for at in autotexts:
    at.set_color('#0f172a')
    at.set_weight('bold')

ax.set_title("Financial Settlement Channels: Digital (61.3%) vs Cash (38.7%)\n(Cash: ₨14,115 | Card: ₨10,801 | UPI: ₨8,181 | Wallet: ₨3,369)", color='white', pad=20, fontweight='bold')
save_fig(fig, "06_payment_ecosystem_contribution.png")

# ------------------------------------------------------------------------------
# 7. Day of Week Demand & Operational Risk
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_comp = df[df['ride_status'] == 'Completed']['day_name'].value_counts().reindex(days).fillna(0)
day_canc = df[df['ride_status'] == 'Cancelled']['day_name'].value_counts().reindex(days).fillna(0)

x = np.arange(len(days))
width = 0.55

b1 = ax.bar(x, day_comp, width, label='Completed Trips', color=CYAN, alpha=0.9)
b2 = ax.bar(x, day_canc, width, bottom=day_comp, label='Cancelled Trips (Churn)', color=ROSE, alpha=0.9)

ax.set_xticks(x)
ax.set_xticklabels(days, color='white', fontweight='bold')
ax.set_ylabel("Total Dispatched Demand", color='#94a3b8', labelpad=10)
ax.set_title("Temporal Volatility: Demand & Cancellation Risk by Weekday\n(Thursday commands peak 24 rides; Friday suffers 25% peak churn rate)", color='white', pad=20, fontweight='bold')
ax.legend(frameon=True, facecolor=CARD_COLOR, edgecolor=BORDER_COLOR, labelcolor='white')
ax.grid(axis='y', linestyle=':', alpha=0.3, color=BORDER_COLOR)

for i in range(len(days)):
    c_val = day_comp.iloc[i]
    can_val = day_canc.iloc[i]
    tot = c_val + can_val
    rate = (can_val / tot * 100) if tot > 0 else 0
    ax.text(i, tot + 0.4, f"{int(tot)}\n({rate:.0f}% churn)", ha='center', color='white', fontsize=8, fontweight='bold')

save_fig(fig, "07_weekday_demand_and_churn_risk.png")

# ------------------------------------------------------------------------------
# 8. Time-Intelligence Revenue Trajectory & Daily Volatility
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5), facecolor=BG_COLOR)
ax.set_facecolor(CARD_COLOR)

daily_rev = comp.groupby(comp['date'].dt.strftime('%b %d'))['fare'].sum().reindex(df['date'].dt.strftime('%b %d').unique())
x = range(len(daily_rev))

ax.plot(x, daily_rev.values, marker='o', color=CYAN, linewidth=2.5, label='Daily Realized Revenue (PKR)')
ax.fill_between(x, daily_rev.values, color=CYAN, alpha=0.15)
ax.axhline(daily_rev.mean(), color=AMBER, linestyle='--', label=f"10-Day Mean (PKR {daily_rev.mean():,.0f})")

ax.set_xticks(x)
ax.set_xticklabels(daily_rev.index, rotation=20, color='white')
ax.set_ylabel("Daily Net Revenue (PKR)", color='#94a3b8', labelpad=10)
ax.set_title("Time-Intelligence Revenue Run-Rate (Sep 01 - Sep 10, 2026)\n(Peak: Sep 05 at ₨5,411 | Trough: Sep 07 at ₨2,427)", color='white', pad=20, fontweight='bold')
ax.grid(True, linestyle=':', alpha=0.3, color=BORDER_COLOR)
ax.legend(frameon=True, facecolor=CARD_COLOR, edgecolor=BORDER_COLOR, labelcolor='white')

for i, txt in enumerate(daily_rev.values):
    ax.annotate(f"₨{txt:,.0f}", (i, txt), textcoords="offset points", xytext=(0, 8), ha='center', color=CYAN, fontweight='bold', fontsize=8)

save_fig(fig, "08_time_intelligence_revenue_runrate.png")

print("All 8 Week 5 Advanced Decision Visuals generated successfully!")
