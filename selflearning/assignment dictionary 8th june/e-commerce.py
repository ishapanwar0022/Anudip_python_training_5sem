#2. E-Commerce Inventory & Sales Dashboard 
'''Problem Statement 
An online store wants to manage products and sales. 
Example Structure 
products = { 
    "P101": { 
        "name": "Laptop", 
        "price": 55000, 
        "stock": 12, 
        "sold": 25 
    } 
} 
Maintain records of at least 30 products. 
Requirements 
1. Display all products.  
2. Add a new product.  
3. Update stock after sales.  
4. Find out-of-stock products.  
5. Find products with stock less than 5.  
6. Calculate total inventory value.  
7. Find best-selling product.  
8. Find least-selling product.  
9. Calculate total revenue generated.  
10. Generate a low-stock report.  
11. Display products whose sales exceed the average sales.  
12. Create a dictionary of products eligible for promotion (sales < 10).'''

# E-Commerce Inventory System

products = {
    "P101": {"name": "Laptop", "price": 50000, "stock": 10, "sold": 20},
    "P102": {"name": "Mouse", "price": 500, "stock": 5, "sold": 15},
    "P103": {"name": "Keyboard", "price": 1000, "stock": 8, "sold": 10}
}

while True:

    print("\n1. Display Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Out of Stock Products")
    print("5. Total Inventory Value")
    print("6. Best Selling Product")
    print("7. Total Revenue")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    # Display Products
    if choice == 1:

        for pid in products:
            print(pid, products[pid])

    # Add Product
    elif choice == 2:

        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        price = int(input("Enter Price: "))
        stock = int(input("Enter Stock: "))
        sold = int(input("Enter Sold Quantity: "))

        products[pid] = {
            "name": name,
            "price": price,
            "stock": stock,
            "sold": sold
        }

        print("Product Added")

    # Update Stock
    elif choice == 3:

        pid = input("Enter Product ID: ")

        if pid in products:
            stock = int(input("Enter New Stock: "))
            products[pid]["stock"] = stock
            print("Stock Updated")
        else:
            print("Product Not Found")

    # Out of Stock
    elif choice == 4:

        for pid in products:

            if products[pid]["stock"] == 0:
                print(products[pid]["name"])

    # Total Inventory Value
    elif choice == 5:

        total = 0

        for pid in products:
            total += products[pid]["price"] * products[pid]["stock"]

        print("Inventory Value =", total)

    # Best Selling Product
    elif choice == 6:

        best = ""
        max_sale = 0

        for pid in products:

            if products[pid]["sold"] > max_sale:
                max_sale = products[pid]["sold"]
                best = products[pid]["name"]

        print("Best Selling Product =", best)

    # Total Revenue
    elif choice == 7:

        revenue = 0

        for pid in products:
            revenue += products[pid]["price"] * products[pid]["sold"]

        print("Total Revenue =", revenue)

    # Exit
    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")