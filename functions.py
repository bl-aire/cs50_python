# hello gets input from user and prints a response
def hello():
    name = input("What is your name?")
    print(f"You are making progress, {name}")

hello()

# helloo is a function with a parameter. It prints hello to the argument passed into the function when it is called
# user stores the user's input and this is passed as an argument into helloo when it is called
def helloo(to):
    print(f"Hello, {to}")

user = input("What is your name?")
helloo(user)