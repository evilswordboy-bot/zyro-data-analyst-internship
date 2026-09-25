"""
========================================================================================
 ZYROO DATA ANALYTICS INTERNSHIP • WEEK 4
 Ride Analytics & Revenue Intelligence Platform
 Executive Streamlit Business Intelligence Dashboard (100% Offline & Interactive)
========================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="ZYROO • Ride Analytics & Revenue Intelligence",
    page_icon="🚕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Dark Executive Theme)
st.markdown("""
<style>
    .reportview-container {
        background: #080d1a;
    }
    .main {
        background-color: #080d1a;
        color: #f1f5f9;
    }
    .metric-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.75));
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }
    .metric-title {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        color: #94a3b8;
        letter-spacing: 0.05em;
    }
    .metric-value {
        font-size: 26px;
        font-weight: 800;
        color: #ffffff;
        font-family: monospace;
        margin: 6px 0;
    }
    .metric-sub {
        font-size: 11px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# DATA INGESTION & CACHING
# -----------------------------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv('data/rides_data_week3.csv')
    df['date'] = pd.to_datetime(df['date'])
    df['day_name'] = df['date'].dt.day_name()
    return df

df_raw = load_data()

# -----------------------------------------------------------------------------
# SIDEBAR FILTERS (Phase 9)
# -----------------------------------------------------------------------------
st.sidebar.markdown("### 🎛️ Executive Filters")

# Date range
dates = sorted(df_raw['date'].dt.date.unique())
selected_dates = st.sidebar.multiselect(
    "Observation Dates",
    options=dates,
    default=dates,
    format_func=lambda d: d.strftime('%b %d, %Y')
)

# Status
statuses = ["All"] + list(df_raw['ride_status'].unique())
selected_status = st.sidebar.selectbox("Fulfillment Status", statuses)

# Pickup location
locations = ["All"] + sorted(df_raw['pickup_location'].unique().tolist())
selected_location = st.sidebar.selectbox("Pickup Hub", locations)

# Ride type
ride_types = ["All"] + sorted(df_raw['ride_type'].unique().tolist())
selected_ride_type = st.sidebar.selectbox("Vehicle Tier", ride_types)

# Payment method
payments = ["All"] + sorted(df_raw['payment_method'].unique().tolist())
selected_payment = st.sidebar.selectbox("Settlement Channel", payments)

# Driver ID
drivers = ["All"] + sorted(df_raw['driver_id'].unique().tolist())
selected_driver = st.sidebar.selectbox("Driver ID", drivers)

# Apply Filter Logic
df_filtered = df_raw[df_raw['date'].dt.date.isin(selected_dates)]
if selected_status != "All":
    df_filtered = df_filtered[df_filtered['ride_status'] == selected_status]
if selected_location != "All":
    df_filtered = df_filtered[df_filtered['pickup_location'] == selected_location]
if selected_ride_type != "All":
    df_filtered = df_filtered[df_filtered['ride_type'] == selected_ride_type]
if selected_payment != "All":
    df_filtered = df_filtered[df_filtered['payment_method'] == selected_payment]
if selected_driver != "All":
    df_filtered = df_filtered[df_filtered['driver_id'] == selected_driver]

st.sidebar.markdown(f"**Filtered Records:** `{len(df_filtered)} / {len(df_raw)}`")

# -----------------------------------------------------------------------------
# HEADER SECTION
# -----------------------------------------------------------------------------
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.title("🚕 ZYROO • Ride Analytics & Revenue Intelligence")
    st.caption("Week 4 • Streamlit Business Intelligence Platform | Offline Enabled")

with col_h2:
    st.markdown("<br>", unsafe_allow_html=True)
    csv_data = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Export Filtered CSV",
        data=csv_data,
        file_name="zyroo_filtered_rides.csv",
        mime="text/csv"
    )

st.markdown("---")

# -----------------------------------------------------------------------------
# PHASE 4: KPI SECTION
# -----------------------------------------------------------------------------
total_rides = len(df_filtered)
comp_rides = (df_filtered['ride_status'] == 'Completed').sum()
canc_rides = (df_filtered['ride_status'] == 'Cancelled').sum()

comp_df = df_filtered[df_filtered['ride_status'] == 'Completed']
total_rev = comp_df['fare'].sum() if len(comp_df) > 0 else 0
avg_fare = comp_df['fare'].mean() if len(comp_df) > 0 else 0
crate = (comp_rides / total_rides * 100) if total_rides > 0 else 0
canc_rate = (canc_rides / total_rides * 100) if total_rides > 0 else 0
avg_rating = comp_df['rating'].dropna().mean() if len(comp_df['rating'].dropna()) > 0 else 0
avg_dist = comp_df['distance_km'].mean() if len(comp_df) > 0 else 0

k1, k2, k3, k4, k5, k6, k7, k8 = st.columns(8)

with k1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Total Rides</div>
        <div class="metric-value">{total_rides}</div>
        <div class="metric-sub" style="color: #38bdf8;">Gross Demand</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Completed</div>
        <div class="metric-value" style="color: #34d399;">{comp_rides}</div>
        <div class="metric-sub" style="color: #34d399;">{crate:.1f}% Fulfill</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Cancelled</div>
        <div class="metric-value" style="color: #f87171;">{canc_rides}</div>
        <div class="metric-sub" style="color: #f87171;">{canc_rate:.1f}% Churn</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Revenue</div>
        <div class="metric-value" style="color: #38bdf8;">₨{total_rev:,.0f}</div>
        <div class="metric-sub" style="color: #38bdf8;">Realized Cash</div>
    </div>
    """, unsafe_allow_html=True)

with k5:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Avg Ticket</div>
        <div class="metric-value" style="color: #fbbf24;">₨{avg_fare:.1f}</div>
        <div class="metric-sub" style="color: #fbbf24;">Per Completed</div>
    </div>
    """, unsafe_allow_html=True)

with k6:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Completion</div>
        <div class="metric-value" style="color: #34d399;">{crate:.1f}%</div>
        <div class="metric-sub" style="color: #34d399;">Target &ge; 85%</div>
    </div>
    """, unsafe_allow_html=True)

with k7:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Avg Rating</div>
        <div class="metric-value" style="color: #facc15;">{avg_rating:.2f}★</div>
        <div class="metric-sub" style="color: #facc15;">Customer CSAT</div>
    </div>
    """, unsafe_allow_html=True)

with k8:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Avg Distance</div>
        <div class="metric-value" style="color: #818cf8;">{avg_dist:.1f}k</div>
        <div class="metric-sub" style="color: #818cf8;">Route Length</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# PHASE 5: RIDE DEMAND & GEOGRAPHIC ANALYSIS
# -----------------------------------------------------------------------------
st.subheader("📈 Phase 5 • Ride Demand & Geographic Distribution")

c1, c2, c3 = st.columns(3)

with c1:
    daily_rides = df_filtered.groupby(df_filtered['date'].dt.strftime('%b %d')).size().reset_index(name='count')
    fig1 = px.line(
        daily_rides, x='date', y='count',
        title="Rides by Date (Demand Trend)",
        markers=True,
        color_discrete_sequence=['#38bdf8']
    )
    fig1.update_layout(template="plotly_dark", height=300, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    order_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_counts = df_filtered['day_name'].value_counts().reindex(order_days).fillna(0).reset_index()
    day_counts.columns = ['Day', 'Rides']
    fig2 = px.bar(
        day_counts, x='Day', y='Rides',
        title="Rides by Weekday (Demand Comparison)",
        color='Rides',
        color_continuous_scale='Blues'
    )
    fig2.update_layout(template="plotly_dark", height=300, margin=dict(l=20, r=20, t=40, b=20), coloraxis_showscale=False)
    st.plotly_chart(fig2, use_container_width=True)

with c3:
    pickups = df_filtered['pickup_location'].value_counts().reset_index()
    pickups.columns = ['Hub', 'Bookings']
    fig3 = px.bar(
        pickups, x='Bookings', y='Hub', orientation='h',
        title="Top Pickup Hubs (Origin Volume)",
        color='Bookings',
        color_continuous_scale='Viridis'
    )
    fig3.update_layout(template="plotly_dark", height=300, margin=dict(l=20, r=20, t=40, b=20), coloraxis_showscale=False)
    st.plotly_chart(fig3, use_container_width=True)

# -----------------------------------------------------------------------------
# PHASE 6: REVENUE INTELLIGENCE
# -----------------------------------------------------------------------------
st.subheader("💰 Phase 6 • Financial & Revenue Intelligence")

r1, r2, r3 = st.columns(3)

with r1:
    pay_rev = comp_df.groupby('payment_method')['fare'].sum().reset_index()
    fig4 = px.pie(
        pay_rev, values='fare', names='payment_method',
        title="Revenue by Payment Channel",
        hole=0.45,
        color_discrete_sequence=['#38bdf8', '#818cf8', '#34d399', '#fbbf24']
    )
    fig4.update_layout(template="plotly_dark", height=300, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig4, use_container_width=True)

with r2:
    rt_summary = comp_df.groupby('ride_type').agg(
        Total_Revenue=('fare', 'sum'),
        Avg_Fare=('fare', 'mean')
    ).reset_index()
    fig5 = px.bar(
        rt_summary, x='ride_type', y='Total_Revenue',
        title="Revenue by Vehicle Tier (PKR)",
        color='ride_type',
        color_discrete_sequence=['#34d399', '#fbbf24', '#38bdf8']
    )
    fig5.update_layout(template="plotly_dark", height=300, margin=dict(l=20, r=20, t=40, b=20), showlegend=False)
    st.plotly_chart(fig5, use_container_width=True)

with r3:
    loc_rev = comp_df.groupby('pickup_location')['fare'].sum().reset_index()
    loc_rev = loc_rev.sort_values(by='fare', ascending=True)
    fig6 = px.bar(
        loc_rev, x='fare', y='pickup_location', orientation='h',
        title="Realized Revenue by Origin Hub (PKR)",
        color='fare',
        color_continuous_scale='Teal'
    )
    fig6.update_layout(template="plotly_dark", height=300, margin=dict(l=20, r=20, t=40, b=20), coloraxis_showscale=False)
    st.plotly_chart(fig6, use_container_width=True)

# -----------------------------------------------------------------------------
# PHASE 8: DRIVER PERFORMANCE TABLE
# -----------------------------------------------------------------------------
st.subheader("🚗 Phase 8 • Driver Performance League Table")

drv_total = df_filtered.groupby('driver_id').size().reset_index(name='Total_Rides')
drv_comp = df_filtered[df_filtered['ride_status'] == 'Completed'].groupby('driver_id').size().reset_index(name='Completed')
drv_canc = df_filtered[df_filtered['ride_status'] == 'Cancelled'].groupby('driver_id').size().reset_index(name='Cancelled')

drv_rev = comp_df.groupby('driver_id').agg(
    Revenue=('fare', 'sum'),
    Rating=('rating', 'mean'),
    Avg_Distance=('distance_km', 'mean')
).reset_index()

m1 = pd.merge(drv_total, drv_comp, on='driver_id', how='left').fillna(0)
m2 = pd.merge(m1, drv_canc, on='driver_id', how='left').fillna(0)
drv_table = pd.merge(m2, drv_rev, on='driver_id', how='left').fillna(0)

drv_table['Completion_Rate'] = (drv_table['Completed'] / drv_table['Total_Rides'] * 100).round(1).astype(str) + '%'
drv_table['Revenue_PKR'] = drv_table['Revenue'].map('₨{:,.2f}'.format)
drv_table['Rating_Stars'] = drv_table['Rating'].map('{:.2f} ★'.format)
drv_table['Distance_KM'] = drv_table['Avg_Distance'].map('{:.1f} km'.format)

display_table = drv_table[['driver_id', 'Total_Rides', 'Completed', 'Cancelled', 'Revenue_PKR', 'Rating_Stars', 'Distance_KM', 'Completion_Rate']].copy()
display_table.columns = ['Driver ID', 'Total Rides', 'Completed', 'Cancelled', 'Realized Revenue', 'Avg Rating', 'Avg Distance', 'Completion Rate']

st.dataframe(display_table, use_container_width=True, hide_index=True)

# -----------------------------------------------------------------------------
# PHASE 12 & 13: STRATEGIC INSIGHTS & RECOMMENDATIONS
# -----------------------------------------------------------------------------
st.markdown("---")
i_col, r_col = st.columns(2)

with i_col:
    st.subheader("💡 5 Data-Driven Business Insights")
    st.info("**1. DHA Geographic Dominance:** DHA drives 38.0% of total bookings and 42.2% of total platform revenue (₨15,388).")
    st.info("**2. Revenue Mirage vs Dependability:** DRV-002 earned top revenue (₨4,484), but DRV-001, 004, 010 delivered 100% completion (>₨4,000).")
    st.warning("**3. Gulberg Operational Leakage:** Gulberg booked 20 rides but incurred a 30.0% cancellation rate and lowest fare (₨397.07).")
    st.success("**4. Premium Tier Ticket Yield:** Premium rides yield ₨558.05 (+30.3% over Standard) across similar travel distances.")
    st.info("**5. Concentrated Cancellation Risk:** 46.7% of all platform cancellations were caused by just two drivers (DRV-005 and DRV-007).")

with r_col:
    st.subheader("🚀 3 Actionable Business Recommendations")
    st.success("**1. Geofenced Fulfillment Boost for Gulberg:** Deploy a ₨50 - ₨75 driver incentive for completed Gulberg pickups during rush hours.")
    st.success("**2. Star Partner Priority Dispatch:** Grant priority dispatch for Premium rides to drivers with &ge;90% completion and &ge;4.3 ★ rating.")
    st.success("**3. 5% Instant Digital Discount:** Incentivize Card, UPI, and Wallet settlements to drive cash volume below 20%.")
    st.caption("📌 **Technical Telemetry Audit:** Schema captures 11 core operational fields. In strict adherence to internship standards, customer behavior is evaluated via platform trip velocity rather than synthetic IDs.")
