# ==============================================================================
# ZYROO DATA ANALYTICS INTERNSHIP • WEEK 5
# Advanced Business Intelligence Dashboard HTML Generator
# ==============================================================================

import pandas as pd
import json

df = pd.read_csv('data/rides_data_week3.csv')
df['rating'] = df['rating'].where(pd.notnull(df['rating']), None)
records = df.to_dict(orient='records')

html_template = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ZYROO • Week 5 Advanced Decision Analytics & Business Intelligence System</title>
  <script src="tailwindcss.min.js"></script>
  <script>
    if (!window.tailwind) {{
      document.write('<script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"><\\/script>');
    }}
  </script>
  <style>
    :root {{
      --bg-primary: #080d1a;
      --surface-1: #0f172a;
      --border-subtle: rgba(56, 189, 248, 0.12);
      --border-accent: rgba(0, 229, 255, 0.35);
    }}
    body {{
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg-primary);
      color: #f1f5f9;
      background-image: 
        radial-gradient(at 10% 10%, rgba(14, 165, 233, 0.08) 0px, transparent 50%),
        radial-gradient(at 90% 90%, rgba(99, 102, 241, 0.06) 0px, transparent 50%);
      background-attachment: fixed;
    }}
    .font-mono-num {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-variant-numeric: tabular-nums;
    }}
    .acrylic-card {{
      background: linear-gradient(135deg, rgba(15, 23, 42, 0.94), rgba(15, 23, 42, 0.78));
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-subtle);
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
      transition: all 0.25s ease;
    }}
    .acrylic-card:hover {{
      border-color: var(--border-accent);
      box-shadow: 0 12px 35px -8px rgba(0, 229, 255, 0.14);
    }}
    .nav-btn.active {{
      background-color: #38bdf8;
      color: #080d1a;
      font-weight: 800;
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
    }}
  </style>
</head>
<body class="min-h-screen p-4 sm:p-6 lg:p-8 antialiased">
  <div class="max-w-[1700px] mx-auto space-y-6">

    <!-- EXECUTIVE HEADER -->
    <header class="acrylic-card rounded-2xl p-4 sm:p-5 flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div class="flex items-center gap-4">
        <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-cyan-400 to-blue-600 flex items-center justify-center text-slate-950 font-black text-xl tracking-tighter shadow-lg shadow-cyan-500/20">
          ZY
        </div>
        <div>
          <div class="flex items-center gap-2 flex-wrap">
            <span class="text-xs font-black uppercase tracking-widest text-cyan-400 px-2.5 py-0.5 rounded-md bg-cyan-500/10 border border-cyan-500/20">ZYROO Intelligence</span>
            <span class="text-xs text-slate-400">Week 5 • Advanced Business Intelligence & Decision Support</span>
            <span class="inline-flex items-center gap-1.5 px-2 py-0.5 text-[11px] font-semibold text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 rounded-full">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
              Decision Engine Active
            </span>
          </div>
          <h1 class="text-xl sm:text-2xl font-extrabold tracking-tight text-white mt-1">
            Ride Analytics & <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-300 to-indigo-400">Decision Analytics System</span>
          </h1>
        </div>
      </div>

      <div class="flex items-center gap-3">
        <button onclick="downloadCSV()" class="px-3.5 py-2 text-xs font-semibold rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition flex items-center gap-2">
          Export Telemetry CSV
        </button>
        <button onclick="resetAllFilters()" class="px-3.5 py-2 text-xs font-semibold rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 transition font-bold shadow-lg shadow-cyan-500/25">
          Reset Slicers
        </button>
      </div>
    </header>

    <!-- MULTI-PAGE NAVIGATION TABS -->
    <nav class="flex items-center gap-2 overflow-x-auto pb-1 border-b border-slate-800 text-xs font-bold">
      <button onclick="switchTab('tab-exec')" id="btn-tab-exec" class="nav-btn active px-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white transition">
        📊 Page 1: Executive Overview
      </button>
      <button onclick="switchTab('tab-rev')" id="btn-tab-rev" class="nav-btn px-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white transition">
        💰 Page 2: Revenue Intelligence
      </button>
      <button onclick="switchTab('tab-seg')" id="btn-tab-seg" class="nav-btn px-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white transition">
        👥 Page 3: Customer Segmentation
      </button>
      <button onclick="switchTab('tab-drv')" id="btn-tab-drv" class="nav-btn px-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white transition">
        🚗 Page 4: Driver Intelligence
      </button>
      <button onclick="switchTab('tab-canc')" id="btn-tab-canc" class="nav-btn px-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white transition">
        ⚠️ Page 5: Cancellation & Churn
      </button>
      <button onclick="switchTab('tab-whatif')" id="btn-tab-whatif" class="nav-btn px-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white transition">
        🔮 Page 6: What-If Scenarios
      </button>
      <button onclick="switchTab('tab-insights')" id="btn-tab-insights" class="nav-btn px-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white transition">
        💡 Page 7: 8+ Insights & 5+ Actions
      </button>
    </nav>

    <!-- EXECUTIVE SLICERS (Active Across All Pages) -->
    <section class="acrylic-card rounded-2xl p-4 space-y-3">
      <div class="flex items-center justify-between">
        <span class="text-xs font-bold uppercase tracking-wider text-slate-300">Global Executive Slicers (Dynamic Cross-Filtering)</span>
        <span class="text-xs text-slate-400">Active Telemetry: <strong class="text-cyan-400 font-mono-num" id="slicer-count">100 / 100</strong></span>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3">
        <div>
          <label class="block text-[11px] font-semibold text-slate-400 mb-1">📅 Observation Date</label>
          <select id="filter-date" onchange="applyFilters()" class="w-full text-xs rounded-xl bg-slate-900 border border-slate-700/80 text-slate-200 px-3 py-2 outline-none focus:border-cyan-400">
            <option value="ALL">All Dates (Sep 01 - Sep 10)</option>
          </select>
        </div>
        <div>
          <label class="block text-[11px] font-semibold text-slate-400 mb-1">🚦 Fulfillment Status</label>
          <select id="filter-status" onchange="applyFilters()" class="w-full text-xs rounded-xl bg-slate-900 border border-slate-700/80 text-slate-200 px-3 py-2 outline-none focus:border-cyan-400">
            <option value="ALL">All Statuses</option>
            <option value="Completed">Completed Only</option>
            <option value="Cancelled">Cancelled Only</option>
          </select>
        </div>
        <div>
          <label class="block text-[11px] font-semibold text-slate-400 mb-1">📍 Pickup Hub</label>
          <select id="filter-location" onchange="applyFilters()" class="w-full text-xs rounded-xl bg-slate-900 border border-slate-700/80 text-slate-200 px-3 py-2 outline-none focus:border-cyan-400">
            <option value="ALL">All Pickup Locations</option>
          </select>
        </div>
        <div>
          <label class="block text-[11px] font-semibold text-slate-400 mb-1">🚗 Vehicle Tier</label>
          <select id="filter-ride-type" onchange="applyFilters()" class="w-full text-xs rounded-xl bg-slate-900 border border-slate-700/80 text-slate-200 px-3 py-2 outline-none focus:border-cyan-400">
            <option value="ALL">All Vehicle Tiers</option>
          </select>
        </div>
        <div>
          <label class="block text-[11px] font-semibold text-slate-400 mb-1">💳 Settlement Channel</label>
          <select id="filter-payment" onchange="applyFilters()" class="w-full text-xs rounded-xl bg-slate-900 border border-slate-700/80 text-slate-200 px-3 py-2 outline-none focus:border-cyan-400">
            <option value="ALL">All Payment Methods</option>
          </select>
        </div>
        <div>
          <label class="block text-[11px] font-semibold text-slate-400 mb-1">👤 Driver ID</label>
          <select id="filter-driver" onchange="applyFilters()" class="w-full text-xs rounded-xl bg-slate-900 border border-slate-700/80 text-slate-200 px-3 py-2 outline-none focus:border-cyan-400">
            <option value="ALL">All 10 Drivers</option>
          </select>
        </div>
      </div>
    </section>

    <!-- CORE EXECUTIVE KPI SUMMARY ROW -->
    <section class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3">
      <div class="acrylic-card rounded-2xl p-3.5 flex flex-col justify-between">
        <span class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Gross Demand</span>
        <div class="my-1.5 text-2xl font-extrabold text-white font-mono-num" id="kpi-rides">100</div>
        <span class="text-[10px] text-cyan-400 font-semibold">Total Dispatched</span>
      </div>
      <div class="acrylic-card rounded-2xl p-3.5 flex flex-col justify-between">
        <span class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Fulfilled Trips</span>
        <div class="my-1.5 text-2xl font-extrabold text-emerald-400 font-mono-num" id="kpi-completed">85</div>
        <span class="text-[10px] text-emerald-400 font-semibold" id="kpi-crate-sub">85.0% Fulfill Rate</span>
      </div>
      <div class="acrylic-card rounded-2xl p-3.5 flex flex-col justify-between">
        <span class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Unrealized Churn</span>
        <div class="my-1.5 text-2xl font-extrabold text-rose-400 font-mono-num" id="kpi-cancelled">15</div>
        <span class="text-[10px] text-rose-400 font-semibold" id="kpi-canc-sub">15.0% Churn Rate</span>
      </div>
      <div class="acrylic-card rounded-2xl p-3.5 flex flex-col justify-between">
        <span class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Realized Revenue</span>
        <div class="my-1.5 text-xl font-extrabold text-cyan-300 font-mono-num" id="kpi-revenue">₨36,466</div>
        <span class="text-[10px] text-cyan-400 font-semibold">Cash & Digital Inflow</span>
      </div>
      <div class="acrylic-card rounded-2xl p-3.5 flex flex-col justify-between">
        <span class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Rev / Completed</span>
        <div class="my-1.5 text-xl font-extrabold text-amber-400 font-mono-num" id="kpi-avg-fare">₨429.01</div>
        <span class="text-[10px] text-amber-400 font-semibold">Avg Ticket Size</span>
      </div>
      <div class="acrylic-card rounded-2xl p-3.5 flex flex-col justify-between">
        <span class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Gross Booking Val</span>
        <div class="my-1.5 text-xl font-extrabold text-purple-300 font-mono-num" id="kpi-gbv">₨42,962</div>
        <span class="text-[10px] text-purple-400 font-semibold">Total Demanded</span>
      </div>
      <div class="acrylic-card rounded-2xl p-3.5 flex flex-col justify-between">
        <span class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Customer CSAT</span>
        <div class="my-1.5 text-2xl font-extrabold text-yellow-400 font-mono-num" id="kpi-rating">4.27 ★</div>
        <span class="text-[10px] text-yellow-400 font-semibold">Completed Reviews</span>
      </div>
      <div class="acrylic-card rounded-2xl p-3.5 flex flex-col justify-between">
        <span class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Mean Route Run</span>
        <div class="my-1.5 text-2xl font-extrabold text-indigo-300 font-mono-num" id="kpi-distance">13.7 km</div>
        <span class="text-[10px] text-indigo-400 font-semibold">Completed Avg Dist</span>
      </div>
    </section>

    <!-- ===================================================================== -->
    <!-- TAB 1: EXECUTIVE OVERVIEW -->
    <!-- ===================================================================== -->
    <div id="tab-exec" class="tab-content space-y-5">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-5">
        <div class="acrylic-card rounded-2xl p-4">
          <h3 class="text-xs font-bold text-white mb-2">Demand & Fulfillment Over Time (Sep 01 - 10)</h3>
          <div class="h-56" id="chart-exec-date"></div>
        </div>
        <div class="acrylic-card rounded-2xl p-4">
          <h3 class="text-xs font-bold text-white mb-2">Weekday Demand & Churn Volatility</h3>
          <div class="h-56" id="chart-exec-weekday"></div>
        </div>
        <div class="acrylic-card rounded-2xl p-4">
          <h3 class="text-xs font-bold text-white mb-2">Top Origin Hubs vs Drop-off Inflow</h3>
          <div class="h-56" id="chart-exec-loc"></div>
        </div>
      </div>
    </div>

    <!-- ===================================================================== -->
    <!-- TAB 2: REVENUE INTELLIGENCE -->
    <!-- ===================================================================== -->
    <div id="tab-rev" class="tab-content hidden space-y-5">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-5">
        <div class="acrylic-card rounded-2xl p-4">
          <h3 class="text-xs font-bold text-white mb-2">Settlement Channel Revenue (Digital vs Cash)</h3>
          <div class="h-56 flex items-center justify-center" id="chart-rev-pay"></div>
        </div>
        <div class="acrylic-card rounded-2xl p-4">
          <h3 class="text-xs font-bold text-white mb-2">Revenue & Avg Fare by Vehicle Tier</h3>
          <div class="h-56" id="chart-rev-tier"></div>
        </div>
        <div class="acrylic-card rounded-2xl p-4">
          <h3 class="text-xs font-bold text-white mb-2">Geographic Realized Revenue by Origin Hub</h3>
          <div class="h-56" id="chart-rev-loc"></div>
        </div>
      </div>
    </div>

    <!-- ===================================================================== -->
    <!-- TAB 3: CUSTOMER SEGMENTATION -->
    <!-- ===================================================================== -->
    <div id="tab-seg" class="tab-content hidden space-y-5">
      <div class="acrylic-card rounded-2xl p-5 space-y-4">
        <div>
          <h3 class="text-sm font-bold text-white">Customer Behavioral Segmentation & Value Contribution</h3>
          <p class="text-xs text-slate-400">Classified by Passenger Value, Service Tier, and Journey Dynamics</p>
        </div>
        <div class="overflow-x-auto rounded-xl border border-slate-800">
          <table class="w-full text-left text-xs whitespace-nowrap">
            <thead class="bg-slate-900 text-slate-300 font-bold uppercase text-[10px] border-b border-slate-800">
              <tr>
                <th class="p-3">Behavioral Segment</th>
                <th class="p-3 text-center">Bookings</th>
                <th class="p-3 text-center">Completed</th>
                <th class="p-3 text-center">Churn %</th>
                <th class="p-3 text-right">Realized Revenue</th>
                <th class="p-3 text-right">Revenue Share</th>
                <th class="p-3 text-right">Avg Ticket Size</th>
                <th class="p-3 text-right">Avg Distance</th>
                <th class="p-3 text-center">Top Channel</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800 font-mono-num text-slate-200">
              <tr class="hover:bg-slate-800/40">
                <td class="p-3 font-bold text-cyan-400 font-sans">Standard Daily Commuters</td>
                <td class="p-3 text-center">39</td>
                <td class="p-3 text-center text-emerald-400 font-bold">32</td>
                <td class="p-3 text-center text-rose-400">17.9%</td>
                <td class="p-3 text-right font-bold text-white">₨14,136.00</td>
                <td class="p-3 text-right text-cyan-400 font-bold">38.76%</td>
                <td class="p-3 text-right text-amber-400">₨441.75</td>
                <td class="p-3 text-right">14.2 km</td>
                <td class="p-3 text-center font-sans">UPI / Cash</td>
              </tr>
              <tr class="hover:bg-slate-800/40">
                <td class="p-3 font-bold text-amber-400 font-sans">Premium Executive Riders</td>
                <td class="p-3 text-center">26</td>
                <td class="p-3 text-center text-emerald-400 font-bold">22</td>
                <td class="p-3 text-center text-rose-400">15.4%</td>
                <td class="p-3 text-right font-bold text-white">₨12,277.00</td>
                <td class="p-3 text-right text-amber-400 font-bold">33.67%</td>
                <td class="p-3 text-right text-amber-300 font-bold">₨558.05</td>
                <td class="p-3 text-right">19.5 km</td>
                <td class="p-3 text-center font-sans">Cash / Card</td>
              </tr>
              <tr class="hover:bg-slate-800/40">
                <td class="p-3 font-bold text-emerald-400 font-sans">Economy Short-Hop Riders</td>
                <td class="p-3 text-center">35</td>
                <td class="p-3 text-center text-emerald-400 font-bold">31</td>
                <td class="p-3 text-center text-emerald-400">11.4%</td>
                <td class="p-3 text-right font-bold text-white">₨10,053.00</td>
                <td class="p-3 text-right text-emerald-400 font-bold">27.57%</td>
                <td class="p-3 text-right text-slate-300">₨324.29</td>
                <td class="p-3 text-right">9.1 km</td>
                <td class="p-3 text-center font-sans">Card / UPI</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- ===================================================================== -->
    <!-- TAB 4: DRIVER INTELLIGENCE & BENCHMARKING -->
    <!-- ===================================================================== -->
    <div id="tab-drv" class="tab-content hidden space-y-5">
      <div class="acrylic-card rounded-2xl p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <h3 class="text-sm font-bold text-white">Driver Performance League Table & Benchmark Variance</h3>
            <p class="text-xs text-slate-400">Cohort Benchmarks: Revenue = ₨3,646.60 | Completion Rate = 85.0% | Rating = 4.27 ★</p>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs text-slate-400">Sort By:</span>
            <select id="driver-sort-by" onchange="renderDriverTable()" class="text-xs rounded-xl bg-slate-900 border border-slate-700/80 text-cyan-400 px-3 py-1.5 outline-none font-bold">
              <option value="composite">Composite Score (Weighted)</option>
              <option value="revenue">Total Revenue (PKR)</option>
              <option value="completed">Completed Rides</option>
              <option value="crate">Completion Rate (%)</option>
              <option value="rating">Average Rating</option>
            </select>
          </div>
        </div>

        <div class="overflow-x-auto rounded-xl border border-slate-800">
          <table class="w-full text-left text-xs whitespace-nowrap">
            <thead class="bg-slate-900 text-slate-300 font-bold uppercase text-[10px] border-b border-slate-800">
              <tr>
                <th class="p-3">Rank</th>
                <th class="p-3">Driver ID</th>
                <th class="p-3 text-center">Total</th>
                <th class="p-3 text-center">Completed</th>
                <th class="p-3 text-center">Cancelled</th>
                <th class="p-3 text-right">Realized Revenue</th>
                <th class="p-3 text-right">Rev vs Bench</th>
                <th class="p-3 text-center">C-Rate</th>
                <th class="p-3 text-center">C-Rate vs Bench</th>
                <th class="p-3 text-right">Rating</th>
                <th class="p-3 text-right">Composite Score</th>
                <th class="p-3 text-center">Status Tier</th>
              </tr>
            </thead>
            <tbody id="driver-tbody" class="divide-y divide-slate-800 font-mono-num text-slate-200">
              <!-- Dynamically rendered -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- ===================================================================== -->
    <!-- TAB 5: CANCELLATION & CHURN INTELLIGENCE -->
    <!-- ===================================================================== -->
    <div id="tab-canc" class="tab-content hidden space-y-5">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
        <div class="acrylic-card rounded-2xl p-4">
          <h3 class="text-xs font-bold text-white mb-2">Location Demand vs Cancellation Churn Rate</h3>
          <div class="h-64" id="chart-canc-loc"></div>
        </div>
        <div class="acrylic-card rounded-2xl p-4">
          <h3 class="text-xs font-bold text-white mb-2">Weekday Churn Volatility & Leakage</h3>
          <div class="h-64" id="chart-canc-day"></div>
        </div>
      </div>
      <div class="acrylic-card rounded-2xl p-4 space-y-2">
        <h4 class="text-xs font-bold text-cyan-300 uppercase">Operational Finding: Gulberg Demand vs Churn Anomaly</h4>
        <p class="text-xs text-slate-300 leading-relaxed">
          Gulberg represents the second highest passenger origination hub (20 ride requests), but suffers a severe <strong>30.0% cancellation rate (6 cancelled rides)</strong> and the lowest realized average fare (₨397.07). This indicates that driver cancellation is associated with traffic congestion and lower fare yields in this corridor.
        </p>
      </div>
    </div>

    <!-- ===================================================================== -->
    <!-- TAB 6: WHAT-IF SCENARIO ANALYTICS -->
    <!-- ===================================================================== -->
    <div id="tab-whatif" class="tab-content hidden space-y-5">
      <div class="acrylic-card rounded-2xl p-5 space-y-4">
        <div>
          <h3 class="text-sm font-bold text-white">What-If Financial Simulation Engine</h3>
          <p class="text-xs text-slate-400">Baseline Actuals: 85 Completed Trips | PKR 36,466 Realized Revenue | 15% Churn Rate</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <!-- Scenario A -->
          <div class="p-4 rounded-xl bg-slate-900/90 border border-cyan-500/30 space-y-3">
            <span class="text-xs font-bold text-cyan-400 uppercase">Scenario A: Completed Rides Growth</span>
            <label class="block text-[11px] text-slate-400">Growth Parameter: <strong id="val-scen-a" class="text-cyan-300">+10%</strong></label>
            <input type="range" min="0" max="30" step="5" value="10" id="slider-scen-a" oninput="runScenarios()" class="w-full accent-cyan-400">
            <div class="pt-2 border-t border-slate-800 space-y-1 text-xs font-mono-num">
              <div class="flex justify-between"><span class="text-slate-400">New Trips:</span><span id="res-trips-a" class="text-white font-bold">93.5</span></div>
              <div class="flex justify-between"><span class="text-slate-400">Projected Rev:</span><span id="res-rev-a" class="text-cyan-300 font-bold">₨40,113</span></div>
              <div class="flex justify-between"><span class="text-slate-400">Revenue Delta:</span><span id="res-delta-a" class="text-emerald-400 font-bold">+₨3,647</span></div>
            </div>
          </div>

          <!-- Scenario B -->
          <div class="p-4 rounded-xl bg-slate-900/90 border border-amber-500/30 space-y-3">
            <span class="text-xs font-bold text-amber-400 uppercase">Scenario B: Pricing Yield Shift</span>
            <label class="block text-[11px] text-slate-400">Fare Shift Parameter: <strong id="val-scen-b" class="text-amber-300">+5%</strong></label>
            <input type="range" min="-10" max="20" step="5" value="5" id="slider-scen-b" oninput="runScenarios()" class="w-full accent-amber-400">
            <div class="pt-2 border-t border-slate-800 space-y-1 text-xs font-mono-num">
              <div class="flex justify-between"><span class="text-slate-400">New Avg Fare:</span><span id="res-fare-b" class="text-white font-bold">₨450.46</span></div>
              <div class="flex justify-between"><span class="text-slate-400">Projected Rev:</span><span id="res-rev-b" class="text-amber-300 font-bold">₨38,289</span></div>
              <div class="flex justify-between"><span class="text-slate-400">Revenue Delta:</span><span id="res-delta-b" class="text-emerald-400 font-bold">+₨1,823</span></div>
            </div>
          </div>

          <!-- Scenario C -->
          <div class="p-4 rounded-xl bg-slate-900/90 border border-emerald-500/30 space-y-3">
            <span class="text-xs font-bold text-emerald-400 uppercase">Scenario C: Churn Recovery</span>
            <label class="block text-[11px] text-slate-400">Recovery Parameter: <strong id="val-scen-c" class="text-emerald-300">50% Recovered</strong></label>
            <input type="range" min="0" max="100" step="25" value="50" id="slider-scen-c" oninput="runScenarios()" class="w-full accent-emerald-400">
            <div class="pt-2 border-t border-slate-800 space-y-1 text-xs font-mono-num">
              <div class="flex justify-between"><span class="text-slate-400">Recovered Cash:</span><span id="res-rec-c" class="text-emerald-300 font-bold">₨3,248</span></div>
              <div class="flex justify-between"><span class="text-slate-400">Projected Rev:</span><span id="res-rev-c" class="text-white font-bold">₨39,714</span></div>
              <div class="flex justify-between"><span class="text-slate-400">Growth Impact:</span><span id="res-pct-c" class="text-emerald-400 font-bold">+8.91%</span></div>
            </div>
          </div>
        </div>

        <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-400">
          <strong class="text-slate-300">Methodology & Assumptions Notice:</strong> What-If calculations represent hypothetical projections based on historical 10-day elasticity. Revenue projections hold other operational variables constant.
        </div>
      </div>
    </div>

    <!-- ===================================================================== -->
    <!-- TAB 7: 8+ INSIGHTS & 5+ RECOMMENDATIONS -->
    <!-- ===================================================================== -->
    <div id="tab-insights" class="tab-content hidden space-y-5">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
        <!-- 8+ Insights -->
        <div class="acrylic-card rounded-2xl p-5 space-y-3">
          <h3 class="text-sm font-bold text-white flex items-center gap-2">
            <span class="text-cyan-400">💡</span> 8 Evidence-Based Business Insights
          </h3>
          <div class="space-y-2.5 text-xs text-slate-300 leading-relaxed">
            <div class="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800">
              <strong class="text-cyan-300 block">1. Geographic Revenue Concentration (DHA)</strong>
              <strong>Finding:</strong> DHA generated 35 completed rides and <strong>42.20% (₨15,388.00)</strong> of total realized revenue with an above-average ticket size of ₨439.66 and low 7.89% cancellation rate.<br>
              <strong>Meaning:</strong> DHA is the financial anchor of the platform; preserving driver liquidity here is critical.
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800">
              <strong class="text-rose-300 block">2. Gulberg Churn & Revenue Disincentive</strong>
              <strong>Finding:</strong> Gulberg commanded 20 ride requests (20.0% of demand) but experienced a <strong>30.0% cancellation rate (6 cancelled rides)</strong> and the lowest completed average fare (₨397.07).<br>
              <strong>Meaning:</strong> Driver reluctance to accept lower-fare trips in congested traffic creates severe passenger friction.
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800">
              <strong class="text-emerald-300 block">3. Revenue Mirage vs Operational Dependability</strong>
              <strong>Finding:</strong> DRV-002 achieved top gross revenue (₨4,484.00) but cancelled 10% of trips. DRV-010, DRV-004, and DRV-001 achieved <strong>100% completion (0 cancellations)</strong> while earning >₨4,000.<br>
              <strong>Meaning:</strong> Evaluating drivers purely on top-line revenue encourages cherry-picking; multi-criteria scoring preserves reliability.
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800">
              <strong class="text-amber-300 block">4. Premium Tier Ticket Yield Density</strong>
              <strong>Finding:</strong> Premium rides average <strong>₨558.05 per journey (+30.3% over Standard)</strong> across comparable distances (19.5 km vs 14.2 km), contributing 33.67% of revenue from only 22 trips.<br>
              <strong>Meaning:</strong> Premium riders show strong pricing tolerance; expanding executive supply expands operator margins.
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800">
              <strong class="text-purple-300 block">5. Concentration of Platform Churn</strong>
              <strong>Finding:</strong> Two drivers (DRV-005 with 4 cancellations and DRV-007 with 3 cancellations) caused <strong>46.7% of all platform churn (7 of 15 cancellations)</strong>.<br>
              <strong>Meaning:</strong> Cancellation leakage is concentrated among isolated operators rather than systemic across the entire fleet.
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800">
              <strong class="text-indigo-300 block">6. Digital Financial Ecosystem Dominance</strong>
              <strong>Finding:</strong> Digital payment channels collectively account for <strong>61.29% of revenue (₨22,351.00)</strong> across Card (29.6%), UPI (22.4%), and Wallet (9.2%), while Cash accounts for 38.71%.<br>
              <strong>Meaning:</strong> High digital adoption streamlines driver settlement and eliminates change-handling delays.
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800">
              <strong class="text-sky-300 block">7. Temporal Demand & Weekday Peaks</strong>
              <strong>Finding:</strong> <strong>Thursday (24 bookings)</strong> and <strong>Tuesday (20 bookings)</strong> drive 44.0% of total weekly volume. Friday experienced the highest weekday cancellation rate (25.0%).<br>
              <strong>Meaning:</strong> Fleet scheduling must dynamically align with midweek business travel patterns.
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800">
              <strong class="text-yellow-300 block">8. Cross-City Transit Equilibrium</strong>
              <strong>Finding:</strong> Drop-off destinations are uniformly distributed across Johar Town (22%), Gulberg (21%), Model Town (20%), Bahria Town (19%), and DHA (18%).<br>
              <strong>Meaning:</strong> Fleet re-balancing is relatively efficient because vehicles naturally disperse across all residential sectors.
            </div>
          </div>
        </div>

        <!-- 5+ Recommendations -->
        <div class="acrylic-card rounded-2xl p-5 space-y-3">
          <h3 class="text-sm font-bold text-white flex items-center gap-2">
            <span class="text-emerald-400">🚀</span> 5 Practical Business Recommendations
          </h3>
          <div class="space-y-2.5 text-xs text-slate-300 leading-relaxed">
            <div class="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800">
              <strong class="text-emerald-300 block">1. Geofenced Fulfillment Bonus for Gulberg</strong>
              <strong>Finding:</strong> Gulberg suffers 30% cancellation churn and lower fare yield (₨397.07).<br>
              <strong>Action:</strong> Deploy a dynamic ₨50 - ₨75 pickup bonus for drivers accepting dispatches originating in Gulberg.<br>
              <strong>Expected Impact:</strong> Drop churn below 12%, recapturing ~₨1,800.00 in leaked bookings.<br>
              <em class="text-slate-400 text-[10px]">Limitation: Requires A/B testing against driver acceptance elasticities.</em>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800">
              <strong class="text-cyan-300 block">2. Star Partner Priority Dispatch Protocol</strong>
              <strong>Finding:</strong> DRV-010, 004, and 001 maintain 100% completion rates and high ratings.<br>
              <strong>Action:</strong> Implement dispatch routing giving 100% completion drivers priority assignment to high-yield Premium trips.<br>
              <strong>Expected Impact:</strong> Reduces passenger wait times and rewards dependable fleet partners.<br>
              <em class="text-slate-400 text-[10px]">Limitation: Must ensure minimum dispatch volume remains equitable for lower tiers.</em>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800">
              <strong class="text-amber-300 block">3. Strategic Expansion of Premium Tier Fleet</strong>
              <strong>Finding:</strong> Premium trips yield ₨558.05 (+30.3% over Standard) across similar travel distances.<br>
              <strong>Action:</strong> Recruit and onboard vehicles meeting executive comfort standards into the Premium fleet.<br>
              <strong>Expected Impact:</strong> Expands platform gross margins and raises average ticket size.<br>
              <em class="text-slate-400 text-[10px]">Limitation: Dependent on luxury vehicle supply in the Lahore market.</em>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800">
              <strong class="text-indigo-300 block">4. Targeted Driver Retraining & Churn Warnings</strong>
              <strong>Finding:</strong> DRV-005 (40% churn) and DRV-007 (30% churn) account for nearly half of all unfulfilled trips.<br>
              <strong>Action:</strong> Issue automated operational alerts and schedule mandatory route compliance retraining.<br>
              <strong>Expected Impact:</strong> Immediately eliminates ~5 to 6 cancellations per 100 dispatches.<br>
              <em class="text-slate-400 text-[10px]">Limitation: High cancellation drivers may churn off platform if penalties are too severe.</em>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800">
              <strong class="text-purple-300 block">5. Digital Payment Cashback Acceleration</strong>
              <strong>Finding:</strong> Cash remains 38.7% of collections, introducing cash-handling friction.<br>
              <strong>Action:</strong> Offer 5% instant cashback on Card, UPI, and Wallet settlements.<br>
              <strong>Expected Impact:</strong> Compresses cash share below 20%, accelerating driver turnover.<br>
              <em class="text-slate-400 text-[10px]">Limitation: Promotional budget requires subsidy from gateway partners.</em>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- FOOTER -->
    <footer class="text-center text-xs text-slate-500 py-4 border-t border-slate-800/80">
      ZYROO Data Analytics Internship • Week 5 Advanced BI & Decision Analytics Platform • Offline & Localhost Enabled
    </footer>

  </div>

  <script>
    const RAW_RIDES = {json.dumps(records)};
    let filteredRides = [...RAW_RIDES];

    function switchTab(tabId) {{
      document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
      document.getElementById(tabId).classList.remove('hidden');
      document.getElementById('btn-' + tabId).classList.add('active');
    }}

    function initFilters() {{
      const dates = [...new Set(RAW_RIDES.map(r => r.date))].sort();
      const dateSelect = document.getElementById('filter-date');
      dates.forEach(d => {{
        const opt = document.createElement('option');
        opt.value = d;
        opt.textContent = d;
        dateSelect.appendChild(opt);
      }});

      const locations = [...new Set(RAW_RIDES.map(r => r.pickup_location))].sort();
      const locSelect = document.getElementById('filter-location');
      locations.forEach(l => {{
        const opt = document.createElement('option');
        opt.value = l;
        opt.textContent = l;
        locSelect.appendChild(opt);
      }});

      const rideTypes = [...new Set(RAW_RIDES.map(r => r.ride_type))].sort();
      const rtSelect = document.getElementById('filter-ride-type');
      rideTypes.forEach(rt => {{
        const opt = document.createElement('option');
        opt.value = rt;
        opt.textContent = rt;
        rtSelect.appendChild(opt);
      }});

      const payments = [...new Set(RAW_RIDES.map(r => r.payment_method))].sort();
      const paySelect = document.getElementById('filter-payment');
      payments.forEach(p => {{
        const opt = document.createElement('option');
        opt.value = p;
        opt.textContent = p;
        paySelect.appendChild(opt);
      }});

      const drivers = [...new Set(RAW_RIDES.map(r => r.driver_id))].sort();
      const drvSelect = document.getElementById('filter-driver');
      drivers.forEach(drv => {{
        const opt = document.createElement('option');
        opt.value = drv;
        opt.textContent = drv;
        drvSelect.appendChild(opt);
      }});
    }}

    function applyFilters() {{
      const dVal = document.getElementById('filter-date').value;
      const sVal = document.getElementById('filter-status').value;
      const lVal = document.getElementById('filter-location').value;
      const rtVal = document.getElementById('filter-ride-type').value;
      const pVal = document.getElementById('filter-payment').value;
      const drvVal = document.getElementById('filter-driver').value;

      filteredRides = RAW_RIDES.filter(r => {{
        if (dVal !== 'ALL' && r.date !== dVal) return false;
        if (sVal !== 'ALL' && r.ride_status !== sVal) return false;
        if (lVal !== 'ALL' && r.pickup_location !== lVal) return false;
        if (rtVal !== 'ALL' && r.ride_type !== rtVal) return false;
        if (pVal !== 'ALL' && r.payment_method !== pVal) return false;
        if (drvVal !== 'ALL' && r.driver_id !== drvVal) return false;
        return true;
      }});

      document.getElementById('slicer-count').textContent = `${{filteredRides.length}} / ${{RAW_RIDES.length}}`;
      updateKPIs(filteredRides);
      renderExecVisuals(filteredRides);
      renderRevVisuals(filteredRides);
      renderDriverTable();
      renderCancVisuals(filteredRides);
    }}

    function resetAllFilters() {{
      document.getElementById('filter-date').value = 'ALL';
      document.getElementById('filter-status').value = 'ALL';
      document.getElementById('filter-location').value = 'ALL';
      document.getElementById('filter-ride-type').value = 'ALL';
      document.getElementById('filter-payment').value = 'ALL';
      document.getElementById('filter-driver').value = 'ALL';
      applyFilters();
    }}

    function updateKPIs(data) {{
      const total = data.length;
      const comp = data.filter(r => r.ride_status === 'Completed');
      const canc = data.filter(r => r.ride_status === 'Cancelled');
      const compCount = comp.length;
      const cancCount = canc.length;

      const rev = comp.reduce((acc, r) => acc + r.fare, 0);
      const gbv = data.reduce((acc, r) => acc + r.fare, 0);
      const avgFare = compCount > 0 ? (rev / compCount) : 0;
      const crate = total > 0 ? ((compCount / total) * 100) : 0;
      const cancRate = total > 0 ? ((cancCount / total) * 100) : 0;

      const rated = comp.filter(r => r.rating !== null && r.rating !== undefined);
      const avgRating = rated.length > 0 ? (rated.reduce((acc, r) => acc + r.rating, 0) / rated.length) : 0;
      const compDist = comp.reduce((acc, r) => acc + (r.distance_km || 0), 0);
      const avgDist = compCount > 0 ? (compDist / compCount) : 0;

      document.getElementById('kpi-rides').textContent = total;
      document.getElementById('kpi-completed').textContent = compCount;
      document.getElementById('kpi-crate-sub').textContent = `${{crate.toFixed(1)}}% Fulfill Rate`;
      document.getElementById('kpi-cancelled').textContent = cancCount;
      document.getElementById('kpi-canc-sub').textContent = `${{cancRate.toFixed(1)}}% Churn Rate`;
      document.getElementById('kpi-revenue').textContent = `₨${{rev.toLocaleString('en-US', {{maximumFractionDigits:0}})}}`;
      document.getElementById('kpi-avg-fare').textContent = `₨${{avgFare.toFixed(2)}}`;
      document.getElementById('kpi-gbv').textContent = `₨${{gbv.toLocaleString('en-US', {{maximumFractionDigits:0}})}}`;
      document.getElementById('kpi-rating').textContent = avgRating > 0 ? `${{avgRating.toFixed(2)}} ★` : '—';
      document.getElementById('kpi-distance').textContent = `${{avgDist.toFixed(1)}} km`;
    }}

    function renderExecVisuals(data) {{
      // Rides by Date Line Chart
      const boxD = document.getElementById('chart-exec-date');
      const dates = [...new Set(RAW_RIDES.map(r => r.date))].sort();
      const counts = dates.map(d => data.filter(r => r.date === d).length);
      const compCounts = dates.map(d => data.filter(r => r.date === d && r.ride_status === 'Completed').length);
      const maxVal = Math.max(...counts, 5);

      const w = 450, h = 200, padL = 30, padR = 20, padT = 20, padB = 30;
      const innerW = w - padL - padR, innerH = h - padT - padB;
      const getX = (i) => padL + (i / (dates.length - 1)) * innerW;
      const getY = (v) => padT + innerH - (v / maxVal) * innerH;

      let pTot = '', pComp = '', dots = '';
      counts.forEach((c, i) => {{
        const x = getX(i), y = getY(c);
        pTot += (i === 0 ? `M ${{x}} ${{y}}` : ` L ${{x}} ${{y}}`);
        const dStr = dates[i].split('-')[2];
        dots += `<circle cx="${{x}}" cy="${{y}}" r="3.5" fill="#38bdf8"/>`;
        dots += `<text x="${{x}}" y="${{h - 10}}" fill="#94a3b8" font-size="9" text-anchor="middle">Sep ${{dStr}}</text>`;
      }});
      compCounts.forEach((c, i) => {{
        const x = getX(i), y = getY(c);
        pComp += (i === 0 ? `M ${{x}} ${{y}}` : ` L ${{x}} ${{y}}`);
      }});

      boxD.innerHTML = `
        <svg viewBox="0 0 ${{w}} ${{h}}" class="w-full h-full">
          <line x1="${{padL}}" y1="${{padT + innerH}}" x2="${{w - padR}}" y2="${{padT + innerH}}" stroke="#1e293b"/>
          <path d="${{pTot}}" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
          <path d="${{pComp}}" fill="none" stroke="#34d399" stroke-width="2" stroke-dasharray="3,3"/>
          ${{dots}}
        </svg>
      `;

      // Weekday Bar Chart
      const boxW = document.getElementById('chart-exec-weekday');
      const days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
      const dayFull = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
      const dayCounts = dayFull.map(df => data.filter(r => new Date(r.date).toLocaleDateString('en-US', {{weekday:'long'}}) === df).length);
      const maxW = Math.max(...dayCounts, 5);
      const barW = innerW / days.length - 10;
      let barsW = '';
      days.forEach((d, i) => {{
        const val = dayCounts[i];
        const bH = (val / maxW) * innerH;
        const x = padL + i * (innerW / days.length) + 5;
        const y = padT + innerH - bH;
        barsW += `
          <rect x="${{x}}" y="${{y}}" width="${{barW}}" height="${{bH}}" rx="4" fill="#818cf8"/>
          <text x="${{x + barW/2}}" y="${{y - 4}}" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">${{val}}</text>
          <text x="${{x + barW/2}}" y="${{h - 10}}" fill="#94a3b8" font-size="9" text-anchor="middle">${{d}}</text>
        `;
      }});
      boxW.innerHTML = `<svg viewBox="0 0 ${{w}} ${{h}}" class="w-full h-full">${{barsW}}</svg>`;

      // Location Bar Chart
      const boxL = document.getElementById('chart-exec-loc');
      const locs = ['DHA', 'Gulberg', 'Bahria Town', 'Johar Town', 'Model Town'];
      const locCounts = locs.map(l => data.filter(r => r.pickup_location === l).length);
      const maxL = Math.max(...locCounts, 5);
      const barHL = innerH / locs.length - 8;
      let barsL = '';
      locs.forEach((l, i) => {{
        const val = locCounts[i];
        const bW = (val / maxL) * (w - 110);
        const y = padT + i * (innerH / locs.length) + 4;
        barsL += `
          <text x="75" y="${{y + barHL/2 + 3}}" fill="#cbd5e1" font-size="10" text-anchor="end">${{l}}</text>
          <rect x="80" y="${{y}}" width="${{bW}}" height="${{barHL}}" rx="3" fill="#38bdf8"/>
          <text x="${{85 + bW}}" y="${{y + barHL/2 + 3}}" fill="#34d399" font-size="9" font-weight="bold">${{val}}</text>
        `;
      }});
      boxL.innerHTML = `<svg viewBox="0 0 ${{w}} ${{h}}" class="w-full h-full">${{barsL}}</svg>`;
    }}

    function renderRevVisuals(data) {{
      const comp = data.filter(r => r.ride_status === 'Completed');
      // Payment Donut
      const boxP = document.getElementById('chart-rev-pay');
      const methods = ['Cash', 'Card', 'UPI', 'Wallet'];
      const colors = ['#38bdf8', '#818cf8', '#34d399', '#fbbf24'];
      const sums = methods.map(m => comp.filter(r => r.payment_method === m).reduce((a, b) => a + b.fare, 0));
      const total = sums.reduce((a, b) => a + b, 0);

      if (total === 0) {{
        boxP.innerHTML = '<span class="text-xs text-slate-500">No completed transactions</span>';
      }} else {{
        let curAngle = 0, paths = '', legend = '';
        sums.forEach((s, idx) => {{
          const pct = s / total, angle = pct * 360;
          const rO = 70, rI = 45;
          const sRad = (curAngle - 90) * Math.PI / 180;
          const eRad = (curAngle + angle - 90) * Math.PI / 180;
          const x1 = 90 + rO * Math.cos(sRad), y1 = 90 + rO * Math.sin(sRad);
          const x2 = 90 + rO * Math.cos(eRad), y2 = 90 + rO * Math.sin(eRad);
          const x3 = 90 + rI * Math.cos(eRad), y3 = 90 + rI * Math.sin(eRad);
          const x4 = 90 + rI * Math.cos(sRad), y4 = 90 + rI * Math.sin(sRad);
          const la = angle > 180 ? 1 : 0;
          if (s > 0) {{
            paths += `<path d="M ${{x1}} ${{y1}} A ${{rO}} ${{rO}} 0 ${{la}} 1 ${{x2}} ${{y2}} L ${{x3}} ${{y3}} A ${{rI}} ${{rI}} 0 ${{la}} 0 ${{x4}} ${{y4}} Z" fill="${{colors[idx]}}" stroke="#080d1a" stroke-width="2"/>`;
          }}
          legend += `
            <div class="flex items-center justify-between text-[11px]">
              <span class="flex items-center gap-1.5 text-slate-300">
                <span class="w-2.5 h-2.5 rounded-full" style="background-color:${{colors[idx]}}"></span> ${{methods[idx]}}
              </span>
              <span class="font-bold font-mono-num text-white">₨${{s.toLocaleString()}} (${{(pct*100).toFixed(1)}}%)</span>
            </div>
          `;
          curAngle += angle;
        }});
        boxP.innerHTML = `<div class="flex items-center gap-4 w-full justify-center"><svg viewBox="0 0 180 180" class="w-36 h-36">${{paths}}</svg><div class="space-y-1.5 flex-1 max-w-[200px]">${{legend}}</div></div>`;
      }}

      // Tier Revenue Bar
      const boxT = document.getElementById('chart-rev-tier');
      const tiers = ['Economy', 'Standard', 'Premium'];
      const tierSums = tiers.map(t => comp.filter(r => r.ride_type === t).reduce((a, b) => a + b.fare, 0));
      const maxT = Math.max(...tierSums, 5000);
      const w = 450, h = 200, padL = 40, padR = 20, padT = 20, padB = 30;
      const innerW = w - padL - padR, innerH = h - padT - padB;
      const barWT = innerW / tiers.length - 30;
      let barsT = '';
      tiers.forEach((t, i) => {{
        const val = tierSums[i];
        const bH = (val / maxT) * innerH;
        const x = padL + i * (innerW / tiers.length) + 15;
        const y = padT + innerH - bH;
        barsT += `
          <rect x="${{x}}" y="${{y}}" width="${{barWT}}" height="${{bH}}" rx="4" fill="#38bdf8"/>
          <text x="${{x + barWT/2}}" y="${{y - 5}}" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">₨${{val.toLocaleString()}}</text>
          <text x="${{x + barWT/2}}" y="${{h - 10}}" fill="#94a3b8" font-size="10" text-anchor="middle">${{t}}</text>
        `;
      }});
      boxT.innerHTML = `<svg viewBox="0 0 ${{w}} ${{h}}" class="w-full h-full">${{barsT}}</svg>`;

      // Location Revenue Bar
      const boxLR = document.getElementById('chart-rev-loc');
      const locs = ['DHA', 'Bahria Town', 'Gulberg', 'Johar Town', 'Model Town'];
      const locRevs = locs.map(l => comp.filter(r => r.pickup_location === l).reduce((a, b) => a + b.fare, 0));
      const maxLR = Math.max(...locRevs, 5000);
      const barHLR = innerH / locs.length - 8;
      let barsLR = '';
      locs.forEach((l, i) => {{
        const val = locRevs[i];
        const bW = (val / maxLR) * (w - 110);
        const y = padT + i * (innerH / locs.length) + 4;
        barsLR += `
          <text x="75" y="${{y + barHLR/2 + 3}}" fill="#cbd5e1" font-size="10" text-anchor="end">${{l}}</text>
          <rect x="80" y="${{y}}" width="${{bW}}" height="${{barHLR}}" rx="3" fill="#34d399"/>
          <text x="${{85 + bW}}" y="${{y + barHLR/2 + 3}}" fill="#38bdf8" font-size="9" font-weight="bold">₨${{val.toLocaleString()}}</text>
        `;
      }});
      boxLR.innerHTML = `<svg viewBox="0 0 ${{w}} ${{h}}" class="w-full h-full">${{barsLR}}</svg>`;
    }}

    function renderDriverTable() {{
      const sortBy = document.getElementById('driver-sort-by').value;
      const drivers = [...new Set(RAW_RIDES.map(r => r.driver_id))].sort();
      const benchRev = 3646.60, benchCrate = 85.0;

      const stats = drivers.map(d => {{
        const allD = filteredRides.filter(r => r.driver_id === d);
        const compD = allD.filter(r => r.ride_status === 'Completed');
        const cancD = allD.filter(r => r.ride_status === 'Cancelled');
        const rev = compD.reduce((a, b) => a + b.fare, 0);
        const rated = compD.filter(r => r.rating !== null && r.rating !== undefined);
        const avgR = rated.length > 0 ? (rated.reduce((a, b) => a + b.rating, 0) / rated.length) : 0;
        const crate = allD.length > 0 ? ((compD.length / allD.length) * 100) : 0;

        return {{
          id: d,
          total: allD.length,
          completed: compD.length,
          cancelled: cancD.length,
          revenue: rev,
          rating: avgR,
          crate: crate,
          revDelta: rev - benchRev,
          crateDelta: crate - benchCrate
        }};
      }});

      const minR = Math.min(...stats.map(s => s.revenue)), maxR = Math.max(...stats.map(s => s.revenue));
      const minC = Math.min(...stats.map(s => s.completed)), maxC = Math.max(...stats.map(s => s.completed));
      const minRat = Math.min(...stats.map(s => s.rating)), maxRat = Math.max(...stats.map(s => s.rating));
      const minCr = Math.min(...stats.map(s => s.crate)), maxCr = Math.max(...stats.map(s => s.crate));

      stats.forEach(s => {{
        const normR = maxR > minR ? (s.revenue - minR) / (maxR - minR) * 100 : 50;
        const normC = maxC > minC ? (s.completed - minC) / (maxC - minC) * 100 : 50;
        const normRat = maxRat > minRat ? (s.rating - minRat) / (maxRat - minRat) * 100 : 50;
        const normCr = maxCr > minCr ? (s.crate - minCr) / (maxCr - minCr) * 100 : 50;
        s.score = (0.35 * normR + 0.25 * normC + 0.25 * normRat + 0.15 * normCr);
      }});

      stats.sort((a, b) => {{
        if (sortBy === 'composite') return b.score - a.score;
        if (sortBy === 'revenue') return b.revenue - a.revenue;
        if (sortBy === 'completed') return b.completed - a.completed;
        if (sortBy === 'crate') return b.crate - a.crate;
        if (sortBy === 'rating') return b.rating - a.rating;
        return 0;
      }});

      const tbody = document.getElementById('driver-tbody');
      tbody.innerHTML = stats.map((s, idx) => {{
        const tierBadge = s.crate === 100 
          ? '<span class="px-2 py-0.5 rounded text-[10px] bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-bold">🌟 Star Partner</span>'
          : s.crate >= 80
          ? '<span class="px-2 py-0.5 rounded text-[10px] bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 font-bold">🟢 Reliable</span>'
          : '<span class="px-2 py-0.5 rounded text-[10px] bg-rose-500/10 text-rose-400 border border-rose-500/20 font-bold">🔴 Churn Risk</span>';

        return `
          <tr class="hover:bg-slate-800/40">
            <td class="p-3 font-bold text-slate-400">#${{idx + 1}}</td>
            <td class="p-3 font-bold text-cyan-400 font-sans">${{s.id}}</td>
            <td class="p-3 text-center text-white">${{s.total}}</td>
            <td class="p-3 text-center text-emerald-400 font-bold">${{s.completed}}</td>
            <td class="p-3 text-center ${{s.cancelled > 0 ? 'text-rose-400 font-bold' : 'text-slate-500'}}">${{s.cancelled}}</td>
            <td class="p-3 text-right font-bold text-white">₨${{s.revenue.toLocaleString()}}</td>
            <td class="p-3 text-right ${{s.revDelta >= 0 ? 'text-emerald-400' : 'text-rose-400'}}">${{s.revDelta >= 0 ? '+' : ''}}₨${{s.revDelta.toFixed(0)}}</td>
            <td class="p-3 text-center font-bold text-white">${{s.crate.toFixed(0)}}%</td>
            <td class="p-3 text-center ${{s.crateDelta >= 0 ? 'text-emerald-400' : 'text-rose-400'}}">${{s.crateDelta >= 0 ? '+' : ''}}${{s.crateDelta.toFixed(0)}}%</td>
            <td class="p-3 text-right text-yellow-400 font-bold">${{s.rating > 0 ? s.rating.toFixed(2) + ' ★' : '—'}}</td>
            <td class="p-3 text-right font-bold text-cyan-300">${{s.score.toFixed(1)}}</td>
            <td class="p-3 text-center">${{tierBadge}}</td>
          </tr>
        `;
      }}).join('');
    }}

    function renderCancVisuals(data) {{
      const boxL = document.getElementById('chart-canc-loc');
      const locs = ['DHA', 'Gulberg', 'Bahria Town', 'Johar Town', 'Model Town'];
      const rates = locs.map(l => {{
        const allL = data.filter(r => r.pickup_location === l);
        const canL = allL.filter(r => r.ride_status === 'Cancelled');
        return allL.length > 0 ? (canL.length / allL.length * 100) : 0;
      }});
      const w = 450, h = 200, padL = 75, padR = 40, padT = 20, padB = 20;
      const innerW = w - padL - padR, innerH = h - padT - padB;
      const barH = innerH / locs.length - 8;
      let bars = '';
      locs.forEach((l, i) => {{
        const r = rates[i];
        const bW = (r / 35) * innerW;
        const y = padT + i * (innerH / locs.length) + 4;
        bars += `
          <text x="70" y="${{y + barH/2 + 3}}" fill="#cbd5e1" font-size="10" text-anchor="end">${{l}}</text>
          <rect x="75" y="${{y}}" width="${{bW}}" height="${{barH}}" rx="3" fill="${{r >= 20 ? '#f87171' : '#38bdf8'}}"/>
          <text x="${{80 + bW}}" y="${{y + barH/2 + 3}}" fill="${{r >= 20 ? '#f87171' : '#38bdf8'}}" font-size="9" font-weight="bold">${{r.toFixed(1)}}%</text>
        `;
      }});
      boxL.innerHTML = `<svg viewBox="0 0 ${{w}} ${{h}}" class="w-full h-full">${{bars}}</svg>`;

      const boxD = document.getElementById('chart-canc-day');
      const days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
      const dayFull = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
      const dayRates = dayFull.map(df => {{
        const allD = data.filter(r => new Date(r.date).toLocaleDateString('en-US', {{weekday:'long'}}) === df);
        const canD = allD.filter(r => r.ride_status === 'Cancelled');
        return allD.length > 0 ? (canD.length / allD.length * 100) : 0;
      }});
      const barWD = innerW / days.length - 10;
      let barsD = '';
      days.forEach((d, i) => {{
        const r = dayRates[i];
        const bH = (r / 30) * innerH;
        const x = padL + i * (innerW / days.length) + 5;
        const y = padT + innerH - bH;
        barsD += `
          <rect x="${{x}}" y="${{y}}" width="${{barWD}}" height="${{bH}}" rx="4" fill="${{r >= 20 ? '#f87171' : '#818cf8'}}"/>
          <text x="${{x + barWD/2}}" y="${{y - 4}}" fill="${{r >= 20 ? '#f87171' : '#38bdf8'}}" font-size="8" font-weight="bold" text-anchor="middle">${{r.toFixed(0)}}%</text>
          <text x="${{x + barWD/2}}" y="${{h - 10}}" fill="#94a3b8" font-size="9" text-anchor="middle">${{d}}</text>
        `;
      }});
      boxD.innerHTML = `<svg viewBox="0 0 ${{w}} ${{h}}" class="w-full h-full">${{barsD}}</svg>`;
    }}

    function runScenarios() {{
      const pA = parseFloat(document.getElementById('slider-scen-a').value);
      const pB = parseFloat(document.getElementById('slider-scen-b').value);
      const pC = parseFloat(document.getElementById('slider-scen-c').value);

      document.getElementById('val-scen-a').textContent = `+${{pA}}%`;
      document.getElementById('val-scen-b').textContent = `${{pB >= 0 ? '+' : ''}}${{pB}}%`;
      document.getElementById('val-scen-c').textContent = `${{pC}}% Recovered`;

      // Scenario A
      const baseComp = 85, baseRev = 36466, baseFare = 429.0117;
      const newTripsA = baseComp * (1 + pA / 100);
      const newRevA = newTripsA * baseFare;
      document.getElementById('res-trips-a').textContent = newTripsA.toFixed(1);
      document.getElementById('res-rev-a').textContent = `₨${{Math.round(newRevA).toLocaleString()}}`;
      document.getElementById('res-delta-a').textContent = `+₨${{Math.round(newRevA - baseRev).toLocaleString()}}`;

      // Scenario B
      const newFareB = baseFare * (1 + pB / 100);
      const newRevB = baseComp * newFareB;
      document.getElementById('res-fare-b').textContent = `₨${{newFareB.toFixed(2)}}`;
      document.getElementById('res-rev-b').textContent = `₨${{Math.round(newRevB).toLocaleString()}}`;
      document.getElementById('res-delta-b').textContent = `${{newRevB >= baseRev ? '+₨' : '-₨'}}${{Math.abs(Math.round(newRevB - baseRev)).toLocaleString()}}`;

      // Scenario C
      const churnLeakage = 6496;
      const recRevC = churnLeakage * (pC / 100);
      const newRevC = baseRev + recRevC;
      document.getElementById('res-rec-c').textContent = `₨${{Math.round(recRevC).toLocaleString()}}`;
      document.getElementById('res-rev-c').textContent = `₨${{Math.round(newRevC).toLocaleString()}}`;
      document.getElementById('res-pct-c').textContent = `+${{((recRevC / baseRev) * 100).toFixed(2)}}%`;
    }}

    function downloadCSV() {{
      const headers = ["ride_id","date","pickup_location","dropoff_location","distance_km","fare","payment_method","driver_id","ride_type","ride_status","rating"];
      const rows = filteredRides.map(r => [r.ride_id, r.date, r.pickup_location, r.dropoff_location, r.distance_km, r.fare, r.payment_method, r.driver_id, r.ride_type, r.ride_status, r.rating || '']);
      const csvContent = "data:text/csv;charset=utf-8," + [headers.join(",")].concat(rows.map(e => e.join(","))).join("\\n");
      const link = document.createElement("a");
      link.setAttribute("href", encodeURI(csvContent));
      link.setAttribute("download", "zyroo_week5_decision_analytics_telemetry.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      initFilters();
      applyFilters();
      runScenarios();
    }});
  </script>
</body>
</html>
"""

with open('powerbi/week-05-advanced-analytics/index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Generated Week 5 Multi-Page Advanced BI Dashboard in powerbi/week-05-advanced-analytics/index.html and index.html!")
