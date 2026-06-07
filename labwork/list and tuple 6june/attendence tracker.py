# Attendance record
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P',
              'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

present = 0
absent = 0

# Count present and absent days
for day in attendance:
    if day == 'P':
        present += 1
    else:
        absent += 1

print("Present Days =", present)
print("Absent Days =", absent)

# Calculate attendance percentage
percentage = (present / len(attendance)) * 100

print("Attendance Percentage =", percentage)

# Check eligibility
if percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")

# Display absent positions
print("Absent on Days:")

for i in range(len(attendance)):
    if attendance[i] == 'A':
        print(i + 1)