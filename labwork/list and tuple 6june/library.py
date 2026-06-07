# Books and available copies
books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# Display unavailable books
print("Unavailable Books:")
for book, copies in books:
    if copies == 0:
        print(book)

# Find books with more than 2 copies
print("\nBooks with more than 2 copies:")
for book, copies in books:
    if copies > 2:
        print(book)

# Count available books
count = 0
for book, copies in books:
    if copies > 0:
        count += 1

print("\nAvailable Books =", count)

# Search a book
search_book = input("\nEnter book name to search: ")

for book, copies in books:
    if book == search_book:
        print("Book Found!")
        break