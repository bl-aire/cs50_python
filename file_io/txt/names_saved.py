name = input("Enter your name: ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

# ALTERNATIVELY, this closes the file automatically after file.writ(f"{name}\n") is run:
# with open("students.csv", "a") as file:
#   file.write(f"{name}\n")

