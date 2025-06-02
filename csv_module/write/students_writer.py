import csv

name = input("Enter your name: ")
home = input("Enter your home: ")

# Library sorted out escaping commas, appended data etc
with open("students_write.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])