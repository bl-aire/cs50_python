def main():
    score = int(input("Enter your score: "))
    print(grade(score))

def grade(a):
    # Boolean expression {or, and, if, elif, else }
    # Below illustrates how conditions can be chained. We can just check is score is above each boundary.
    # A for instance will be score >= 90
    if 90 <= a <= 100 :
        print("Grade: A")
    elif 80 <= a < 90 :
        print("Grade: B")
    elif  70 <= a < 80 :
        print("Grade: C")
    elif  60 <= a < 70 :
        print("Grade: D")
    else:
        print("Grade: F")

main()

