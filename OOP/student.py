def main():
    student = get_student()
    print(f"Hello, {student[0]} from {student[1]}!")

    student2 = get_student2()
    print(f"Hello, {student2['name']} from {student2['house']}!")

def get_student():
    name = input("What is your name? ")
    house = input("What is your name? ")
    return name, house

def get_student2():
    student = {
        'name': input("What is your name? "),
        'house': input("What is your name? ")
    }
    return student

if __name__ == "__main__":
    main()