# Product ID and status
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

pass_count = 0
fail_count = 0

print("Failed Product IDs:")

for pid, status in products:
    if status == "Fail":
        print(pid)
        fail_count += 1
    else:
        pass_count += 1

print("Passed Products =", pass_count)
print("Failed Products =", fail_count)

# Calculate pass percentage
percentage = (pass_count / len(products)) * 100

print("Pass Percentage =", percentage)

# Stop if 3 failures are found
fails = 0

for pid, status in products:
    if status == "Fail":
        fails += 1

    if fails == 3:
        print("3 failures found. Stopping check.")
        break