"""Should you go to class"""

name: str = input("What is your name? ")

Q1 = input("Are you tired right now? ")
Q2 = input("Do you hate this class? ")
Q3 = input("Is you laptop too far away? ")

if input(Q1) == "no" or "No":
    print("Go to class " + name) quit()
elif input(Q2) == "no" or "no":
    print("Go to class " + name) quit()
elif input(Q3) == "no" or "no":
    print("Go to class " + name) quit()
else:
    print("You should not go to class " + name)