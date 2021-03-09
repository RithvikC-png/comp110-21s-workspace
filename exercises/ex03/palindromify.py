"""EX03 - palindromify function."""

__author__: str = "730398645"

original: str = input("What would you like to Palindromify? ")
odd_even: bool = (len(original) % 2)

if odd_even == 0:
    x = True
else:
    x = False

def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))
    print(palindromify(original, x))


def palindromify(original: str, x: bool) -> str:
    """A way to palindrome inputs."""
    if x is True:
        palindrome = original[::-1]
        return (original + palindrome)

    if x is False:
        new_statement = original[::-1]
    return(original[0:len(original) -1 :1] + new_statement)

if __name__ == "__main__":
    main()