
import csv
import os

FILE_NAME = "students.csv"


# Initialize CSV file
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll", "Name", "Marks"])


# Add student
def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")

    if not roll or not name:
        print("Roll number and name cannot be empty!")
        return

    try:
        marks = float(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100!")
            return

    except ValueError:
        print("Invalid marks! Enter a number.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll"] == roll:
                print("Roll number already exists!")
                return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully!")


# Search student
def search_student():
    roll = input("Enter roll number to search: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll"] == roll:
                print("\nStudent Found!")
                print("Roll Number:", student["Roll"])
                print("Name:", student["Name"])
                print("Marks:", student["Marks"])
                return

    print("Student not found!")


# Update student
def update_student():
    roll = input("Enter roll number to update: ")

    students = []
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll"] == roll:
                found = True

                new_name = input("Enter new name: ")
                new_marks = input("Enter new marks: ")

                if new_name.strip():
                    student["Name"] = new_name

                if new_marks.strip():
                    try:
                        marks = float(new_marks)

                        if 0 <= marks <= 100:
                            student["Marks"] = str(marks)
                        else:
                            print("Invalid marks! Update cancelled.")
                            return

                    except ValueError:
                        print("Invalid marks! Update cancelled.")
                        return

            students.append(student)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["Roll", "Name", "Marks"]

            writer = csv.DictWriter(
                file, fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(students)

        print("Student updated successfully!")

    else:
        print("Student not found!")


# Delete student
def delete_student():
    roll = input("Enter roll number to delete: ")

    students = []
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll"] == roll:
                found = True
            else:
                students.append(student)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["Roll", "Name", "Marks"]

            writer = csv.DictWriter(
                file, fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(students)

        print("Student deleted successfully!")

    else:
        print("Student not found!")


# Display all students
def display_students():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\n========== STUDENT RECORDS ==========")

        found = False

        for student in reader:
            found = True

            print("Roll Number:", student["Roll"])
            print("Name:", student["Name"])
            print("Marks:", student["Marks"])
            print("-------------------------------------")

        if not found:
            print("No student records found!")


# Main program
def main():

    initialize_file()

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            search_student()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            display_students()

        elif choice == "6":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


# Program execution
if __name__ == "__main__":
    main()
