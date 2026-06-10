# E-Commerce Inventory System
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
12. Create a dictionary of products eligible for promotion (sales < 10).  
Challenge 
Generate a complete business report. '''

products = {
    "P101": {"name": "Laptop", "price": 50000, "stock": 10, "sold": 20},
    "P102": {"name": "Mouse", "price": 500, "stock": 2, "sold": 15},
    "P103": {"name": "Keyboard", "price": 1000, "stock": 0, "sold": 5},
    "P104": {"name": "Monitor", "price": 8000, "stock": 8, "sold": 12},
    "P105": {"name": "Printer", "price": 6000, "stock": 4, "sold": 8}
}

while True:

    print("\n1.Display Products")
    print("2.Add Product")
    print("3.Update Stock")
    print("4.Out of Stock Products")
    print("5.Low Stock Products")
    print("6.Total Inventory Value")
    print("7.Best Selling Product")
    print("8.Least Selling Product")
    print("9.Total Revenue")
    print("10.Products Above Average Sales")
    print("11.Promotion Products")
    print("12.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:

        for pid in products:
            print(pid, products[pid])

    elif ch == 2:

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

    elif ch == 3:

        pid = input("Enter Product ID: ")

        if pid in products:
            stock = int(input("Enter New Stock: "))
            products[pid]["stock"] = stock
            print("Stock Updated")

    elif ch == 4:

        print("Out of Stock Products:")

        for pid in products:

            if products[pid]["stock"] == 0:
                print(products[pid]["name"])

    elif ch == 5:

        print("Low Stock Products:")

        for pid in products:

            if products[pid]["stock"] < 5:
                print(products[pid]["name"])

    elif ch == 6:

        total = 0

        for pid in products:

            total += products[pid]["price"] * products[pid]["stock"]

        print("Inventory Value =", total)

    elif ch == 7:

        best = ""
        max_sale = -1

        for pid in products:

            if products[pid]["sold"] > max_sale:

                max_sale = products[pid]["sold"]
                best = products[pid]["name"]

        print("Best Selling Product =", best)

    elif ch == 8:

        least = ""
        min_sale = 99999

        for pid in products:

            if products[pid]["sold"] < min_sale:

                min_sale = products[pid]["sold"]
                least = products[pid]["name"]

        print("Least Selling Product =", least)

    elif ch == 9:

        revenue = 0

        for pid in products:

            revenue += products[pid]["price"] * products[pid]["sold"]

        print("Total Revenue =", revenue)

    elif ch == 10:

        total = 0

        for pid in products:
            total += products[pid]["sold"]

        avg = total / len(products)

        print("Products Above Average Sales:")

        for pid in products:

            if products[pid]["sold"] > avg:
                print(products[pid]["name"])

    elif ch == 11:

        promotion = {}

        for pid in products:

            if products[pid]["sold"] < 10:
                promotion[pid] = products[pid]

        print("Promotion Products:")
        print(promotion)

    elif ch == 12:
        break

    else:
        print("Invalid Choice")