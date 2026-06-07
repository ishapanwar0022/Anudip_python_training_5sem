# Dictionary containing student names and marks
marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# Display students scoring 80 or above
print("Students scoring 80 or above:")
for student, mark in marks.items():
    if mark >= 80:
        print(student, "-", mark)

# Count failed students
fail_count = 0
for mark in marks.values():
    if mark < 40:
        fail_count += 1
print("Failed Students:", fail_count)

# Find highest scorer
highest = max(marks, key=marks.get)
print("Highest Scorer:", highest, "-", marks[highest])

# Students scoring between 60 and 75
between_60_75 = []
for student, mark in marks.items():
    if 60 <= mark <= 75:
        between_60_75.append(student)
print("Students scoring between 60 and 75:", between_60_75)

# Assign grades
print("\nGrades:")
for student, mark in marks.items():
    if mark >= 90:
        grade = "A"
    elif mark >= 75:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    else:
        grade = "F"

    print(student, ":", grade)