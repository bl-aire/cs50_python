x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))

# User input comes as strings so x and y are concatenated instead of added if int() is not used

print(x + y)

a = float(input("Enter a number for a: "))
b = float(input("Enter a number for b: "))

print(a + b)

# Round up
print(round(0.05555, 2))
print(f"{a:.3f}")

# Return

def main():
    q= int(input("Enter a number for q: "))
    print("q squared is:", square(q))

def square(n):
    return n ** 2
    # n * n....n ** 2...pow(n, 2)

main()

