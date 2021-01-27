"""Should you go to class"""

name: str = input("What is your name? ")

Q1 = input("Are you tired right now? ")
Q2 = input("Do you hate class? ")
Q3 = input("Is you laptop too far away? ")

score = int(0)

if Q1 == "yes"
    score = score + 1
if Q2 == "yes"
    score = score + 1
if Q3 == "yes"
    score = score + 1

if score >= 2
    print("You should not go to class " + name)
if score < 2
    print("You should go to class " + name)