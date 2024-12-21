student_records = {}

while True:
    try:
        name = input("Enter your student's name: ").strip()
        if name.lower() == 'exit':
            break
        if not name:
            raise ValueError("Name cannot be empty.")
        if name in student_records:
            print(f"Student name already found in our records! Here is {name}'s information.")
            print(f"Age: {student_records[name]['Age']}")
            print(f"Major: {student_records[name]['Major']}")
            print(f"GPA: {student_records[name]['GPA']}")
            update = input("Would you like to update the student's information? (yes/no): ").strip().lower()
            if update != 'yes':
                continue

        age = input("Enter your student's age: ").strip()
        if not age.isdigit() or int(age) < 0 or int(age) > 120:
            raise ValueError("Invalid user input. Please enter a valid numerical age between 0 and 120.")
        age = int(age)

        major = input("Please enter the student's major: ").strip()
        if not all(c.isalpha() or c.isspace() for c in major):
            raise ValueError("This is not a valid major. Please enter your major only using letters and spaces.")

        grade = input("Please enter your student's GPA: ").strip()
        try:
            grade_point_average = float(grade)
        except ValueError:
            raise ValueError("GPA must be a numerical value.")
        if grade_point_average < 0.0 or grade_point_average > 4.0:
            raise ValueError("Invalid GPA entered. Please enter a valid GPA between 0.0 and 4.0.")

        student_records[name] = {'Age': age, 'Major': major, 'GPA': grade_point_average}

    except ValueError as e:
        print(f"Error: {e}")
        continue

while True:
    print("\nMain Menu")
    print("1: Look up student information")
    print("2: Delete student information")
    print("3: Exit")

    choice = input("Please select an option: ").strip()

    if choice == '3':
        break

    elif choice == '1':
        try:
            lookup = input("Please enter the student's name: ").strip()

            if lookup.lower() == 'back':
                continue

            if lookup in student_records:
                student = student_records[lookup]
                print(f"Student Information")
                print(f"Name: {lookup}")
                print(f"Age: {student['Age']}")
                print(f"Major: {student['Major']}")
                print(f"GPA: {student['GPA']}")
            else:
                print(f"'{lookup}' was not found within our records. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")
            continue

    elif choice == '2':
        while True:
            try:
                delete_name = input("\nEnter student name to delete (or 'back' to return to menu): ").strip()

                if delete_name.lower() == 'back':
                    break

                if delete_name in student_records:
                    confirm = input(f"Are you sure you want to delete {delete_name}'s information? (yes/no): ").strip().lower()
                    if confirm == 'yes':
                        del student_records[delete_name]
                        print(f"Information for {delete_name} has been deleted successfully!")
                    else:
                        print("Deletion cancelled.")
                else:
                    print(f"Student '{delete_name}' not found in records.")

            except Exception as e:
                print(f"An error occurred: {e}")
                continue
    else:
        print("Invalid choice. Please enter either 1, 2, or 3.")

print("\nThank you for using the Student Information System!")
