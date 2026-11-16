
# Create an empty list
items = []


# CREATE - Add element
def create():
    value = input("Enter value to add: ")
    items.append(value)
    print("Element added successfully!")


# READ - Display elements
def read():
    if len(items) == 0:
        print("List is empty!")
    else:
        print("List elements:", items)


# UPDATE - Modify element
def update():
    read()

    if len(items) == 0:
        return

    try:
        index = int(input("Enter index to update: "))

        if 0 <= index < len(items):
            new_value = input("Enter new value: ")
            items[index] = new_value
            print("Element updated successfully!")
        else:
            print("Invalid index!")

    except ValueError:
        print("Please enter a valid index!")


# DELETE - Remove element
def delete():
    read()

    if len(items) == 0:
        return

    try:
        index = int(input("Enter index to delete: "))

        if 0 <= index < len(items):
            items.pop(index)
            print("Element deleted successfully!")
        else:
            print("Invalid index!")

    except ValueError:
        print("Please enter a valid index!")


# Main menu
while True:

    print("\n===== LIST CRUD OPERATIONS =====")
    print("1. Create (Add)")
    print("2. Read (Display)")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create()

    elif choice == "2":
        read()

    elif choice == "3":
        update()

    elif choice == "4":
        delete()

    elif choice == "5":
        print("Program exited successfully!")
        break

    else:
        print("Invalid choice! Try again.")
