"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730398645"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

a: int = randint(1,4)

if "a" < 2
    print("The early bird gets the worm, but the second mouse gets the cheese")
elif "a" < 3
    print("A faithful friend is a strong defense")
elif "a" < 4
    print("A fresh start will put you on your way")
else
    print("A friend asks only for your time not your money")

print("Now, go spread positive vibes!")