class Student:
    def __init__(self):
        self.house = None
        self.name = None

def main():
    student = get_student()
    print(f"Hello,{student.name} from {student.house}")

def get_student():
    # CREATING an object using the mold(class created earlier)
    student = Student()
    student.name = input("What is your name? ")
    student.house = input("What is your house? ")
    return student

if __name__ == "__main__":
    main()