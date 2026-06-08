#7. Username Generator System 
'''Problem Statement 
A student enters: 
Rahul Sharma 
Tasks 
Generate a username using the rules: 
1. Remove spaces.  
2. Convert to lowercase.  
3. Append current year (2026).  
4. If username length exceeds 12, keep only first 12 characters.  
5. Count vowels in the generated username.  
6. Count consonants.  
7. Display username statistics. '''

# Username Generator System

name = input("Enter Name: ")

username = name.replace(" ", "")
username = username.lower()
username = username + "2026"

length = len(username)

vowels = 0
consonants = 0

for ch in username:

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1

        else:
            consonants += 1

print("Generated Username =", username)
print("Username Length =", length)
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Status = Username Generated Successfully")