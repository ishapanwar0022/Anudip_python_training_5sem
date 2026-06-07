# List of scores
scores = [45, 78, 12, 100, 67, 8, 90, 55]

half_century = 0
century = 0
total = 0

# Count half-centuries and centuries
for score in scores:
    if score >= 50 and score < 100:
        half_century += 1
    elif score >= 100:
        century += 1

# Find highest score
highest = max(scores)

# Display scores below 20
print("Scores below 20:")
for score in scores:
    if score < 20:
        print(score)

# Calculate average
for score in scores:
    total += score

average = total / len(scores)

print("Half Centuries =", half_century)
print("Centuries =", century)
print("Highest Score =", highest)
print("Average Score =", average)