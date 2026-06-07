# E-Commerce Order Analysis

# List of products and their prices stored as tuples
orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# Display products costing more than 1000
print("Products costing more than ₹1000:")
for product, price in orders:
    if price > 1000:
        print(product, "-", price)

# Find the most expensive product
most_expensive = orders[0]

for item in orders:
    if item[1] > most_expensive[1]:
        most_expensive = item

print("\nMost Expensive Product:", most_expensive[0])
print("Price:", most_expensive[1])

# Calculate total order value
total = 0

for product, price in orders:
    total += price

print("\nTotal Order Value =", total)

# Count products costing below 1000
count = 0

for product, price in orders:
    if price < 1000:
        count += 1

print("Products costing below ₹1000 =", count)