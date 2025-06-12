def main():
    student = get_student()
    print(f"Hello, {student[0]} from {student[1]}!")

def get_student():
    name = input("What is your name? ")
    house = input("What is your name? ")
    return name, house

if __name__ == "__main__":
    main()