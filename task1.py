def calculate_monthly_bill(consumption, tariff_slabs, fixed_charge, surcharge_pct, rebate):
    """
    Calculates total bill based on progressive slabs.
    tariff_slabs: List of dicts {'limit': (int), 'rate': (float)}
    """
    energy_cost = 0
    previous_limit = 0
    remaining_consumption = consumption

    # Progressive slab calculation
    for slab in sorted(tariff_slabs, key=lambda x: x['limit']):
        if remaining_consumption <= 0:
            break
        
        # Calculate units in current slab
        units_in_slab = min(remaining_consumption, slab['limit'] - previous_limit)
        energy_cost += units_in_slab * slab['rate']
        
        remaining_consumption -= units_in_slab
        previous_limit = slab['limit']

    # Final bill assembly
    surcharge = (energy_cost + fixed_charge) * (surcharge_pct / 100)
    total_bill = energy_cost + fixed_charge + surcharge - rebate
    
    return round(total_bill, 2)

# --- Configuration & Data ---
tariff = [
    {'limit': 100, 'rate': 0.10},  # First 100 units
    {'limit': 300, 'rate': 0.15},  # Next 200 units
    {'limit': float('inf'), 'rate': 0.20} # Remaining
]

# Historical consumption data (kWh)
monthly_data = {
    "Jan": 250, "Feb": 260, "Mar": 450, "Apr": 270
}

# --- Calculation and Analysis ---
results = {}
for month, usage in monthly_data.items():
    results[month] = calculate_monthly_bill(usage, tariff, 15.00, 5.0, 2.00)

print("Monthly Bills:", results)

# Identify unusual increases (e.g., > 30% increase from previous month)
threshold = 30.0
months = list(results.keys())

for i in range(1, len(months)):
    prev_month = months[i-1]
    curr_month = months[i]
    
    increase = ((results[curr_month] - results[prev_month]) / results[prev_month]) * 100
    
    if increase > threshold:
        print(f"Alert: Unusual increase in {curr_month} (+{round(increase, 2)}% compared to {prev_month})")
