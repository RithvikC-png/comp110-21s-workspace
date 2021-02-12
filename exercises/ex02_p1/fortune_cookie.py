"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730398645"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print("Now, go spread positive vibes!")
    print(fortune_cookie())

def fortune_cookie() -> str:
    a = randint(1, 4)

    if a < 2:
        return("The early bird gets the worm, but the second mouse gets the cheese")
    elif a < 3:
        return("A faithful friend is a strong defense")
    elif a < 4:
        return("A fresh start will put you on your way")
    else:
        return("A friend asks only for your time not your money")


# TODO 1: Define your fortune_cookie function here.


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 



if __name__ == "__main__":
    main()




