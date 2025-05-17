# DICTIONARY
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# Print values
print(students.get("Hermione"))
print(students["Draco"])

# Print values and keys
for student in students:
    print(student, students[student], sep=",")

# LIST OF DICTIONARIES
pupils = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter"
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russell terrier"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None
    }
]

for pupil in pupils:
    print(pupil["name"], pupil["patronus"], sep="," )