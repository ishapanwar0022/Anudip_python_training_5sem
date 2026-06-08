#2.Password Strength Analyzer 
'''Problem Statement 
A user enters a password. 
Python@2026! 
Tasks 
Write a program to determine whether the password is Strong, Medium, or Weak. 
Rules: 
• Minimum length 8  
• Contains at least:  
o 1 uppercase letter  
o 1 lowercase letter  
o 1 digit  
o 1 special character  
Additionally: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Display all digits separately.  
6. Display all special characters separately. ''' 

# Password Strength Analyzer

password = input("Enter Password: ")

upper = 0
lower = 0
digits = []
special = []

for ch in password:

    if ch.isupper():
        upper += 1

    elif ch.islower():
        lower += 1

    elif ch.isdigit():
        digits.append(ch)

    else:
        special.append(ch)

# Check password strength
if len(password) >= 8 and upper >= 1 and lower >= 1 and len(digits) >= 1 and len(special) >= 1:
    strength = "Strong"

elif len(password) >= 6:
    strength = "Medium"

else:
    strength = "Weak"

print("Uppercase Letters =", upper)
print("Lowercase Letters =", lower)
print("Digits =", len(digits))
print("Special Characters =", len(special))
print("Digits Found =", digits)
print("Special Characters Found =", special)
print("Password Strength =", strength)