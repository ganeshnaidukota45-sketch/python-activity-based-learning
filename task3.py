
# Examination Result and Grace-Mark Validation System

print("=" * 55)
print("     EXAMINATION RESULT & GRACE-MARK VALIDATION")
print("=" * 55)

# Student details
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

num_subjects = int(input("Enter number of subjects: "))
max_marks = float(input("Enter maximum marks per subject: "))
pass_marks = float(input("Enter minimum passing marks: "))
grace_limit = float(input("Enter maximum grace marks per subject: "))

# Validate basic rules
if num_subjects <= 0 or max_marks <= 0:
    print("Error: Subjects and maximum marks must be positive.")
    raise SystemExit

if not (0 <= pass_marks <= max_marks):
    print("Error: Passing marks must be within the maximum marks.")
    raise SystemExit

if not (0 <= grace_limit <= max_marks):
    print("Error: Grace marks must be between 0 and maximum marks.")
    raise SystemExit

subjects = []
original_marks = []
final_marks = []
grace_awarded = []

# Collect marks
for i in range(num_subjects):
    print(f"\nSubject {i + 1}")
    subject = input("Enter subject name: ")
    marks = float(input("Enter marks obtained: "))

    if marks < 0 or marks > max_marks:
        print(f"Invalid marks! Enter marks between 0 and {max_marks}.")
        raise SystemExit

    subjects.append(subject)
    original_marks.append(marks)

# Apply grace marks only when needed to pass a subject.
# Grace marks cannot exceed the configured per-subject limit.
for i in range(num_subjects):
    marks = original_marks[i]
    grace = 0

    if marks < pass_marks:
        required = pass_marks - marks

        if required <= grace_limit:
            grace = required

    adjusted_marks = min(marks + grace, max_marks)

    grace_awarded.append(grace)
    final_marks.append(adjusted_marks)

# Calculate result
total_marks = sum(final_marks)
maximum_total = num_subjects * max_marks
percentage = (total_marks / maximum_total) * 100

failed_subjects = [
    subjects[i]
    for i in range(num_subjects)
    if final_marks[i] < pass_marks
]

if failed_subjects:
    result = "FAIL"
    classification = "Not Classified"
elif percentage >= 75:
    result = "PASS"
    classification = "Distinction"
elif percentage >= 60:
    result = "PASS"
    classification = "First Class"
elif percentage >= 50:
    result = "PASS"
    classification = "Second Class"
else:
    result = "PASS"
    classification = "Third Class"

# Display final report
print("\n" + "=" * 65)
print("                 FINAL EXAMINATION REPORT")
print("=" * 65)

print("Student Name:", student_name)
print("Roll Number:", roll_number)

print("-" * 65)
print(f"{'Subject':<20}{'Original':>12}{'Grace':>10}{'Final':>12}")
print("-" * 65)

for i in range(num_subjects):
    print(
        f"{subjects[i]:<20}"
        f"{original_marks[i]:>12.2f}"
        f"{grace_awarded[i]:>10.2f}"
        f"{final_marks[i]:>12.2f}"
    )

print("-" * 65)
print(f"Total Marks: {total_marks:.2f} / {maximum_total:.2f}")
print(f"Percentage: {percentage:.2f}%")
print("Final Result:", result)
print("Classification:", classification)

if failed_subjects:
    print("Failed Subjects:", ", ".join(failed_subjects))
else:
    print("All subjects passed.")

print("Total Grace Marks Awarded:", sum(grace_awarded))
print("=" * 65)
print("Result processing completed.")
