# Seat status list
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# Variables
booked = 0
available = 0
available_seats = []

# Traverse seat list
for i in range(len(seats)):

    # Count booked seats
    if seats[i] == 1:
        booked += 1

    # Count available seats
    else:
        available += 1

        # Store available seat number
        available_seats.append(i + 1)

# Find first available seat
for i in range(len(seats)):

    if seats[i] == 0:
        first_available = i + 1
        break

# Calculate occupancy percentage
occupancy = (booked / len(seats)) * 100

# Display results
print("Booked Seats:", booked)
print("Available Seats:", available)
print("First Available Seat:", first_available)
print("Available Seat Numbers:", available_seats)
print("Bus Occupancy:", occupancy, "%")

# Check occupancy status
if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")