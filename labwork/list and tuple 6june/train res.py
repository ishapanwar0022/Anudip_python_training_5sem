# Passenger records
passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

confirmed = 0
waiting = 0

# Display waiting-list passengers
print("Waiting List Passengers:")

for name, status in passengers:
    if status == "Waiting":
        print(name)

# Count confirmed and waiting passengers
for name, status in passengers:
    if status == "Confirmed":
        confirmed += 1
    else:
        waiting += 1

print("Confirmed =", confirmed)
print("Waiting =", waiting)

# Search passenger ticket status
search_name = input("Enter Passenger Name: ")

for name, status in passengers:
    if name == search_name and status == "Confirmed":
        print("Ticket Confirmed")

# Create separate lists
confirmed_list = []
waiting_list = []

for name, status in passengers:
    if status == "Confirmed":
        confirmed_list.append(name)
    else:
        waiting_list.append(name)

print("Confirmed List =", confirmed_list)
print("Waiting List =", waiting_list)