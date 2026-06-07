# List of numbers
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# Empty list to store pairs
consecutive_pairs = []

# Traverse list
for i in range(len(numbers) - 1):

    # Check if numbers are consecutive
    if numbers[i + 1] == numbers[i] + 1:

        print(numbers[i], "and", numbers[i + 1], "are consecutive")

        # Store pair in list
        consecutive_pairs.append((numbers[i], numbers[i + 1]))

# Display all pairs
print("Consecutive Pairs:", consecutive_pairs)

