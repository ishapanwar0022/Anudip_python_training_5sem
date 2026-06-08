# City Temperature Monitoring System

# Creating a dictionary to store city temperatures

temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# ----------------------------------------------------
# Display cities having temperature above 40°C

print("Cities Above 40°C:")

for city, temp in temperature.items():
    if temp > 40:
        print(city)

# ----------------------------------------------------
# Find hottest city

dict_items = list(temperature.items())

hottest_city = dict_items[0][0]
highest_temp = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_temp:
        hottest_city = item[0]
        highest_temp = item[1]

print("Hottest City:", hottest_city)
print("Temperature:", highest_temp)

# ----------------------------------------------------
# Find coolest city

coolest_city = dict_items[0][0]
lowest_temp = dict_items[0][1]

for item in dict_items:
    if item[1] < lowest_temp:
        coolest_city = item[0]
        lowest_temp = item[1]

print("Coolest City:", coolest_city)
print("Temperature:", lowest_temp)

# ----------------------------------------------------
# Calculate average temperature

total_temp = 0

for temp in temperature.values():
    total_temp = total_temp + temp

average_temp = total_temp / len(temperature)

print("Average Temperature:", average_temp)

# ----------------------------------------------------
# Create list of pleasant cities (temperature below 35°C)

pleasant_cities = []

for city, temp in temperature.items():
    if temp < 35:
        pleasant_cities.append(city)

print("Pleasant Cities:")
print(pleasant_cities)

# ----------------------------------------------------
# Count cities having temperature between 35°C and 40°C

count = 0

for temp in temperature.values():

    if temp >= 35 and temp <= 40:
        count += 1

print("Cities Between 35°C and 40°C:", count)

# ----------------------------------------------------
# Display all city records

print("All City Records:")
print(temperature)