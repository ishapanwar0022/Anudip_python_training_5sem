# Dictionary containing player scores
scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# Players scoring 50 or more
print("Players scoring 50 or more:")
for player, score in scores.items():
    if score >= 50:
        print(player, "-", score)

# Count centuries
centuries = 0
for score in scores.values():
    if score >= 100:
        centuries += 1
print("Number of Centuries:", centuries)

# Highest scorer
highest = max(scores, key=scores.get)
print("Highest Scorer:", highest, "-", scores[highest])

# Players scoring below 30
below_30 = []
for player, score in scores.items():
    if score < 30:
        below_30.append(player)
print("Players below 30:", below_30)

# Players scoring between 50 and 99
count = 0
for score in scores.values():
    if 50 <= score <= 99:
        count += 1
print("Players scoring between 50 and 99:", count)

