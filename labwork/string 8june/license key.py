#9. License Key Verification System 
'''Problem Statement 
A software license key is entered: 
ABCD-EFGH-IJKL-MNOP 
Tasks 
Write a program to: 
1. Verify there are exactly 4 groups.  
2. Verify each group contains exactly 4 characters.  
3. Count total letters.  
4. Count vowels.  
5. Remove hyphens and display the merged key.  
6. Create a list containing all groups.                        
7. Display whether the key format is valid.  '''

# License Key Verification System

key = input("Enter License Key: ")

groups = key.split("-")

letters = 0
vowels = 0

for ch in key:

    if ch.isalpha():
        letters += 1

        if ch.upper() in "AEIOU":
            vowels += 1

merged = key.replace("-", "")

valid = True

if len(groups) != 4:
    valid = False

for g in groups:
    if len(g) != 4:
        valid = False

print("Groups =", groups)
print("Number of Groups =", len(groups))
print("Total Letters =", letters)
print("Total Vowels =", vowels)
print("Merged Key =", merged)

if valid:
    print("License Key Status = Valid")
else:
    print("License Key Status = Invalid")