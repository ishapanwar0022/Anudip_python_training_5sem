#1. Student Performance Analytics System 
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
12. Create a separate dictionary for scholarship students (marks > 85). '''

# Student Performance Analytics System

students = {
    "S101": {"name": "Rahul", "marks": 85},
    "S102": {"name": "Priya", "marks": 92},
    "S103": {"name": "Aman", "marks": 45}
}

while True:

    print("\n1. Display Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Class Average")
    print("8. Pass/Fail Count")
    print("9. Grade Report")
    print("10. Exit")

    choice = int(input("Enter Choice: "))

    # Display
    if choice == 1:

        for sid in students:
            print(sid, students[sid])

    # Search
    elif choice == 2:

        sid = input("Enter Student ID: ")

        if sid in students:
            print(students[sid])
        else:
            print("Student Not Found")

    # Add
    elif choice == 3:

        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))

        students[sid] = {"name": name, "marks": marks}

        print("Student Added")

    # Update
    elif choice == 4:

        sid = input("Enter ID: ")

        if sid in students:
            marks = int(input("Enter New Marks: "))
            students[sid]["marks"] = marks
            print("Marks Updated")
        else:
            print("Student Not Found")

    # Delete
    elif choice == 5:

        sid = input("Enter ID: ")

        if sid in students:
            del students[sid]
            print("Student Deleted")
        else:
            print("Student Not Found")

    # Topper
    elif choice == 6:

        topper = ""
        highest = 0

        for sid in students:

            if students[sid]["marks"] > highest:

                highest = students[sid]["marks"]
                topper = students[sid]["name"]

        print("Topper:", topper)
        print("Marks:", highest)

    # Average
    elif choice == 7:

        total = 0

        for sid in students:
            total += students[sid]["marks"]

        average = total / len(students)

        print("Average Marks =", average)

    # Pass Fail
    elif choice == 8:

        pass_count = 0
        fail_count = 0

        for sid in students:

            if students[sid]["marks"] >= 50:
                pass_count += 1
            else:
                fail_count += 1

        print("Pass Students =", pass_count)
        print("Fail Students =", fail_count)

    # Grades
    elif choice == 9:

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

    # Exit
    elif choice == 10:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")