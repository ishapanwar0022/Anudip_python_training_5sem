#8. String-Based Attendance Tracker 
'''Problem Statement 
Attendance of a student for 15 days is represented as: 
PPAPPPAAPPPPAPP 
Where: 
• P = Present  
• A = Absent  
Tasks 
Write a program to: 
1. Count Present and Absent days.  
2. Calculate attendance percentage.  
3. Find the longest consecutive streak of Presence.  
4. Find the longest consecutive streak of Absence.  
5. Determine whether attendance is below 75%. '''

# String Based Attendance Tracker

attendance = input("Enter Attendance Record: ")

present = attendance.count("P")
absent = attendance.count("A")

percentage = (present / len(attendance)) * 100

# Longest Present Streak
max_p = 0
current_p = 0

for ch in attendance:

    if ch == "P":
        current_p += 1

        if current_p > max_p:
            max_p = current_p

    else:
        current_p = 0

# Longest Absent Streak
max_a = 0
current_a = 0

for ch in attendance:

    if ch == "A":
        current_a += 1

        if current_a > max_a:
            max_a = current_a

    else:
        current_a = 0

print("Present Days =", present)
print("Absent Days =", absent)
print("Attendance Percentage =", percentage)

print("Longest Present Streak =", max_p)
print("Longest Absent Streak =", max_a)

if percentage < 75:
    print("Attendance Status = Below 75%")
else:
    print("Attendance Status = Above 75%")