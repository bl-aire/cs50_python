import csv

name = input("Enter your name: ")
home = input("Enter your home: ")

# Library sorted out escaping commas, appended data,
# Order doesn't matter when accessing data provided fieldnames is arranged etc
with open("students_DictWriter.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})