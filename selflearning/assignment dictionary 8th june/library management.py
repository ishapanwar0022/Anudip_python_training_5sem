#3. Smart Library Management System 
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
12. Create a separate dictionary of books requiring immediate purchase. '''

#  Smart Library Management System

library = {
    "B101": {"title": "Python", "copies": 5},
    "B102": {"title": "Java", "copies": 3},
    "B103": {"title": "C Language", "copies": 2}
}

while True:

    print("\n1.Display Books")
    print("2.Add Book")
    print("3.Search Book")
    print("4.Issue Book")
    print("5.Return Book")
    print("6.Low Copies Books")
    print("7.Exit")

    ch = int(input("Enter Choice: "))

    # Display Books
    if ch == 1:

        for b in library:
            print(b, library[b])

    # Add Book
    elif ch == 2:

        bid = input("Enter Book ID: ")
        title = input("Enter Book Name: ")
        copies = int(input("Enter Copies: "))

        library[bid] = {
            "title": title,
            "copies": copies
        }

        print("Book Added")

    # Search Book
    elif ch == 3:

        bid = input("Enter Book ID: ")

        if bid in library:
            print(library[bid])

        else:
            print("Book Not Found")

    # Issue Book
    elif ch == 4:

        bid = input("Enter Book ID: ")

        if bid in library and library[bid]["copies"] > 0:

            library[bid]["copies"] -= 1
            print("Book Issued")

        else:
            print("Book Not Available")

    # Return Book
    elif ch == 5:

        bid = input("Enter Book ID: ")

        if bid in library:

            library[bid]["copies"] += 1
            print("Book Returned")

    # Low Copies
    elif ch == 6:

        print("Books with less than 3 copies:")

        for b in library:

            if library[b]["copies"] < 3:
                print(library[b]["title"])

    # Exit
    elif ch == 7:
        break

    else:
        print("Invalid Choice")