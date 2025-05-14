# Get input from user and greet user
name = input("What is your name? ")

# Strings can be formated using built-in methods. Strip() for instance removes whitespaces. There is also Capitalize(), Title() etc
name = name.strip()
print(f"Hello {name}")
