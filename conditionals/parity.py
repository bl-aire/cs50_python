def main():
    x = int(input("Enter a number: "))
    print("Even" if even(x) else "Odd")

def even(num):
    #return True if num % 2 == 0 else False
    return num % 2 == 0

main()