# WHILE
i = 3
while i != 0:
    print("meow")
    i -= 1

i = 0
while i < 3:
    print("woof")
    i += 1

# FOR
# with range(), we can avoid hard-coding [0, 1, 2] and if I wanted to iterate up to a million, it's easy
# _ is used to replace i so we don't name a variable and end up not using it
for _ in range(3):
    print("mooo")

print("meow\n" * 3, end = "")