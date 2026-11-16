
# Take list input from user
numbers = list(map(int, input("Enter numbers: ").split()))

# Initialize largest and smallest
largest = numbers[0]
smallest = numbers[0]

# Traverse the list
for num in numbers:

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

# Display results
print("Largest number:", largest)
print("Smallest number:", smallest)
