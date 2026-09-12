import json
import os
from datetime import datetime

DATA_FILE = "students.json"


# DATA MANAGEMENT

def load_students():
    """Load students from JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    return []


def save_students():
    """Save students to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)

    print("Data saved successfully.")


students = load_students()


# GRADE CALCULATION

def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# ADD STUDENT

def add_student():
    print("\n===== ADD STUDENT =====")

    student_id = input("Enter student ID: ")

    # Check if ID already exists
    for student in students:
        if student["id"] == student_id:
            print("A student with this ID already exists.")
            return

    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": {},
        "attendance": 0,
        "total_classes": 0
    }

    students.append(student)
    save_students()

    print("Student added successfully!")

# DISPLAY STUDENTS

def display_students():
    print("\n===== ALL STUDENTS =====")

    if not students:
        print("No students registered.")
        return

    for student in students:
        print("--------------------------------")
        print(f"ID:       {student['id']}")
        print(f"Name:     {student['name']}")
        print(f"Age:      {student['age']}")
        print(f"Course:   {student['course']}")


# SEARCH STUDENT

def search_student():
    print("\n===== SEARCH STUDENT =====")

    search = input("Enter student ID or name: ").lower()

    found = False

    for student in students:
        if (
            student["id"].lower() == search
            or student["name"].lower() == search
        ):
            print("\nStudent found!")
            print(f"ID:       {student['id']}")
            print(f"Name:     {student['name']}")
            print(f"Age:      {student['age']}")
            print(f"Course:   {student['course']}")

            if student["marks"]:
                print("Marks:")
                for subject, mark in student["marks"].items():
                    print(f"  {subject}: {mark}")

            found = True

    if not found:
        print("Student not found.")


# UPDATE STUDENT

def update_student():
    print("\n===== UPDATE STUDENT =====")

    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:

            print("Leave a field empty to keep the current value.")

            name = input(f"Name ({student['name']}): ")
            age = input(f"Age ({student['age']}): ")
            course = input(f"Course ({student['course']}): ")

            if name:
                student["name"] = name

            if age:
                student["age"] = int(age)

            if course:
                student["course"] = course

            save_students()

            print("Student updated successfully!")
            return

    print("Student not found.")


# DELETE STUDENT

def delete_student():
    print("\n===== DELETE STUDENT =====")

    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:

            confirm = input(
                f"Delete {student['name']}? (yes/no): "
            ).lower()

            if confirm == "yes":
                students.remove(student)
                save_students()
                print("Student deleted successfully.")
            else:
                print("Deletion cancelled.")

            return

    print("Student not found.")


# ==============================
# RECORD MARKS
# ==============================

def record_marks():
    print("\n===== RECORD MARKS =====")

    student_id = input("Enter student ID: ")

    for student in students:

        if student["id"] == student_id:

            print(f"\nRecording marks for {student['name']}")

            number = int(input("How many subjects? "))

            for i in range(number):
                subject = input(f"Subject {i + 1}: ")
                mark = float(input(f"Mark for {subject}: "))

                if 0 <= mark <= 100:
                    student["marks"][subject] = mark
                else:
                    print("Mark must be between 0 and 100.")

            save_students()

            print("Marks recorded successfully.")
            return

    print("Student not found.")


# ==============================
# STUDENT RESULTS
# ==============================

def student_results():
    print("\n===== STUDENT RESULTS =====")

    student_id = input("Enter student ID: ")

    for student in students:

        if student["id"] == student_id:

            if not student["marks"]:
                print("No marks recorded.")
                return

            total = sum(student["marks"].values())
            number_of_subjects = len(student["marks"])
            average = total / number_of_subjects
            grade = calculate_grade(average)

            print("\n-----------------------------")
            print(f"Student: {student['name']}")
            print(f"ID:      {student['id']}")
            print("-----------------------------")

            for subject, mark in student["marks"].items():
                print(f"{subject}: {mark}")

            print("-----------------------------")
            print(f"Total:   {total}")
            print(f"Average: {average:.2f}")
            print(f"Grade:   {grade}")

            return

    print("Student not found.")


# CLASS STATISTICS


def class_statistics():
    print("\n===== CLASS STATISTICS =====")

    averages = []

    for student in students:

        if student["marks"]:
            average = sum(student["marks"].values()) / len(student["marks"])
            averages.append((student, average))

    if not averages:
        print("No marks have been recorded.")
        return

    class_average = sum(
        average for student, average in averages
    ) / len(averages)

    highest = max(averages, key=lambda x: x[1])
    lowest = min(averages, key=lambda x: x[1])

    print(f"Number of students: {len(students)}")
    print(f"Students with marks: {len(averages)}")
    print(f"Class average: {class_average:.2f}")

    print(
        f"Highest average: "
        f"{highest[0]['name']} ({highest[1]:.2f})"
    )

    print(
        f"Lowest average: "
        f"{lowest[0]['name']} ({lowest[1]:.2f})"
    )


# ATTENDANCE


def record_attendance():
    print("\n===== RECORD ATTENDANCE =====")

    student_id = input("Enter student ID: ")

    for student in students:

        if student["id"] == student_id:

            classes = int(input("Number of classes held: "))
            attended = int(input("Classes attended: "))

            if attended > classes:
                print("Attended classes cannot exceed classes held.")
                return

            student["total_classes"] = classes
            student["attendance"] = attended

            save_students()

            print("Attendance recorded.")
            return

    print("Student not found.")


# ==============================
# ATTENDANCE REPORT
# ==============================

def attendance_report():
    print("\n===== ATTENDANCE REPORT =====")

    student_id = input("Enter student ID: ")

    for student in students:

        if student["id"] == student_id:

            total = student["total_classes"]
            attended = student["attendance"]

            if total == 0:
                print("No attendance recorded.")
                return

            percentage = (attended / total) * 100

            print(f"\nStudent: {student['name']}")
            print(f"Classes held: {total}")
            print(f"Classes attended: {attended}")
            print(f"Attendance: {percentage:.2f}%")

            if percentage >= 75:
                print("Status: Good")
            else:
                print("Status: Attendance Warning")

            return

    print("Student not found.")


# GRADE STATISTICS

def grade_statistics():
    print("\nGRADE STATISTICS ")

    grades = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for student in students:

        if student["marks"]:

            average = (
                sum(student["marks"].values())
                / len(student["marks"])
            )

            grade = calculate_grade(average)
            grades[grade] += 1

    for grade, count in grades.items():
        print(f"Grade {grade}: {count} student(s)")

# STUDENT REPORT

def generate_report():
    print("\n===== STUDENT REPORT =====")

    student_id = input("Enter student ID: ")

    for student in students:

        if student["id"] == student_id:

            filename = f"report_{student_id}.txt"

            with open(filename, "w") as file:

                file.write("STUDENT ACADEMIC REPORT\n")
                file.write("=======================\n\n")

                file.write(f"Student ID: {student['id']}\n")
                file.write(f"Name: {student['name']}\n")
                file.write(f"Age: {student['age']}\n")
                file.write(f"Course: {student['course']}\n\n")

                file.write("RESULTS\n")
                file.write("-------\n")

                if student["marks"]:

                    total = sum(student["marks"].values())
                    average = total / len(student["marks"])
                    grade = calculate_grade(average)

                    for subject, mark in student["marks"].items():
                        file.write(f"{subject}: {mark}\n")

                    file.write(f"\nTotal: {total}\n")
                    file.write(f"Average: {average:.2f}\n")
                    file.write(f"Grade: {grade}\n")

                else:
                    file.write("No marks recorded.\n")

                file.write("\nGenerated: ")
                file.write(
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )

            print(f"Report generated: {filename}")
            return

    print("Student not found.")


# MAIN MENU

def main():

    while True:

        print("\n")
        print("========================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("========================================")
        print("1.  Add Student")
        print("2.  View All Students")
        print("3.  Search Student")
        print("4.  Update Student")
        print("5.  Delete Student")
        print("6.  Record Marks")
        print("7.  View Student Results")
        print("8.  Class Statistics")
        print("9.  Record Attendance")
        print("10. Attendance Report")
        print("11. Grade Statistics")
        print("12. Generate Student Report")
        print("13. Save Data")
        print("14. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            record_marks()

        elif choice == "7":
            student_results()

        elif choice == "8":
            class_statistics()

        elif choice == "9":
            record_attendance()

        elif choice == "10":
            attendance_report()

        elif choice == "11":
            grade_statistics()

        elif choice == "12":
            generate_report()

        elif choice == "13":
            save_students()

        elif choice == "14":
            save_students()
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


# START PROGRAM

if __name__ == "__main__":
    main()