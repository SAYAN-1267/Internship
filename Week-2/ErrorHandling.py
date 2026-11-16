
try:
    file = open("sample.txt", "r")

    content = file.read()

    # Count words
    words = content.split()
    word_count = len(words)

    # Count lines
    file.seek(0)
    lines = file.readlines()
    line_count = len(lines)

    # Count characters
    char_count = len(content)

    print("----- WORD COUNTER -----")
    print("Total Words:", word_count)
    print("Total Lines:", line_count)
    print("Total Characters:", char_count)

    file.close()

except FileNotFoundError:
    print("File not found!")

