#5. City Population & Development Dashboard 
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
12. Generate a national summary report. '''

# City Population Dashboard

cities = {
    "Delhi": {"population": 30000000, "literacy": 89},
    "Mumbai": {"population": 20000000, "literacy": 92},
    "Jaipur": {"population": 4000000, "literacy": 85}
}

while True:

    print("\n1.Display Cities")
    print("2.Add City")
    print("3.Highest Population")
    print("4.Average Population")
    print("5.High Literacy Cities")
    print("6.Exit")

    ch = int(input("Enter Choice: "))

    # Display Cities
    if ch == 1:

        for c in cities:
            print(c, cities[c])

    # Add City
    elif ch == 2:

        name = input("Enter City Name: ")
        population = int(input("Enter Population: "))
        literacy = int(input("Enter Literacy Rate: "))

        cities[name] = {
            "population": population,
            "literacy": literacy
        }

        print("City Added")

    # Highest Population
    elif ch == 3:

        city = ""
        max_pop = 0

        for c in cities:

            if cities[c]["population"] > max_pop:

                max_pop = cities[c]["population"]
                city = c

        print("Highest Population City =", city)

    # Average Population
    elif ch == 4:

        total = 0

        for c in cities:
            total += cities[c]["population"]

        avg = total / len(cities)

        print("Average Population =", avg)

    # High Literacy Cities
    elif ch == 5:

        print("High Literacy Cities:")

        for c in cities:

            if cities[c]["literacy"] >= 90:
                print(c)

    # Exit
    elif ch == 6:
        break

    else:
        print("Invalid Choice")