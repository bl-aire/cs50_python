def main():
    x = int(input('What is x?'))
    print(f"x squared is: {square(x)}")

def square(y):
    return y * y

if __name__ == '__main__':
    main()