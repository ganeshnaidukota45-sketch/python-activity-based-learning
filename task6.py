
# Student Performance Trend Analysis System

print("=" * 60)
print("       STUDENT PERFORMANCE TREND ANALYSIS")
print("=" * 60)

# Student details
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

# Input validation
while True:
    try:
        num_subjects = int(input("Enter number of subjects: "))
        num_exams = int(input("Enter number of examinations: "))
        max_marks = float(input("Enter maximum marks per subject: "))

        if num_subjects <= 0 or num_exams < 2 or max_marks <= 0:
            print("Enter positive subjects and maximum marks,")
            print("and at least 2 examinations.")
            continue

        break
    except ValueError:
        print("Invalid input. Enter valid numbers.")

subjects = []
scores = {}

# Enter subject names
for i in range(num_subjects):
    subject = input(f"Enter subject {i + 1} name: ").strip()

    while not subject or subject in subjects:
        print("Subject name must be non-empty and unique.")
        subject = input(f"Enter subject {i + 1} name: ").strip()

    subjects.append(subject)
    scores[subject] = []

# Enter examination scores
for exam in range(num_exams):
    print(f"\n--- Examination {exam + 1} ---")

    for subject in subjects:
        while True:
            try:
                marks = float(
                    input(f"Enter marks for {subject}: ")
                )

                if 0 <= marks <= max_marks:
                    scores[subject].append(marks)
                    break

                print(f"Marks must be between 0 and {max_marks}.")

            except ValueError:
                print("Please enter a valid numeric score.")

# Analyze performance
print("\n" + "=" * 75)
print("                 PERFORMANCE REPORT")
print("=" * 75)

print("Student Name:", student_name)
print("Roll Number:", roll_number)

total_improvement = 0
total_decline = 0
weak_subjects = []
total_score = 0
total_possible = num_subjects * num_exams * max_marks

for subject in subjects:
    marks_list = scores[subject]

    first_score = marks_list[0]
    latest_score = marks_list[-1]
    change = latest_score - first_score
    average = sum(marks_list) / num_exams

    total_score += sum(marks_list)

    # Identify improvement or decline
    if change > 0:
        trend = "Improved"
        total_improvement += change
    elif change < 0:
        trend = "Declined"
        total_decline += abs(change)
    else:
        trend = "Unchanged"

    # A subject is weak if every exam score is below 40%
    if all(mark < max_marks * 0.40 for mark in marks_list):
        weak_subjects.append(subject)

    print("\nSubject:", subject)
    print("Examination Scores:", marks_list)
    print(f"Average Score: {average:.2f}/{max_marks:.2f}")
    print(f"First Exam Score: {first_score:.2f}")
    print(f"Latest Exam Score: {latest_score:.2f}")
    print(f"Change: {change:+.2f}")
    print("Trend:", trend)

# Overall performance
overall_percentage = (total_score / total_possible) * 100

print("\n" + "=" * 60)
print("             OVERALL PERFORMANCE")
print("=" * 60)

print(f"Overall Percentage: {overall_percentage:.2f}%")
print(f"Total Improvement: {total_improvement:.2f} marks")
print(f"Total Decline: {total_decline:.2f} marks")

# Classification criteria
if overall_percentage >= 90:
    classification = "Outstanding"
elif overall_percentage >= 75:
    classification = "Excellent"
elif overall_percentage >= 60:
    classification = "Good"
elif overall_percentage >= 40:
    classification = "Average"
else:
    classification = "Needs Improvement"

print("Student Classification:", classification)

# Display weak subjects
if weak_subjects:
    print("Consistently Weak Subjects:", ", ".join(weak_subjects))
else:
    print("Consistently Weak Subjects: None")

# Suggestions
print("\n--- RECOMMENDATIONS ---")

if weak_subjects:
    print("Focus on practice and revision in:")
    for subject in weak_subjects:
        print("-", subject)

if total_improvement > total_decline:
    print("Overall score changes show more improvement than decline.")
elif total_decline > total_improvement:
    print("Review subjects with declining scores.")
else:
    print("Overall improvement and decline are balanced.")

print("=" * 60)
print("Performance analysis completed.")
