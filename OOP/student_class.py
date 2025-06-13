class Student:
    # self refers to the object created. You can then use dot notation to populate it
    def __init__(self, name, house):
        self.house = name
        self.name = house

def main():
    student = get_student()
    print(f"Hello, {student.name} from {student.house}!")

def get_student():
    # Creating an object using the mold(class created earlier)

    # student = Student()
    # student.name = input("What is your name? ")
    # student.house = input("What is your house? ")

    # Alternative approach using constructor call

    name = input("What is your name? ")
    house = input("What is your house? ")
    return Student(name, house)

if __name__ == "__main__":
    main()