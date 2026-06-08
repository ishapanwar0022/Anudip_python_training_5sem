#10. Text Compression Analyzer 
'''Problem Statement 
A compressed message is given: 
AAABBBCCCDDDAAA 
Tasks 
Write a program to: 
1. Count occurrences of each character.  
2. Create a dictionary of character frequencies.  
3. Display unique characters.  
4. Find the most frequent character.  
5. Create a compressed output:  
A3B3C3D3A3 
6. Calculate compression ratio.''' 

# Text Compression Analyzer

text = input("Enter Text: ")

freq = {}

for ch in text:

    if ch in freq:
        freq[ch] += 1

    else:
        freq[ch] = 1

print("Character Frequencies")

for key in freq:
    print(key, "->", freq[key])

# Unique Characters
unique = list(freq.keys())

print("Unique Characters =", unique)

# Most Frequent Character
most_char = max(freq, key=freq.get)

print("Most Frequent Character =", most_char)

# Compressed Output
compressed = ""

count = 1

for i in range(len(text)-1):

    if text[i] == text[i+1]:
        count += 1

    else:
        compressed = compressed + text[i] + str(count)
        count = 1

compressed = compressed + text[-1] + str(count)

print("Compressed Output =", compressed)

original_length = len(text)
compressed_length = len(compressed)

ratio = (compressed_length / original_length) * 100

print("Original Length =", original_length)
print("Compressed Length =", compressed_length)
print("Compression Ratio =", ratio, "%")