
import json

# Student data
student = {
    "name": "Sayan",
    "age": 21,
    "course": "Computer Science",
    "marks": 85
}

# Create and write data into JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully!")

# Read data from JSON file
with open("student.json", "r") as file:
    data = json.load(file)

# Display data
print("\nStudent Details:")
print("Name:", data["name"])
print("Age:", data["age"])
print("Course:", data["course"])
print("Marks:", data["marks"])
