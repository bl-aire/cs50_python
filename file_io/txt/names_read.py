# UNSORTED OUTPUT
with open('names.txt', 'r') as file:
    for line in file:
        print(f"Hello, {line.rstrip()}!")


# FOR A SORTED OUTPUT:
names = []

with open('names.txt') as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}!")


# ALTERNATIVE
with open('names.txt') as file:
    for line in sorted(file):
        print(f"Hello, {line.rstrip()}!")