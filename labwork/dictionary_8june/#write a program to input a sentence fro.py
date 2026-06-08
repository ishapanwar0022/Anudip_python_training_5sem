'''#write a program to input a sentence from user and count the number of special characters present in sentence in string python

# Program to count special characters in a sentence

sentence = input("Enter a sentence: ")

count = 0

for ch in sentence:
    # Check if character is not alphabet, digit, or space
    if not (ch.isalpha() or ch.isdigit() or ch.isspace()):
        count += 1

print("Number of special characters =", count)

#write a program and input a sentence from user and count the number of character in the sentence in string python without using lame function 

sentence = input("enter a sentence: ")
count = 0

for ch in sentence:
    count = count + 1
    print("total number of character =", count)'''


    #write a program to input a sentence and display the frequency of vowel which are present in thesentence ignoring the case.


from itertools import count


sentence = input("enter a sentence :")

count a = e = i = o = u = 0

for ch in sentence:
    if ch == 'a' or ch == 'A':
        a = a + 1

    elif ch == 'e' or ch == 'E':
        e = e + 1

    elif ch == 'i' or ch == 'I':
        i = i + 1

    elif ch == 'o' or ch == 'O':
        o = o + 1

    elif ch == 'u' or ch == 'U':
        u = u + 1

print("Frequency of vowel 'a' or 'A':", a)
print("Frequency of vowel 'e' or 'E':", e)
print("Frequency of vowel 'i' or 'I':", i)
print("Frequency of vowel 'o' or 'O':", o)
print("Frequency of vowel 'u' or 'U':", u)