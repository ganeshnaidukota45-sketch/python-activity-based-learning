
# Tuple-Based Route Distance Analysis

import math

print("=" * 60)
print("       TUPLE-BASED ROUTE DISTANCE ANALYSIS")
print("=" * 60)

# Haversine formula calculates distance between two coordinates
# Coordinates are stored as tuples: (latitude, longitude)
def calculate_distance(point1, point2):
    R = 6371.0  # Earth's radius in kilometres

    lat1, lon1 = point1
    lat2, lon2 = point2

    # Convert degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    # Protect against floating-point rounding errors
    a = max(0.0, min(1.0, a))

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


# Validate geographic coordinates
def get_coordinate(prompt, minimum, maximum):
    while True:
        try:
            value = float(input(prompt))

            if minimum <= value <= maximum:
                return value

            print(f"Enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Invalid input. Please enter a number.")


# Input route points
while True:
    try:
        n = int(input("Enter number of route points (minimum 2): "))

        if n >= 2:
            break

        print("At least two points are required.")

    except ValueError:
        print("Enter a valid integer.")

route = []

for i in range(n):
    print(f"\nRoute Point {i + 1}")

    latitude = get_coordinate(
        "Enter latitude (-90 to 90): ", -90, 90
    )

    longitude = get_coordinate(
        "Enter longitude (-180 to 180): ", -180, 180
    )

    # Store coordinates as an immutable tuple
    coordinate = (latitude, longitude)
    route.append(coordinate)

# Calculate successive segment distances
distances = []
total_distance = 0.0

print("\n" + "=" * 65)
print("                 ROUTE SEGMENT DETAILS")
print("=" * 65)

for i in range(len(route) - 1):
    start = route[i]
    end = route[i + 1]

    distance = calculate_distance(start, end)
    distances.append(distance)
    total_distance += distance

    print(f"\nSegment {i + 1}: Point {i + 1} -> Point {i + 2}")
    print(f"Start Coordinate: {start}")
    print(f"End Coordinate:   {end}")
    print(f"Distance:         {distance:.3f} km")

# Identify the longest segment
longest_index = distances.index(max(distances))
longest_distance = distances[longest_index]

# Display final analysis
print("\n" + "=" * 65)
print("                   ROUTE ANALYSIS")
print("=" * 65)

print(f"Total Route Points: {len(route)}")
print(f"Total Route Segments: {len(distances)}")
print(f"Total Route Distance: {total_distance:.3f} km")

print(f"\nLongest Segment: Segment {longest_index + 1}")
print(
    f"From Point {longest_index + 1} "
    f"to Point {longest_index + 2}"
)
print(f"Longest Segment Distance: {longest_distance:.3f} km")

print("\nAll Coordinates:")
for i, point in enumerate(route, start=1):
    print(f"Point {i}: {point}")

print("=" * 65)
print("Route distance analysis completed.")
