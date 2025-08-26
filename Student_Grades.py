
students = {}
while True:
        print("1. Add new student and grade")
        print("2. Update existing student’s grade")
        print("3. Print all student grades")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter student name: ")
            if name in students:
                print("Student already exists! Use option 2 to update.")
            else:
                grade = input("Enter grade: ")
                students[name] = grade
                print(f"{name} added with grade {grade}.")
        
        elif choice == "2":
            name = input("Enter student name: ")
            if name in students:
                grade = input("Enter new grade: ")
                students[name] = grade
                print(f"{name}'s grade updated to {grade}.")
            else:
                print("Student not found! Use option 1 to add first.")

        elif choice == "3":
            if students:
                print("\nStudent Grades:")
                for name, grade in students.items():
                    print(f"{name}: {grade}")
            else:
                print("No student records found.")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please enter 1-4.")