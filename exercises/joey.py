"""Should you go to class"""

score: int = int(0)

name: str = input("What is your name? ")

Q1 = input("Are you tired right now? ")
Q2 = input("Do you hate class? ")
Q3 = input("Is you laptop too far away? ")

if input(Q1) == "yes":
    score = score + int(1)
if input(Q2) == "yes":
    score = score + int(1)
if input(Q3) == "yes":
    score = score + int(1)

print(score)