 
#1. Online Shopping Order Analytics 
'''Problem Statement 
An e-commerce company stores product sales data as: 
sales = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 
Tasks 
1. Display products sold more than 20 times.  
2. Find the best-selling product.  
3. Find the least-selling product.  
4. Calculate total products sold.  
5. Create a list of products requiring promotion (sales < 15).  
6. Count products having sales between 10 and 30'''

# Online Shopping Order Analytics
# Creating a dictionary to store product sales
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}
# ----------------------------------------------------
# 1. Products sold more than 20 times
print("Products sold more than 20 times:")
for product, qty in sales.items():
    if qty > 20:
        print(product)

# ----------------------------------------------------
# 2. Find best-selling product
dict_items = list(sales.items())
best_product = dict_items[0][0]
highest_qty = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_qty:
        best_product = item[0]
        highest_qty = item[1]
print("Best Selling Product:", best_product, "with", highest_qty, "units")

# ----------------------------------------------------
# 3. Find least-selling product
least_product = dict_items[0][0]
lowest_qty = dict_items[0][1]

for item in dict_items:
    if item[1] < lowest_qty:
        least_product = item[0]
        lowest_qty = item[1]
print("Least Selling Product:", least_product, "with", lowest_qty, "units")

# ----------------------------------------------------
# 4. Calculate total units sold
total_units = 0
for qty in sales.values():
    total_units = total_units + qty
print("Total Units Sold:", total_units)

# ----------------------------------------------------
# 5. Products requiring promotion (sales less than 15)
promotion_list = []
for product, qty in sales.items():
    if qty < 15:
        promotion_list.append(product)
print("Products Requiring Promotion:", promotion_list)

# ----------------------------------------------------
# 6. Count products having sales between 10 and 30
count = 0
for qty in sales.values():
    if qty >= 10 and qty <= 30:
        count += 1
print("Products having sales between 10 and 30:", count)

# ----------------------------------------------------
# Display all product records
print("All Product Records:")
print(sales)
