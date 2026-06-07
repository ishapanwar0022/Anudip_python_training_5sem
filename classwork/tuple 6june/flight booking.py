# Passenger booking records stored in tuple
# Format: (Passenger ID, Destination, Booking Status)

bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# 1. Display confirmed passengers


print("Confirmed Passengers:")

for pid, destination, status in bookings:
    if status == "Confirmed":
        print(pid, destination)


# 2. Count passengers travelling to Delhi


delhi_count = 0

for pid, destination, status in bookings:
    if destination == "Delhi":
        delhi_count += 1

print("\nPassengers Travelling to Delhi =", delhi_count)


# 3. Count Confirmed, Waiting and Cancelled bookings

confirmed = 0
waiting = 0
cancelled = 0

for pid, destination, status in bookings:

    if status == "Confirmed":
        confirmed += 1

    elif status == "Waiting":
        waiting += 1

    elif status == "Cancelled":
        cancelled += 1

print("\nConfirmed =", confirmed)
print("Waiting =", waiting)
print("Cancelled =", cancelled)


# 4. Create list of waiting passengers


waiting_list = []

for pid, destination, status in bookings:
    if status == "Waiting":
        waiting_list.append(pid)

print("\nWaiting List:")
print(waiting_list)


# 5. Find destination with highest bookings

destination_count = {}

for pid, destination, status in bookings:

    if destination in destination_count:
        destination_count[destination] += 1
    else:
        destination_count[destination] = 1

most_booked = max(destination_count, key=destination_count.get)

print("\nMost Booked Destination:")
print(most_booked)