
from datetime import datetime
import math

# Smart Parking Fee Management System

print("=" * 55)
print("       SMART PARKING FEE MANAGEMENT SYSTEM")
print("=" * 55)

# Parking rates (rupees per hour)
vehicle_rates = {
    "bike": 20,
    "car": 40,
    "truck": 60
}

DAILY_LIMIT = 300
OVERNIGHT_FEE = 50
PENALTY_FEE = 100
MAX_PARKING_DAYS = 30

# Read and validate date/time
def get_datetime(prompt):
    while True:
        value = input(prompt)
        try:
            return datetime.strptime(value, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid format! Use YYYY-MM-DD HH:MM.")

# Vehicle category
while True:
    vehicle = input(
        "Enter vehicle category (bike/car/truck): "
    ).strip().lower()

    if vehicle in vehicle_rates:
        break

    print("Invalid category. Please try again.")

# Vehicle number
vehicle_number = input("Enter vehicle registration number: ").strip()

while not vehicle_number:
    print("Vehicle number cannot be empty.")
    vehicle_number = input("Enter vehicle registration number: ").strip()

# Get parking times
entry_time = get_datetime("Enter entry time (YYYY-MM-DD HH:MM): ")
exit_time = get_datetime("Enter exit time (YYYY-MM-DD HH:MM): ")

# Validate time range
if exit_time <= entry_time:
    print("\nError: Exit time must be after entry time.")
    raise SystemExit

duration_seconds = (exit_time - entry_time).total_seconds()
duration_hours = duration_seconds / 3600
charged_hours = math.ceil(duration_hours)

calendar_days = (
    (exit_time.date() - entry_time.date()).days + 1
)

if duration_hours > MAX_PARKING_DAYS * 24:
    print("Error: Parking duration cannot exceed 30 days.")
    raise SystemExit

# Calculate base charges
hourly_rate = vehicle_rates[vehicle]
raw_charge = charged_hours * hourly_rate

# Apply a daily limit to each 24-hour parking period
complete_days = int(duration_hours // 24)
remaining_hours = charged_hours - complete_days * 24

daily_charge = min(24 * hourly_rate, DAILY_LIMIT)
base_charge = complete_days * daily_charge

if remaining_hours > 0:
    base_charge += min(remaining_hours * hourly_rate, DAILY_LIMIT)

# Count overnight periods: each midnight crossed
overnight_count = (
    (exit_time.date() - entry_time.date()).days
)

overnight_charge = overnight_count * OVERNIGHT_FEE

# Penalty conditions
# Example: penalty applies if parking lasts more than 12 hours.
penalty = 0
if duration_hours > 12:
    penalty = PENALTY_FEE

# Total fee
total_fee = base_charge + overnight_charge + penalty

# Display parking receipt
print("\n" + "=" * 55)
print("                PARKING RECEIPT")
print("=" * 55)

print("Vehicle Number:", vehicle_number)
print("Vehicle Category:", vehicle.title())
print("Entry Time:", entry_time.strftime("%d-%m-%Y %H:%M"))
print("Exit Time:", exit_time.strftime("%d-%m-%Y %H:%M"))
print(f"Parking Duration: {duration_hours:.2f} hours")
print("Charged Hours:", charged_hours)
print(f"Hourly Rate: Rs. {hourly_rate:.2f}")

print("-" * 55)
print(f"Parking Charge:    Rs. {base_charge:.2f}")
print(f"Overnight Charge:  Rs. {overnight_charge:.2f}")
print(f"Penalty:           Rs. {penalty:.2f}")
print("-" * 55)
print(f"TOTAL FEE:         Rs. {total_fee:.2f}")
print("=" * 55)
print("Thank you for using Smart Parking!")
