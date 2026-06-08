# Smart Electricity Billing System
# Creating a dictionary to store electricity units
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}
# ----------------------------------------------------
# 1. Display houses consuming more than 400 units
print("Houses consuming more than 400 units:")
for house, unit in units.items():
    if unit > 400:
        print(house)

# ----------------------------------------------------
# 2. Find highest consuming house
dict_items = list(units.items())
highest_house = dict_items[0][0]
highest_unit = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_unit:
        highest_house = item[0]
        highest_unit = item[1]
print("Highest Consumption House:", highest_house, "with", highest_unit, "units")

# ----------------------------------------------------
# 3. Find lowest consuming house
lowest_house = dict_items[0][0]
lowest_unit = dict_items[0][1]

for item in dict_items:
    if item[1] < lowest_unit:
        lowest_house = item[0]
        lowest_unit = item[1]
print("Lowest Consumption House:", lowest_house, "with", lowest_unit, "units")

# ----------------------------------------------------
# 4. Calculate total units consumed
total_units = 0
for unit in units.values():
    total_units = total_units + unit
print("Total Units Consumed:", total_units)

# ----------------------------------------------------
# 5. Create categories (Low, Medium, High)
low = []
medium = []
high = []

for house, unit in units.items():
    if unit < 200:
        low.append(house)
    elif unit <= 400:
        medium.append(house)
    else:
        high.append(house)

print("Low Consumption Houses:", low)
print("Medium Consumption Houses:", medium)
print("High Consumption Houses:", high)

# ----------------------------------------------------
# 6. Count houses for energy-saving campaign (>300 units)
count = 0
for unit in units.values():
    if unit > 300:
        count += 1
print("Houses eligible for Energy-Saving Campaign:", count)

# ----------------------------------------------------
# Display all house records
print("All House Records:")
print(units)