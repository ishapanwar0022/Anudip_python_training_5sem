
#4. Vehicle Number Plate Verification 
'''Problem Statement 
A vehicle number plate is entered: 
MH12AB4589 
Tasks 
Write a program to: 
1. Extract state code.  
2. Extract district code.  
3. Extract vehicle series.  
4. Extract vehicle number.  
5. Count letters and digits separately.  
6. Verify:  
o First 2 characters must be alphabets.  
o Next 2 must be digits.  
o Next 2 must be alphabets.  
o Last 4 must be digits.  
7. Display whether the number plate is valid. '''

# Vehicle Number Plate Verification

vehicle = input("Enter Vehicle Number: ")

state = vehicle[:2]
district = vehicle[2:4]
series = vehicle[4:6]
number = vehicle[6:]

letters = 0
digits = 0

for ch in vehicle:

    if ch.isalpha():
        letters += 1

    elif ch.isdigit():
        digits += 1

# Validation
if (state.isalpha() and
    district.isdigit() and
    series.isalpha() and
    number.isdigit() and
    len(number) == 4):

    status = "Valid"

else:
    status = "Invalid"

print("State Code =", state)
print("District Code =", district)
print("Series =", series)
print("Vehicle Number =", number)
print("Total Letters =", letters)
print("Total Digits =", digits)
print("Vehicle Number Status =", status)