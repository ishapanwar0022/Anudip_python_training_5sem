# Employee Performance Dashboard

# Creating a dictionary to store employee performance scores

performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# ----------------------------------------------------
# Display employees scoring above 80

print("Employees Scoring Above 80:")

for emp, score in performance.items():
    if score > 80:
        print(emp)

# ----------------------------------------------------
# Count employees needing improvement (score < 60)

improvement_count = 0

for score in performance.values():
    if score < 60:
        improvement_count += 1

print("Employees Needing Improvement:", improvement_count)

# ----------------------------------------------------
# Find top performer

dict_items = list(performance.items())

top_employee = dict_items[0][0]
top_score = dict_items[0][1]

for item in dict_items:
    if item[1] > top_score:
        top_employee = item[0]
        top_score = item[1]

print("Top Performer:", top_employee, "with score:", top_score)

# ----------------------------------------------------
# Calculate average performance score

total_score = 0

for score in performance.values():
    total_score = total_score + score

average_score = total_score / len(performance)

print("Average Score:", average_score)

# ----------------------------------------------------
# Create separate lists

excellent = []
good = []
average = []
poor = []

for emp, score in performance.items():

    if score >= 90:
        excellent.append(emp)

    elif score >= 75:
        good.append(emp)

    elif score >= 60:
        average.append(emp)

    else:
        poor.append(emp)

print("Excellent:")
print(excellent)

print("Good:")
print(good)

print("Average:")
print(average)

print("Poor:")
print(poor)

# ----------------------------------------------------
# Display all employee records

print("All Employee Records:")
print(performance)