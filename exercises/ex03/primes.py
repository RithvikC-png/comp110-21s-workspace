"""EX03 - prime functions."""

__author__: str = "730398645"


def main() -> None:
    """Entrypoint of the program."""
    number = (int(input("What number would you like to test? ")))
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    print(is_prime(number))

def is_prime(number: int) -> bool:
    numbers = range (2 , number)
    if number > 1:
        i: int = 0
        while i < len(numbers):
            if (number % numbers[i]) != 0:
                return False
                i += 1
            if (number % numbers[i]) == 0:
                return True
    if number <= 1:
        print("Composited")
        return False

if __name__ == "__main__":
    main()