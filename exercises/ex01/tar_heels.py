"""An exercise in remainders and boolean logic."""

__author__ = "730398645"


# Begin your solution here...

a = int(input("Enter a number "))

if (a % 2) == 0 and (a % 7) == 0:
    print("TAR HEELS")
elif (a % 2) == 0:
    print("TAR")
elif (a % 7) == 0:
    print("HEELS")
else:
    print("CAROLINA")
