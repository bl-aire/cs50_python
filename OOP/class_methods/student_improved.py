# Cleans up the code as everything related to Student is within the class here
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f'Student {self.name} from {self.house}'

    @classmethod
    def get(cls):
        name = input('Enter student name: ')
        house = input('Enter student house: ')
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__ == '__main__':
    main()