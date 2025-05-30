def main():
    name = input("What is your name?")
    print(hello(name))

def hello(to="Blaire"):
    return f"Hello, {to}!"

if __name__ == "__main__":
    main()