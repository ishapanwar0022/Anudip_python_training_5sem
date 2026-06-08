#6. Email Address Validator 
'''Problem Statement 
A user enters an email address: 
rahul.sharma2026@gmail.com 
Tasks 
Write a program to: 
1. Extract username.  
2. Extract domain name.  
3. Extract extension.  
4. Count digits present in username.  
5. Count special characters.  
6. Check whether:  
o Exactly one '@' exists.  
o At least one '.' exists after '@'.  
7. Display Valid Email or Invalid Email.'''

# Email Address Validator

email = input("Enter Email: ")

username = email[:email.index("@")]
domain_part = email[email.index("@")+1:]

domain = domain_part[:domain_part.index(".")]
extension = domain_part[domain_part.index(".")+1:]

digits = 0
special = 0

for ch in username:

    if ch.isdigit():
        digits += 1

    elif not ch.isalnum():
        special += 1

# Validation
if email.count("@") == 1 and "." in domain_part:
    status = "Valid Email"
else:
    status = "Invalid Email"

print("Username =", username)
print("Domain =", domain)
print("Extension =", extension)
print("Digits Found =", digits)
print("Special Characters Found =", special)
print("Email Status =", status)