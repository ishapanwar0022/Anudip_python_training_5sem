# Cricket Tournament Statistics
# Creating a dictionary to store player runs
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}
# ----------------------------------------------------
# 1. Display players scoring more than 500 runs
print("Players scoring more than 500 runs:")
for player, run in runs.items():
    if run > 500:
        print(player)

# ----------------------------------------------------
# 2. Find Orange Cap winner (Highest Scorer)
dict_items = list(runs.items())
orange_cap_winner = dict_items[0][0]
highest_runs = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_runs:
        orange_cap_winner = item[0]
        highest_runs = item[1]
print("Orange Cap Winner:", orange_cap_winner, "with", highest_runs, "runs")

# ----------------------------------------------------
# 3. Find lowest scorer
lowest_scorer = dict_items[0][0]
lowest_runs = dict_items[0][1]

for item in dict_items:
    if item[1] < lowest_runs:
        lowest_scorer = item[0]
        lowest_runs = item[1]
print("Lowest Scorer:", lowest_scorer, "with", lowest_runs, "runs")

# ----------------------------------------------------
# 4. Calculate total runs
total_runs = 0
for run in runs.values():
    total_runs = total_runs + run
print("Total Runs Scored:", total_runs)

# ----------------------------------------------------
# 5. Players below 400 runs
below_400 = []
for player, run in runs.items():
    if run < 400:
        below_400.append(player)
print("Players below 400 runs:", below_400)

# ----------------------------------------------------
# 6. Count players between 400 and 600 runs
count = 0
for run in runs.values():
    if run >= 400 and run <= 600:
        count += 1
print("Players scoring between 400 and 600:", count)

# ----------------------------------------------------
# Display all player records
print("All Player Records:")
print(runs)