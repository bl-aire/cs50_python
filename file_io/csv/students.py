#  READ CSV

with open('students.csv') as csvfile:
    for line in csvfile:
        row = line.rstrip().split(",")
        #print(f"{row[0]} is in House{row[1]}.")

# REFACTOR

with open('students.csv') as csvfile:
    for line in csvfile:
        name, house = line.rstrip().split(",")
        #print(f"{name} is in House{house}.")

# SORTING

students   = []

with open('students.csv') as csvfile:
    for line in csvfile:
        name, house = line.rstrip().split(",")
        student = {'name': name, 'house': house}
        students.append(student)

for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} is in House{student['house']}.")
