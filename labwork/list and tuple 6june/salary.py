# Employee data
employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

print("Employees earning above 50000:")

# Display employees earning above 50000
for name, salary in employees:
    if salary > 50000:
        print(name, salary)

# Find highest-paid employee
highest = employees[0]

for emp in employees:
    if emp[1] > highest[1]:
        highest = emp

print("Highest Paid Employee =", highest[0])
print("Salary =", highest[1])

# Calculate total salary expenditure
total_salary = 0

for name, salary in employees:
    total_salary += salary

print("Total Salary Expenditure =", total_salary)

# Count employees earning below 40000
count = 0

for name, salary in employees:
    if salary < 40000:
        count += 1

print("Employees earning below 40000 =", count)