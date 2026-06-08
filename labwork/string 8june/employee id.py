1. #Employee ID Validation and Analysis System 
'''Problem Statement 
A company generates employee IDs in the following format: 
EMP2026ANUJ458 
Tasks 
Write a program to: 
1. Count the number of uppercase letters.  
2. Count the number of digits.  
3. Extract the joining year.  
4. Extract the employee name.  
5. Check whether the ID follows these rules:  
o Starts with "EMP"  
o Contains exactly 4 digits for the year  
o Ends with exactly 3 digits  
6. Create a list containing all digits present in the ID.  
7. Find the sum of all digits present in the ID.  
8. Display whether the ID is valid or invalid. '''     


# Employee ID Validation and Analysis System

emp_id = input("Enter Employee ID: ")

upper = 0
digit_count = 0
digit_list = []
digit_sum = 0

# Count uppercase letters and digits
for ch in emp_id:
    if ch.isupper():
        upper += 1

    if ch.isdigit():
        digit_count += 1
        digit_list.append(int(ch))
        digit_sum += int(ch)

# Extract year and employee name
year = emp_id[3:7]
name = emp_id[7:-3]

# Validation
if emp_id.startswith("EMP") and year.isdigit() and emp_id[-3:].isdigit():
    status = "Valid"
else:
    status = "Invalid"

print("Uppercase Letters =", upper)
print("Digits =", digit_count)
print("Joining Year =", year)
print("Employee Name =", name)
print("Digit List =", digit_list)
print("Sum of Digits =", digit_sum)
print("ID Status =", status)