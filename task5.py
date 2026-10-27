
# Multi-Day Water Tank Simulation

print("=" * 55)
print("       MULTI-DAY WATER TANK SIMULATION")
print("=" * 55)

# Get tank details
capacity = float(input("Enter tank capacity (litres): "))
initial_water = float(input("Enter initial water level (litres): "))
threshold = float(input("Enter target water threshold (litres): "))
days = int(input("Enter number of days to simulate: "))

# Validate input
if capacity <= 0:
    print("Error: Tank capacity must be positive.")
    raise SystemExit

if not 0 <= initial_water <= capacity:
    print("Error: Initial water must be between 0 and capacity.")
    raise SystemExit

if not 0 <= threshold <= capacity:
    print("Error: Threshold must be between 0 and capacity.")
    raise SystemExit

if days <= 0:
    print("Error: Number of days must be positive.")
    raise SystemExit

# Initialize variables
water_level = initial_water
first_threshold_day = 0 if water_level >= threshold else None
total_overflow = 0
total_shortage = 0

print("\nEnter inflow and outflow for each day.")
print("All quantities must be in litres.")

print("\n" + "=" * 75)
print(
    f"{'Day':<8}{'Inflow':>12}{'Outflow':>12}"
    f"{'Overflow':>12}{'Shortage':>12}{'Final Level':>15}"
)
print("=" * 75)

# Daily simulation
for day in range(1, days + 1):

    print(f"\nDay {day}")
    inflow = float(input("Enter water inflow: "))
    outflow = float(input("Enter requested water outflow: "))

    if inflow < 0 or outflow < 0:
        print("Error: Inflow and outflow cannot be negative.")
        raise SystemExit

    # Add incoming water
    water_level += inflow

    # Detect overflow
    overflow = max(0, water_level - capacity)
    water_level = min(water_level, capacity)

    # Remove outgoing water
    shortage = max(0, outflow - water_level)
    actual_outflow = min(outflow, water_level)
    water_level -= actual_outflow

    # Update totals
    total_overflow += overflow
    total_shortage += shortage

    # Detect first day threshold is reached
    if first_threshold_day is None and water_level >= threshold:
        first_threshold_day = day

    # Display daily result
    print(
        f"{day:<8}{inflow:>12.2f}{outflow:>12.2f}"
        f"{overflow:>12.2f}{shortage:>12.2f}"
        f"{water_level:>15.2f}"
    )

# Final report
print("\n" + "=" * 55)
print("             SIMULATION SUMMARY")
print("=" * 55)

print(f"Tank Capacity:       {capacity:.2f} litres")
print(f"Initial Water:       {initial_water:.2f} litres")
print(f"Final Water Level:   {water_level:.2f} litres")
print(f"Total Overflow:      {total_overflow:.2f} litres")
print(f"Total Shortage:      {total_shortage:.2f} litres")
print(f"Target Threshold:    {threshold:.2f} litres")

if first_threshold_day is not None:
    if first_threshold_day == 0:
        print("Threshold was already reached initially.")
    else:
        print(f"First Reached On: Day {first_threshold_day}")
else:
    print("Threshold was not reached during the simulation.")

print("=" * 55)
print("Water tank simulation completed.")
