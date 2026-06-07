# Dictionary containing books and available copies
books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# Display unavailable books
print("Unavailable Books:")
for book, copies in books.items():
    if copies == 0:
        print(book)

# Count available books
count = 0
for copies in books.values():
    if copies > 0:
        count += 1
print("Available Books:", count)

# Book with maximum copies
maximum = max(books, key=books.get)
print("Book with Maximum Copies:", maximum)

# Books having less than 3 copies
less_than_3 = []
for book, copies in books.items():
    if copies < 3:
        less_than_3.append(book)
print("Books having less than 3 copies:", less_than_3)

# Total available books
total = sum(books.values())
print("Total Books Available:", total)


