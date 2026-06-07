# Correct answers
correct = ['A', 'C', 'B', 'D', 'A']

# Student answers
student = ['A', 'B', 'B', 'D', 'C']

score = 0
wrong = 0

print("Incorrect Question Numbers:")

# Compare answers
for i in range(len(correct)):
    if correct[i] == student[i]:
        score += 1
    else:
        wrong += 1
        print(i + 1)

print("Correct Answers =", score)
print("Wrong Answers =", wrong)

# Calculate percentage
percentage = (score / len(correct)) * 100

print("Percentage =", percentage)

# Pass/Fail
if percentage >= 60:
    print("Pass")
else:
    print("Fail")