# Import library for reading csv and add column titles in the csv file
import csv

# Empty array that will house data collected from csv
students = []

# Open file via file i/o method, read file via csv
# Loop through csv data rows and append them in array created earlier
# csv.reader returns array so we can use row[i] to access data
# csv.DictReader returns a dictionary
with open('students.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

# Loop through students array, sort array via student name key and print output
# Lambda is an anonymous function that accepts student as a parameter and returns the name variable
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from house {student['home']}")