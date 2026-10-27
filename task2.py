
# Campus Event Financial Planning System

print("=" * 50)
print("      CAMPUS EVENT FINANCIAL PLANNER")
print("=" * 50)

# Get event details
event_name = input("Enter event name: ")
participants = int(input("Expected number of participants: "))

print("\nEnter event expenses (in Rs.)")

venue = float(input("Venue cost: Rs. "))
equipment = float(input("Equipment cost: Rs. "))
catering_per_person = float(input("Catering cost per person: Rs. "))
transport_per_person = float(input("Transport cost per person: Rs. "))
certificate_per_person = float(input("Certificate cost per person: Rs. "))

# Financial contributions
registration_fee = float(input("Registration fee per participant: Rs. "))
sponsorship = float(input("Total sponsorship received: Rs. "))

# Calculate costs
fixed_cost = venue + equipment

variable_cost_per_person = (
    catering_per_person
    + transport_per_person
    + certificate_per_person
)

total_variable_cost = variable_cost_per_person * participants
total_cost = fixed_cost + total_variable_cost

# Calculate income
registration_income = registration_fee * participants
total_income = registration_income + sponsorship

# Calculate sponsorship shortfall
shortfall = max(0, total_cost - total_income)

# Calculate break-even registrations
contribution_per_person = registration_fee - variable_cost_per_person

if contribution_per_person > 0:
    remaining_fixed_cost = max(0, fixed_cost - sponsorship)
    break_even = (
        int(remaining_fixed_cost // contribution_per_person)
        + (1 if remaining_fixed_cost % contribution_per_person > 0 else 0)
    )
else:
    break_even = None

# Display financial report
print("\n" + "=" * 50)
print("           EVENT FINANCIAL REPORT")
print("=" * 50)

print("Event Name:", event_name)
print("Expected Participants:", participants)

print("\n--- EXPENSE DETAILS ---")
print(f"Venue Cost:              Rs. {venue:.2f}")
print(f"Equipment Cost:          Rs. {equipment:.2f}")
print(f"Catering Cost:           Rs. {catering_per_person * participants:.2f}")
print(f"Transport Cost:          Rs. {transport_per_person * participants:.2f}")
print(f"Certificate Cost:        Rs. {certificate_per_person * participants:.2f}")
print(f"Total Event Cost:        Rs. {total_cost:.2f}")

print("\n--- INCOME DETAILS ---")
print(f"Registration Income:     Rs. {registration_income:.2f}")
print(f"Sponsorship:             Rs. {sponsorship:.2f}")
print(f"Total Income:            Rs. {total_income:.2f}")

print("\n--- FINANCIAL SUMMARY ---")
print(f"Participant Fee:         Rs. {registration_fee:.2f}")
print(f"Variable Cost/Person:    Rs. {variable_cost_per_person:.2f}")
print(f"Sponsorship Shortfall:   Rs. {shortfall:.2f}")

if total_income > total_cost:
    print(f"Event Surplus:            Rs. {total_income - total_cost:.2f}")
elif total_income == total_cost:
    print("Event Status: Break-even")
else:
    print(f"Event Deficit:            Rs. {total_cost - total_income:.2f}")

if break_even is not None:
    print("Minimum Registrations for Break-even:", break_even)

    if break_even > participants:
        print("Warning: More registrations are needed.")
else:
    print("Break-even is not possible with the current fee.")
    print("Increase the registration fee or obtain more sponsorship.")

print("=" * 50)
print("Financial planning completed.")
