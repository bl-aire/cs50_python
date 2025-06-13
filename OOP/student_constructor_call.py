class Student:
    # self refers to the object created. You can then use dot notation to populate it
    def __init__(self, name, house):
        if not name:
            raise ValueError("Student name or house cannot be empty")
        if house not in ["Abuja", "Lagos"]:
            raise ValueError("Please enter a valid house name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(f"Hello, {student.name} from {student.house}!")
    # print(student)


def get_student():
    # ALTERNATIVE approach using constructor call
    name = input("What is your name? ")
    house = input("What is your house? ")
    # Create object only if values are provided for name and house
    try:
        return Student(name, house)
    except ValueError:
        print("Please enter valid information")


if __name__ == "__main__":
    main()