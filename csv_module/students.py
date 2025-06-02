# Import library for reading csv
import csv

# Empty array that will house data collected from csv
students = []

# Open file via file i/o method, read file via csv
# Loop through csv data rows, deconstruct data in rows and append them in array created earlier
with open('students.csv') as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

# Loop through students array, sort array via student name key and print output
# Lambda is an anonymous function that accepts student as a parameter and returns the name variable
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from house{student['home']}")