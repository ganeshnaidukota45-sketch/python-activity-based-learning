
# Nested List Classroom Occupancy Analysis

print("=" * 60)
print("       CLASSROOM OCCUPANCY ANALYSIS SYSTEM")
print("=" * 60)

# Classroom configuration
classrooms = {}
reserved_seats = {}
assigned_students = set()

num_classrooms = int(input("Enter number of classrooms: "))

if num_classrooms <= 0:
    print("Error: Number of classrooms must be positive.")
    raise SystemExit

# Create nested lists for classrooms and seats
for c in range(num_classrooms):
    room_name = input(f"\nEnter classroom name {c + 1}: ").strip()

    while not room_name or room_name in classrooms:
        print("Classroom name must be unique and non-empty.")
        room_name = input("Enter classroom name: ").strip()

    rows = int(input("Enter number of seating rows: "))
    columns = int(input("Enter seats per row: "))

    if rows <= 0 or columns <= 0:
        print("Error: Rows and columns must be positive.")
        raise SystemExit

    # None means vacant; student name means occupied
    classrooms[room_name] = [
        [None for _ in range(columns)]
        for _ in range(rows)
    ]

    reserved_seats[room_name] = set()

    # Reserve seats using 1-based row and seat numbers
    count = int(input("Enter number of reserved seats: "))

    if count < 0 or count > rows * columns:
        print("Error: Invalid number of reserved seats.")
        raise SystemExit

    for i in range(count):
        print(f"Reserved seat {i + 1}")
        r = int(input(f"Row (1-{rows}): "))
        s = int(input(f"Seat number (1-{columns}): "))

        if not (1 <= r <= rows and 1 <= s <= columns):
            print("Error: Invalid seat position.")
            raise SystemExit

        position = (r - 1, s - 1)

        if position in reserved_seats[room_name]:
            print("Error: Seat already reserved.")
            raise SystemExit

        reserved_seats[room_name].add(position)

# Allocate students
num_students = int(input("\nEnter number of students to allocate: "))

if num_students < 0:
    print("Error: Student count cannot be negative.")
    raise SystemExit

for i in range(num_students):
    print(f"\nStudent {i + 1}")
    student = input("Enter student name or ID: ").strip()

    while not student:
        student = input("Student ID cannot be empty: ").strip()

    # Detect duplicate student assignments
    if student in assigned_students:
        print("Duplicate assignment detected! Student already allocated.")
        continue

    room_name = input("Enter classroom name: ").strip()

    if room_name not in classrooms:
        print("Invalid classroom. Student was not allocated.")
        continue

    room = classrooms[room_name]
    allocated = False

    # Allocate the first available non-reserved seat
    for r in range(len(room)):
        for s in range(len(room[r])):
            position = (r, s)

            if (
                room[r][s] is None
                and position not in reserved_seats[room_name]
            ):
                room[r][s] = student
                assigned_students.add(student)
                print(
                    f"Allocated {student} to {room_name}, "
                    f"Row {r + 1}, Seat {s + 1}"
                )
                allocated = True
                break

        if allocated:
            break

    if not allocated:
        print(f"No available seats in {room_name}.")

# Display classroom seating and occupancy report
print("\n" + "=" * 70)
print("                 CLASSROOM OCCUPANCY REPORT")
print("=" * 70)

total_capacity = 0
total_occupied = 0
total_reserved = 0
total_vacant = 0

for room_name, room in classrooms.items():
    rows = len(room)
    columns = len(room[0])

    capacity = rows * columns
    reserved = len(reserved_seats[room_name])
    occupied = sum(
        1 for row in room for seat in row if seat is not None
    )
    vacant = capacity - occupied - reserved

    total_capacity += capacity
    total_occupied += occupied
    total_reserved += reserved
    total_vacant += vacant

    print(f"\nClassroom: {room_name}")
    print("-" * 50)

    for r, row in enumerate(room):
        display_row = []

        for s, seat in enumerate(row):
            if (r, s) in reserved_seats[room_name]:
                display_row.append("[RESERVED]")
            elif seat is None:
                display_row.append("[VACANT]")
            else:
                display_row.append(f"[{seat}]")

        print(f"Row {r + 1}: " + " ".join(display_row))

    print(f"Total Capacity: {capacity}")
    print(f"Occupied Seats: {occupied}")
    print(f"Reserved Seats: {reserved}")
    print(f"Vacant Seats: {vacant}")

# Overall summary
print("\n" + "=" * 60)
print("                 OVERALL SUMMARY")
print("=" * 60)

print("Total Classrooms:", len(classrooms))
print("Total Seating Capacity:", total_capacity)
print("Total Students Allocated:", total_occupied)
print("Total Reserved Seats:", total_reserved)
print("Total Vacant Seats:", total_vacant)

if total_capacity > 0:
    occupancy_rate = (total_occupied / total_capacity) * 100
    print(f"Occupancy Rate: {occupancy_rate:.2f}%")

print("=" * 60)
print("Classroom analysis completed.")
