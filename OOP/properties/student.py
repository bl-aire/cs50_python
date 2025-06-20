class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Student name cannot be empty")
        self._name = name

    # GETTER
    @property
    def house(self):
        return self._house

    # SETTER
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house name")
        self._house = house


def main():
    student = get_student()
    # Override whatever house is entered initially but
    # when house() setter is introduced, the setter is called instead here throwing a ValueError cos house is INVALID
    #....hence, we take out line 31 and use the setter when _house needs to be updated
    # self.house in other parts of the code call the setter
    # Instance variable = _house but Property is called house

    # student.house = "Number Four, Privet Drive"
    print(student)

def get_student():
    name = input("What is your name? ")
    house = input("What is your house? ")
    return Student(name, house)

if __name__ == "__main__":
    main()