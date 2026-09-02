from students import add_student, display_students, search_student

while True:
    print("\n===== STUDENT GRADE SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")






