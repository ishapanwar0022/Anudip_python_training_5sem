# Dictionary of quiz scores
quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# Display students scoring 15 or above
print("Students scoring 15 or above:")
for student, score in quiz_scores.items():
    if score >= 15:
        print(student, ":", score)

# Count students scoring below 10
count = 0
for score in quiz_scores.values():
    if score < 10:
        count += 1
print("\nStudents scoring below 10:", count)

# Find the top performer
top_student = max(quiz_scores, key=quiz_scores.get)
print("\nTop Performer:", top_student)
print("Score:", quiz_scores[top_student])

# Create a list of students who passed
passed = []
for student, score in quiz_scores.items():
    if score >= 10:
        passed.append(student)
print("\nStudents who passed:")
print(passed)

# Calculate class average
average = sum(quiz_scores.values()) / len(quiz_scores)
print("\nClass Average:", average)