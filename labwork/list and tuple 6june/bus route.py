# Passenger count at each stop
passengers = [12, 18, 25, 30, 28, 15, 8]

# Find busiest stop
highest = max(passengers)

stop_no = passengers.index(highest) + 1

print("Busiest Stop =", stop_no)
print("Passengers =", highest)

# Stops with fewer than 10 passengers
print("\nStops with fewer than 10 passengers:")

for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1)

# Calculate average passengers
average = sum(passengers) / len(passengers)

print("\nAverage Passengers =", average)

# Check if any stop exceeded 25 passengers
found = False

for p in passengers:
    if p > 25:
        found = True

if found:
    print("A stop exceeded 25 passengers")
else:
    print("No stop exceeded 25 passengers")