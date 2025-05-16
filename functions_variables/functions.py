# hello gets input from user and prints a response
def hello():
    name = input("What is your name?")
    print(f"You are making progress, {name}")

hello()

# helloo is a function with a parameter. It prints hello to the argument passed into the function when it is called
# user stores the user's input and this is passed as an argument into helloo when it is called
# World is set as a default argument
def helloo(to="World"):
    print(f"Hello, {to}")

user = input("What is your name?")
helloo(user)

# This prints "Hello, World"
helloo()


# Functions have to be defined before they are used.
def main():
    name = input("What is your name?")
    test()

def test(to="World"):
    print(f"Hello, {to}")

main()



# Return. What if we do not want a function to have a side effect @CALCULATOR.PY
