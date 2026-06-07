# Create an empty dictionary to store attendance
attendance_tracker = {}

# Loop to get attendance for 30 students
for i in range(30):
    # Ask the user for input
    roll_number = input("Enter roll number: ")
    Attendance = input("Enter status (Present/Absent): ")
    
    # Store the data in the dictionary
    attendance_tracker[roll_number] = Attendance

print("\n Students who are Present ")

# Display the roll number of students who are Present
for roll_number, Attendance in attendance_tracker.items():
    if Attendance == "Present":
        print(f"Roll Number: {roll_number}")

