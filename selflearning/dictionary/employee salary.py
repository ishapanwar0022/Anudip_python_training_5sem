# Dictionary containing employee salaries
salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# Employees earning above 60000
print("Employees earning above 60000:")
for emp, sal in salary.items():
    if sal > 60000:
        print(emp, "-", sal)

# Count employees earning below 40000
count = 0
for sal in salary.values():
    if sal < 40000:
        count += 1
print("Employees earning below 40000:", count)

# Highest paid employee
highest = max(salary, key=salary.get)
print("Highest Paid Employee:", highest, "-", salary[highest])

# Employees eligible for bonus
bonus = []
for emp, sal in salary.items():
    if sal > 50000:
        bonus.append(emp)
print("Bonus Eligible Employees:", bonus)

# Average salary
average = sum(salary.values()) / len(salary)
print("Average Salary:", average)