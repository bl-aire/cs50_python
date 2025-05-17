# Continue requesting value till user enters a positive value
while True:
    n = int(input("What is n?"))
    if n > 0:
        break

for _ in range(n):
    print("meow")


# Modification
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        p = int(input("What is p?"))
        if p > 0:
            return p


def meow(p):
    for _ in range(p):
        print("meow")

main()