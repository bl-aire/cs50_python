def main():
    print_square(3)
    print_square2(4)

def print_square(n):
    # For each row in square
    for i in range(n):

        # For each brick in row
        for j in range(n):

            # Print brick
            print("#", end="")

        # For new line at the end of a row
        print()

def print_square2(n):
    for i in range(n):
        print_row(n)

def print_row(width):
    print("#" * width)

main()