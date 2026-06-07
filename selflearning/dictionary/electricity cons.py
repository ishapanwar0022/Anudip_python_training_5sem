# Dictionary of electricity units consumed
units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# Display houses consuming more than 300 units
print("Houses consuming more than 300 units:")
for house, unit in units.items():
    if unit > 300:
        print(house, ":", unit)

# Count houses consuming less than 200 units
count = 0
for unit in units.values():
    if unit < 200:
        count += 1
print("\nHouses consuming less than 200 units:", count)

# Find house with highest consumption
highest_house = max(units, key=units.get)
print("\nHighest Consumption House:", highest_house)
print("Units:", units[highest_house])

# Create list of houses for awareness campaign
campaign = []
for house, unit in units.items():
    if unit > 400:
        campaign.append(house)

print("\nHouses for awareness campaign:")
print(campaign)

# Categorize houses
print("\nHouse Categories:")
for house, unit in units.items():

    if unit < 200:
        category = "Low"

    elif unit <= 350:
        category = "Medium"

    else:
        category = "High"

    print(house, ":", category)