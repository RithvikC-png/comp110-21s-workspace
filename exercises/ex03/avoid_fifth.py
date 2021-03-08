"""EX03 - avoid_fifth function."""

__author__: str = "730398645"


def main() -> None:
    """Entrypoint of the program."""
    sentence: str = input("What would you like your sentence to be? ")
    # Put print statements here to test your function
    print("Your new sentence is: " + avoid_fifth(sentence))
    # ex. print(avoid_fifth("hello there"))
def avoid_fifth(sentence: str) -> str:
    """A way to remove the letter 'E'!"""
    print(f"You original sentece: {sentence}")
    delete_e = str("")

    for letter in sentence:
        if letter != "E" and letter != "e":
            delete_e = delete_e + letter
    return(delete_e)


if __name__ == "__main__":
    main()