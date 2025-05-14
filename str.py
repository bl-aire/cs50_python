# Get input from user
# Strings can be formated using built-in methods. Strip() for instance removes whitespaces from the left and right
# There is also Capitalize(), Title() etc
name = input("What is your name? ").strip().title()

# Split user's name into first and last name

first, last = name.split(" ")

# Say hello to user
print(f"Hello {first}")
