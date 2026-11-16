
import json

try:
    # Open JSON file
    with open("students.json", "r") as file:

        # Load JSON data
        data = json.load(file)

    # Print formatted output
    print("----- STUDENT DETAILS -----")

    for student in data["students"]:
        print("\nStudent ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])

except FileNotFoundError:
    print("JSON file not found!")

except json.JSONDecodeError:
    print("Invalid JSON format!")
