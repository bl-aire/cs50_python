import random
# from random import choice ALLOWS FOR SPECIFICITY AND I WOULDN'T HAVE TO USE DOT NOTATION TO ACCESS CHOICE


coin = random.choice(["heads", "tails"])
print(coin)


random_int = random.randint(1, 10)
print(random_int)


mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
for item in mylist:
    print(item)