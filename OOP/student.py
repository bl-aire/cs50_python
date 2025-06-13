def main():
    student = get_student()
    print(f"Hello, {student[0]} from {student[1]}!")

    student2 = get_student2()
    # Even if user enters location for Padma, Ravenclaw overrides it
    if student2['name'] == "Padma":
        student2['house'] = "Ravenclaw"
    print(f"Hello, {student2['name']} from {student2['house']}!")

def get_student():
    name = input("What is your name? ")
    house = input("What is your location? ")
    # tuple
    return name, house

def get_student2():
    # dictionary
    student = {
        'name': input("What is your name? "),
        'house': input("What is your location? ")
    }
    return student

if __name__ == "__main__":
    main()