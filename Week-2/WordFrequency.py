
# Take input from user
text = input("Enter a sentence: ")

# Convert text into lowercase
text = text.lower()

# Split sentence into words
words = text.split()

# Create an empty dictionary
frequency = {}

# Count word frequency
for word in words:

    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1

# Display word frequency
print("\nWord Frequency:")

for word, count in frequency.items():
    print(word, ":", count)
