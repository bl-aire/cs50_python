# SYNTAX ERROR - example closing " is absent
print("Hello, World!")


# RUNTIME ERROR
# Keep asking user for values until they enter int. When they do return it and break the loop
# Else, tell them to input a number!

def main():
    x = get_int("What is x?")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
            # print("Please enter a number, boo! x is not an integer.")
            # user gets prompted again and again to enter new value

main()


# Example:

try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the ZeroDivisionError
    print("Cannot divide by zero")
except (TypeError, ValueError):
    # Handle TypeError or ValueError
    print("Invalid input type or value")
except:
    # Catch any other exception
    print("An error occurred")
else:
    # Code to execute if no exception occurs
    print("No error occurred")
finally:
    # Code that always executes, regardless of exceptions
    print("Finally block executed")
