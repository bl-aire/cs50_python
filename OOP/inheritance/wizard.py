# Students and Professors are Wizards, and they share the attribute name
# We use Inheritance to prevent unnecessary repetition
# Wizard ~ superclass and others are subclass

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name is required")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f'{self.name} {self.subject}'

student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")