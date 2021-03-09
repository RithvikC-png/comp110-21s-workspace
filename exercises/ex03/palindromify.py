"""EX03 - palindromify function."""

__author__: str = "730398645"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))
    print(palindromify("race", False))
    print(palindromify("han", True))


def palindromify(word: str, x: bool) -> str:
    """A way to palindrome inputs."""
    if x is False:
        new_statement = word[:: -1]
        return(word[0: len(word) - 1: 1] + new_statement)
        
    if x is True:
        palindrome = word[::-1]
        return str((word + palindrome))
    return()


if __name__ == "__main__":
    main()