
# Sports Tournament Ranking System

print("=" * 65)
print("           SPORTS TOURNAMENT RANKING SYSTEM")
print("=" * 65)

# Competition policy
WIN_POINTS = 3
DRAW_POINTS = 1
LOSS_POINTS = 0

# Input number of teams
while True:
    try:
        num_teams = int(input("Enter number of teams: "))
        if num_teams >= 2:
            break
        print("At least 2 teams are required.")
    except ValueError:
        print("Please enter a valid integer.")

teams = {}

# Register teams
for i in range(num_teams):
    name = input(f"Enter team {i + 1} name: ").strip()

    while not name or name in teams:
        print("Team name must be unique and non-empty.")
        name = input(f"Enter team {i + 1} name: ").strip()

    teams[name] = {
        "played": 0,
        "won": 0,
        "drawn": 0,
        "lost": 0,
        "points": 0,
        "score_for": 0,
        "score_against": 0,
        "goal_difference": 0
    }

# Input match results
while True:
    try:
        num_matches = int(input("\nEnter number of matches played: "))
        if num_matches >= 0:
            break
        print("Number of matches cannot be negative.")
    except ValueError:
        print("Please enter a valid integer.")

match_results = []

for i in range(num_matches):
    print(f"\n--- Match {i + 1} ---")

    print("Teams:", ", ".join(teams.keys()))

    team1 = input("Enter first team: ").strip()
    team2 = input("Enter second team: ").strip()

    if team1 not in teams or team2 not in teams:
        print("Invalid team name. Match skipped.")
        continue

    if team1 == team2:
        print("A team cannot play against itself. Match skipped.")
        continue

    try:
        score1 = int(input(f"Enter score for {team1}: "))
        score2 = int(input(f"Enter score for {team2}: "))

        if score1 < 0 or score2 < 0:
            print("Scores cannot be negative. Match skipped.")
            continue
    except ValueError:
        print("Invalid score. Match skipped.")
        continue

    match_results.append((team1, team2, score1, score2))

    # Update statistics
    teams[team1]["played"] += 1
    teams[team2]["played"] += 1

    teams[team1]["score_for"] += score1
    teams[team1]["score_against"] += score2

    teams[team2]["score_for"] += score2
    teams[team2]["score_against"] += score1

    # Award points
    if score1 > score2:
        teams[team1]["won"] += 1
        teams[team2]["lost"] += 1
        teams[team1]["points"] += WIN_POINTS
        teams[team2]["points"] += LOSS_POINTS

    elif score2 > score1:
        teams[team2]["won"] += 1
        teams[team1]["lost"] += 1
        teams[team2]["points"] += WIN_POINTS
        teams[team1]["points"] += LOSS_POINTS

    else:
        teams[team1]["drawn"] += 1
        teams[team2]["drawn"] += 1
        teams[team1]["points"] += DRAW_POINTS
        teams[team2]["points"] += DRAW_POINTS

# Calculate score difference
for name in teams:
    teams[name]["goal_difference"] = (
        teams[name]["score_for"]
        - teams[name]["score_against"]
    )

# Ranking policy:
# 1. Total points (highest first)
# 2. Goal/score difference (highest first)
# 3. Total scores for (highest first)
# 4. Team name (alphabetical order)

ranked_teams = sorted(
    teams.items(),
    key=lambda item: (
        -item[1]["points"],
        -item[1]["goal_difference"],
        -item[1]["score_for"],
        item[0].lower()
    )
)

# Display match results
print("\n" + "=" * 65)
print("                    MATCH RESULTS")
print("=" * 65)

if match_results:
    for i, (team1, team2, score1, score2) in enumerate(
        match_results, start=1
    ):
        print(f"{i}. {team1} {score1} - {score2} {team2}")
else:
    print("No valid matches recorded.")

# Display final rankings
print("\n" + "=" * 100)
print("                    FINAL TOURNAMENT RANKINGS")
print("=" * 100)

print(
    f"{'Rank':<6}{'Team':<20}{'P':>5}{'W':>5}"
    f"{'D':>5}{'L':>5}{'SF':>7}{'SA':>7}"
    f"{'Diff':>8}{'Points':>9}"
)

print("-" * 100)

for rank, (name, stats) in enumerate(ranked_teams, start=1):
    print(
        f"{rank:<6}{name:<20}{stats['played']:>5}"
        f"{stats['won']:>5}{stats['drawn']:>5}"
        f"{stats['lost']:>5}{stats['score_for']:>7}"
        f"{stats['score_against']:>7}"
        f"{stats['goal_difference']:>8}"
        f"{stats['points']:>9}"
    )

print("-" * 100)

if ranked_teams:
    print("Tournament Leader:", ranked_teams[0][0])

print("\nRanking Policy:")
print("1. Highest total points")
print("2. Highest score difference")
print("3. Highest total scores")
print("4. Alphabetical team name if still tied")

print("=" * 65)
print("Tournament ranking completed.")
