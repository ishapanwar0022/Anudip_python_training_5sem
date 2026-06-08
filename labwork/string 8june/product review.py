
#5. Product Review Analyzer 
'''Problem Statement 
A customer submits a review: 
This product is excellent excellent excellent and very useful 
Tasks 
Write a program to: 
1. Count total words.  
2. Create a dictionary containing word frequencies.  
3. Find the most frequently used word.  
4. Find all words appearing only once.  
5. Count words having more than 5 characters.  
6. Display words in reverse order.  
7. Create a list of unique words. '''

# Product Review Analyzer

review = input("Enter Review: ")

words = review.split()

print("Total Words =", len(words))

# Frequency Dictionary
freq = {}

for word in words:

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequencies")

for key in freq:
    print(key, "->", freq[key])

# Most frequent word
most_word = max(freq, key=freq.get)

print("Most Frequent Word =", most_word)

# Words appearing once
once = []

for key in freq:
    if freq[key] == 1:
        once.append(key)

print("Words Appearing Once =", once)

# Words more than 5 characters
count = 0

for word in words:
    if len(word) > 5:
        count += 1

print("Words More Than 5 Characters =", count)

# Reverse order
print("Reverse Order =", words[::-1])

# Unique words
unique = list(freq.keys())

print("Unique Words =", unique)