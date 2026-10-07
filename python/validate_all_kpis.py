"""
ZYROO DATA ANALYTICS FINAL CAPSTONE PROJECT
Automated KPI Verification & Mathematical Triangulation Engine
Validates: Python vs SQL vs DAX Business Logic
"""

import pandas as pd
import numpy as np

def run_kpi_validation():
    print("=" * 70)
    print("ZYROO FINAL CAPSTONE: MULTI-ENGINE KPI VALIDATION AUDIT")
    print("=" * 70)
    
    # Load standardized ground truth
    df = pd.read_csv('data/rides_data_week3.csv')
    
    # 1. Base Metrics
    total_rides = len(df)
    completed_rides = int((df['ride_status'] == 'Completed').sum())
    cancelled_rides = int((df['ride_status'] == 'Cancelled').sum())
    completion_rate = (completed_rides / total_rides) * 100
    cancellation_rate = (cancelled_rides / total_rides) * 100
    
    gross_booked_rev = float(df['fare'].sum())
    realized_rev = float(df[df['ride_status'] == 'Completed']['fare'].sum())
    lost_rev = float(df[df['ride_status'] == 'Cancelled']['fare'].sum())
    
    avg_fare_overall = float(df['fare'].mean())
    avg_fare_completed = float(df[df['ride_status'] == 'Completed']['fare'].mean())
    avg_fare_cancelled = float(df[df['ride_status'] == 'Cancelled']['fare'].mean())
    
    avg_distance = float(df['distance_km'].mean())
    avg_rating_completed = float(df[df['ride_status'] == 'Completed']['rating'].mean())
    
    unique_drivers = int(df['driver_id'].nunique())
    unique_pickup = int(df['pickup_location'].nunique())
    unique_dropoff = int(df['dropoff_location'].nunique())
    
    # Validation Table Definitions
    validation_records = [
        ("Total Rides", 100, total_rides, "COUNTROWS(Fact_Rides)"),
        ("Completed Rides", 85, completed_rides, "CALCULATE(COUNTROWS(), Status='Completed')"),
        ("Cancelled Rides", 15, cancelled_rides, "CALCULATE(COUNTROWS(), Status='Cancelled')"),
        ("Completion Rate (%)", 85.00, round(completion_rate, 2), "DIVIDE([Completed Rides], [Total Rides])"),
        ("Cancellation Rate (%)", 15.00, round(cancellation_rate, 2), "DIVIDE([Cancelled Rides], [Total Rides])"),
        ("Gross Booked Revenue ($)", 42962.00, round(gross_booked_rev, 2), "SUM(Fact_Rides[Fare])"),
        ("Realized Revenue ($)", 36466.00, round(realized_rev, 2), "CALCULATE(SUM(Fare), Status='Completed')"),
        ("Lost Cancellation Revenue ($)", 6496.00, round(lost_rev, 2), "CALCULATE(SUM(Fare), Status='Cancelled')"),
        ("Average Realized Fare ($)", 429.01, round(avg_fare_completed, 2), "DIVIDE([Realized Revenue], [Completed Rides])"),
        ("Average Distance (km)", 13.76, round(avg_distance, 2), "AVERAGE(Fact_Rides[Distance_km])"),
        ("Average Rating (Completed)", 4.27, round(avg_rating_completed, 2), "CALCULATE(AVERAGE(Rating), Status='Completed')"),
        ("Active Driver Count", 10, unique_drivers, "DISTINCTCOUNT(Fact_Rides[Driver_ID])"),
        ("Pickup Locations", 5, unique_pickup, "DISTINCTCOUNT(Fact_Rides[Pickup_Location])"),
        ("Drop-off Locations", 5, unique_dropoff, "DISTINCTCOUNT(Fact_Rides[Dropoff_Location])")
    ]
    
    print(f"{'KPI Name':<30} | {'Expected':<10} | {'Calculated':<10} | {'Diff':<6} | {'Status':<6}")
    print("-" * 70)
    
    all_passed = True
    for name, exp, calc, dax_formula in validation_records:
        diff = abs(exp - calc)
        status = "PASS" if diff < 0.01 else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"{name:<30} | {exp:<10} | {calc:<10} | {diff:<6.2f} | {status:<6}")
        
    print("=" * 70)
    print(f"Overall Quality Audit Status: {'100% PASSED (PRODUCTION VERIFIED)' if all_passed else 'FAILED'}")
    print("=" * 70)
    
    # Scenario Modeling Validation
    print("\n=== SCENARIO MODELING INDEPENDENT TEST ===")
    # Scenario A: Target 92% completion rate (+7 rides)
    target_comp_rate = 0.92
    sim_comp_rides = round(total_rides * target_comp_rate)
    inc_rides = sim_comp_rides - completed_rides
    inc_revenue_a = inc_rides * avg_fare_completed
    sim_rev_a = realized_rev + inc_revenue_a
    print(f"Scenario A (92% Comp Rate): +{inc_rides} Completed Rides | +${inc_revenue_a:.2f} Incremental Realized Revenue | Total Sim Rev: ${sim_rev_a:.2f}")
    
    # Scenario B: 50% cancellation reduction (15 -> 7, -8 cancellations)
    sim_cancellations = 7
    recaptured_rides = cancelled_rides - sim_cancellations
    inc_revenue_b = recaptured_rides * avg_fare_cancelled
    sim_rev_b = realized_rev + inc_revenue_b
    print(f"Scenario B (50% Cancellation Cut): -{recaptured_rides} Cancellations | +${inc_revenue_b:.2f} Recaptured Revenue | Total Sim Rev: ${sim_rev_b:.2f}")
    print("=" * 70)

if __name__ == '__main__':
    run_kpi_validation()
