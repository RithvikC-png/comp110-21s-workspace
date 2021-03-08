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

    i = len(original)
    if x is False:
        while i > 0:
            palindrome_odd = original[i]
            i -= i
    
    return original + original[i]

if __name__ == "__main__":
    main()