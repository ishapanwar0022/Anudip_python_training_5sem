# Smart Library Management System
'''Problem Statement 
Create a digital library management system. 
Example Structure 
library = { 
    "B101": { 
        "title": "Python Basics", 
        "author": "ABC", 
        "copies": 5 
    } 
} 
Maintain records of at least 30 books. 
Requirements 
1. Add a book.  
2. Remove a book.  
3. Search a book by ID.  
4. Search by title.  
5. Update available copies.  
6. Issue a book.  
7. Return a book.  
8. Display books with fewer than 3 copies.  
9. Display books that are unavailable.  
10. Find the most available book.  
11. Generate a restocking report.  
12. Create a separate dictionary of books requiring immediate purchase.  
Challenge 
Generate a complete library summary report. '''

library = {
    "B101": {"title": "Python", "copies": 5},
    "B102": {"title": "Java", "copies": 2},
    "B103": {"title": "C Language", "copies": 0},
    "B104": {"title": "DBMS", "copies": 4},
    "B105": {"title": "OS", "copies": 1}
}

while True:

    print("\n1.Display Books")
    print("2.Add Book")
    print("3.Remove Book")
    print("4.Search by ID")
    print("5.Search by Title")
    print("6.Issue Book")
    print("7.Return Book")
    print("8.Low Copies Books")
    print("9.Unavailable Books")
    print("10.Most Available Book")
    print("11.Restocking Report")
    print("12.Immediate Purchase Books")
    print("13.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:

        for b in library:
            print(b, library[b])

    elif ch == 2:

        bid = input("Enter Book ID: ")
        title = input("Enter Title: ")
        copies = int(input("Enter Copies: "))

        library[bid] = {
            "title": title,
            "copies": copies
        }

        print("Book Added")

    elif ch == 3:

        bid = input("Enter Book ID: ")

        if bid in library:
            del library[bid]
            print("Book Removed")

    elif ch == 4:

        bid = input("Enter Book ID: ")

        if bid in library:
            print(library[bid])
        else:
            print("Book Not Found")

    elif ch == 5:

        title = input("Enter Book Title: ")

        for b in library:

            if library[b]["title"] == title:
                print(library[b])

    elif ch == 6:

        bid = input("Enter Book ID: ")

        if bid in library and library[bid]["copies"] > 0:

            library[bid]["copies"] -= 1
            print("Book Issued")

        else:
            print("Book Not Available")

    elif ch == 7:

        bid = input("Enter Book ID: ")

        if bid in library:

            library[bid]["copies"] += 1
            print("Book Returned")

    elif ch == 8:

        print("Books with Less Than 3 Copies:")

        for b in library:

            if library[b]["copies"] < 3:
                print(library[b]["title"])

    elif ch == 9:

        print("Unavailable Books:")

        for b in library:

            if library[b]["copies"] == 0:
                print(library[b]["title"])

    elif ch == 10:

        book = ""
        max_copy = -1

        for b in library:

            if library[b]["copies"] > max_copy:

                max_copy = library[b]["copies"]
                book = library[b]["title"]

        print("Most Available Book =", book)

    elif ch == 11:

        print("Restocking Report:")

        for b in library:

            if library[b]["copies"] < 3:
                print(library[b]["title"])

    elif ch == 12:

        purchase = {}

        for b in library:

            if library[b]["copies"] <= 1:
                purchase[b] = library[b]

        print("Immediate Purchase Books:")
        print(purchase)

    elif ch == 13:
        break

    else:
        print("Invalid Choice")