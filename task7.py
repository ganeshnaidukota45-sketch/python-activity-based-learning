
# Multi-Event Sports Scheduling and Scoring

# Event schedule stored as a list of tuples
# Each tuple contains: (Event Name, Team 1, Team 2, Time)

schedule = [
    ("Cricket", "Team A", "Team B", "10:00"),
    ("Football", "Team C", "Team D", "10:00"),
    ("Volleyball", "Team A", "Team C", "11:00"),
    ("Basketball", "Team B", "Team D", "12:00"),
    ("Badminton", "Team A", "Team D", "13:00")
]

# Match results stored as tuples
# Each tuple contains: (Event, Team 1, Score 1, Team 2, Score 2)

results = [
    ("Cricket", "Team A", 3, "Team B", 1),
    ("Football", "Team C", 2, "Team D", 1),
    ("Volleyball", "Team A", 1, "Team C", 2),
    ("Basketball", "Team B", 3, "Team D", 2),
    ("Badminton", "Team A", 2, "Team D", 0)
]

# 1. Display event schedule
print("===== SPORTS EVENT SCHEDULE =====")

for event in schedule:
    print(event[0], "-", event[1], "vs", event[2],
          "at", event[3])

# 2. Identify scheduling conflicts
print("\n===== SCHEDULING CONFLICTS =====")

conflict_found = False

for i in range(len(schedule)):
    for j in range(i + 1, len(schedule)):
        event1 = schedule[i]
        event2 = schedule[j]

        # Check whether a team plays in two events
        # at the same time
        if event1[3] == event2[3]:
            teams1 = (event1[1], event1[2])
            teams2 = (event2[1], event2[2])

            common_teams = set(teams1) & set(teams2)

            if common_teams:
                print("Conflict:", event1[0], "and",
                      event2[0], "at", event1[3],
                      "- Teams:", ", ".join(sorted(common_teams)))
                conflict_found = True

if not conflict_found:
    print("No scheduling conflicts found.")

# 3. Calculate points for each team
points = {}

for result in results:
    event, team1, score1, team2, score2 = result

    # Initialize teams
    if team1 not in points:
        points[team1] = 0
    if team2 not in points:
        points[team2] = 0

    # Winner gets 3 points; draw gives 1 point each
    if score1 > score2:
        points[team1] += 3
    elif score2 > score1:
        points[team2] += 3
    else:
        points[team1] += 1
        points[team2] += 1

# 4. Generate final rankings
print("\n===== FINAL TEAM RANKINGS =====")

rankings = sorted(
    points.items(),
    key=lambda item: item[1],
    reverse=True
)

for rank, (team, total_points) in enumerate(rankings, start=1):
    print(f"Rank {rank}: {team} - {total_points} points")

print("\nSports scheduling and scoring completed!")

