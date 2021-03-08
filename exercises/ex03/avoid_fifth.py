"""EX03 - avoid_fifth function."""

__author__: str = "730398645"


def main() -> None:
    """Entrypoint of the program."""
    input_sentence: str = input("What would you like your sentence to be? ")
    # Put print statements here to test your function
    avoid_fifth(input_sentence)
    # ex. print(avoid_fifth("hello there"))
    print(f"Original Sentece: {input_sentence}")
    
    return(input_sentence)


if __name__ == "__main__":
    main()