# City Population Dashboard
'''Problem Statement 
The government wants to analyze city data. 
Store details of at least 30 cities. 
Example Structure 
cities = { 
    "Delhi": { 
        "population": 32000000, 
        "area": 1484, 
        "literacy": 89 
    } 
} 
Requirements 
1. Display all city details.  
2. Find the most populated city.  
3. Find the least populated city.  
4. Calculate average population.  
5. Display cities with literacy rate above 90%.  
6. Display cities with literacy below average.  
7. Calculate population density.  
8. Find city with highest density.  
9. Categorize cities:  
o Small  
o Medium  
o Large  
10. Create a development-priority list.  
11. Generate separate dictionaries for:  
o High Literacy Cities  
o Low Literacy Cities  
12. Generate a national summary report.  
Challenge 
Rank all cities based on population density. '''


cities = {
    "Delhi": {"population": 30000000, "literacy": 89, "area": 1484},
    "Mumbai": {"population": 20000000, "literacy": 92, "area": 603},
    "Jaipur": {"population": 4000000, "literacy": 85, "area": 467},
    "Lucknow": {"population": 3500000, "literacy": 88, "area": 631},
    "Pune": {"population": 6000000, "literacy": 91, "area": 516}
}

while True:

    print("\n1.Display Cities")
    print("2.Add City")
    print("3.Highest Population City")
    print("4.Lowest Population City")
    print("5.Average Population")
    print("6.High Literacy Cities")
    print("7.Low Literacy Cities")
    print("8.Population Density")
    print("9.City Categories")
    print("10.Development Priority List")
    print("11.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:

        for c in cities:
            print(c, cities[c])

    elif ch == 2:

        name = input("Enter City Name: ")
        population = int(input("Enter Population: "))
        literacy = int(input("Enter Literacy: "))
        area = int(input("Enter Area: "))

        cities[name] = {
            "population": population,
            "literacy": literacy,
            "area": area
        }

        print("City Added")

    elif ch == 3:

        city = ""
        max_pop = -1

        for c in cities:

            if cities[c]["population"] > max_pop:

                max_pop = cities[c]["population"]
                city = c

        print("Highest Population City =", city)

    elif ch == 4:

        city = ""
        min_pop = 999999999

        for c in cities:

            if cities[c]["population"] < min_pop:

                min_pop = cities[c]["population"]
                city = c

        print("Lowest Population City =", city)

    elif ch == 5:

        total = 0

        for c in cities:
            total += cities[c]["population"]

        avg = total / len(cities)

        print("Average Population =", avg)

    elif ch == 6:

        print("High Literacy Cities:")

        for c in cities:

            if cities[c]["literacy"] >= 90:
                print(c)

    elif ch == 7:

        print("Low Literacy Cities:")

        for c in cities:

            if cities[c]["literacy"] < 90:
                print(c)

    elif ch == 8:

        print("Population Density:")

        for c in cities:

            density = cities[c]["population"] / cities[c]["area"]

            print(c, "=", density)

    elif ch == 9:

        for c in cities:

            pop = cities[c]["population"]

            if pop > 10000000:
                print(c, "- Large")

            elif pop > 5000000:
                print(c, "- Medium")

            else:
                print(c, "- Small")

    elif ch == 10:

        priority = {}

        for c in cities:

            if cities[c]["literacy"] < 90:
                priority[c] = cities[c]

        print("Development Priority Cities:")
        print(priority)

    elif ch == 11:
        break

    else:
        print("Invalid Choice")