# Student Performance Analytics System
'''Problem Statement 
A coaching institute wants to analyze student performance. 
Store details of at least 30 students in a dictionary. 
Example Structure 
students = { 
    "S101": {"name": "Anuj", "marks": 85}, 
    "S102": {"name": "Rahul", "marks": 72} 
} 
Requirements 
1. Display all student records.  
2. Search a student using Student ID.  
3. Add a new student.  
4. Update marks of an existing student.  
5. Delete a student.  
6. Find topper and lowest scorer.  
7. Calculate class average.  
8. Count pass and fail students.  
9. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
10. Display students scoring above average.  
11. Display top 5 performers.  
12. Create a separate dictionary for scholarship students (marks > 85).'''

students = {
    "S101": {"name": "Rahul", "marks": 85},
    "S102": {"name": "Priya", "marks": 92},
    "S103": {"name": "Aman", "marks": 45},
    "S104": {"name": "Riya", "marks": 78},
    "S105": {"name": "Karan", "marks": 60}
}

while True:

    print("\n1. Display Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Topper and Lowest Scorer")
    print("7. Class Average")
    print("8. Pass and Fail Count")
    print("9. Generate Grades")
    print("10. Students Above Average")
    print("11. Scholarship Students")
    print("12. Exit")

    ch = int(input("Enter Choice: "))

    # Display
    if ch == 1:

        for sid in students:
            print(sid, students[sid])

    # Search
    elif ch == 2:

        sid = input("Enter Student ID: ")

        if sid in students:
            print(students[sid])
        else:
            print("Student Not Found")

    # Add
    elif ch == 3:

        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))

        students[sid] = {"name": name, "marks": marks}

        print("Student Added")

    # Update
    elif ch == 4:

        sid = input("Enter ID: ")

        if sid in students:
            marks = int(input("Enter New Marks: "))
            students[sid]["marks"] = marks
            print("Marks Updated")

    # Delete
    elif ch == 5:

        sid = input("Enter ID: ")

        if sid in students:
            del students[sid]
            print("Student Deleted")

    # Topper and Lowest
    elif ch == 6:

        max_marks = -1
        min_marks = 101

        topper = ""
        lowest = ""

        for sid in students:

            if students[sid]["marks"] > max_marks:
                max_marks = students[sid]["marks"]
                topper = students[sid]["name"]

            if students[sid]["marks"] < min_marks:
                min_marks = students[sid]["marks"]
                lowest = students[sid]["name"]

        print("Topper =", topper, max_marks)
        print("Lowest Scorer =", lowest, min_marks)

    # Average
    elif ch == 7:

        total = 0

        for sid in students:
            total += students[sid]["marks"]

        avg = total / len(students)

        print("Class Average =", avg)

    # Pass Fail
    elif ch == 8:

        p = 0
        f = 0

        for sid in students:

            if students[sid]["marks"] >= 50:
                p += 1
            else:
                f += 1

        print("Pass =", p)
        print("Fail =", f)

    # Grades
    elif ch == 9:

        for sid in students:

            marks = students[sid]["marks"]

            if marks >= 90:
                grade = "A"

            elif marks >= 75:
                grade = "B"

            elif marks >= 50:
                grade = "C"

            else:
                grade = "F"

            print(students[sid]["name"], "-", grade)

    # Above Average
    elif ch == 10:

        total = 0

        for sid in students:
            total += students[sid]["marks"]

        avg = total / len(students)

        print("Students Above Average:")

        for sid in students:

            if students[sid]["marks"] > avg:
                print(students[sid]["name"])

    # Scholarship Students
    elif ch == 11:

        scholarship = {}

        for sid in students:

            if students[sid]["marks"] > 85:
                scholarship[sid] = students[sid]

        print("Scholarship Students:")
        print(scholarship)

    # Exit
    elif ch == 12:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")