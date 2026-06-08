#3. Chat Message Analytics 
'''Problem Statement 
A chat application stores a message: 
Python is awesome and Python is easy to learn 
Tasks 
Write a program to: 
1. Count total characters.  
2. Count total words.  
3. Find the longest word.  
4. Find the shortest word.  
5. Count how many times the word "Python" appears.  
6. Create a list of words having more than 4 characters.  
7. Display all words starting with a vowel.  
8. Count the number of vowels and consonants.'''

 # Chat Message Analytics

msg = input("Enter Message: ")

words = msg.split()

# Total characters
print("Total Characters =", len(msg))

# Total words
print("Total Words =", len(words))

# Longest word
longest = max(words, key=len)

# Shortest word
shortest = min(words, key=len)

print("Longest Word =", longest)
print("Shortest Word =", shortest)

# Count Python
count_python = words.count("Python")
print("Occurrences of Python =", count_python)

# Words greater than 4 characters
long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)

print("Words Longer Than 4 Characters =", long_words)

# Words starting with vowel
vowel_words = []

for word in words:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

print("Words Starting With Vowel =", vowel_words)

# Count vowels and consonants
vowels = 0
consonants = 0

for ch in msg.lower():

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)