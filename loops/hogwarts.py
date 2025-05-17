# LISTS
students = ["Hermione", "Harry", "Ron"]

# Access list item
print(students[1])

# Iterate over and print list items. _ is not used cos we use ""student" after its declaration here
for student in students:
    print(student)

# LEN
for i in range(len(students)):
    print(i + 1, students[i])