# Employee records stored in a tuple
# Format: (Employee ID, Employee Name, Performance Score)

employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)


# 1. Display employees scoring 80 or above


print("Employees Scoring 80 or Above:")

for emp_id, name, score in employees:
    if score >= 80:
        print(emp_id, name, score)


# 2. Count employees who need improvement
#    (Score below 60)

improvement_count = 0

for emp_id, name, score in employees:
    if score < 60:
        improvement_count += 1

print("\nEmployees Needing Improvement =", improvement_count)


# 3. Find employee with highest score

highest = employees[0]

for employee in employees:
    if employee[2] > highest[2]:
        highest = employee

print("\nHighest Performer:")
print(highest[0], highest[1], highest[2])


# 4. Create list of employees scoring above 75

high_performers = []

for emp_id, name, score in employees:
    if score > 75:
        high_performers.append(name)

print("\nHigh Performers:")
print(high_performers)


# 5. Display performance category


print("\nPerformance Categories:")

for emp_id, name, score in employees:

    if score >= 90:
        category = "Excellent"

    elif score >= 75:
        category = "Good"

    elif score >= 60:
        category = "Average"

    else:
        category = "Needs Improvement"

    print(name, "->", category)