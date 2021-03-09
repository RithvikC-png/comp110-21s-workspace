"""EX03 - prime functions."""

__author__: str = "730398645"


def main() -> None:
    """Entrypoint of the program."""
    number = (int(input("What number would you like to test? ")))
    lower_number = (int(input("What is your lower number? ")))
    upper_number = (int(input("What is your upper number? ")))
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    print(is_prime(number))
    print(list_primes(lower_number, upper_number))


def is_prime (number: int) -> bool:
    """Talk prime to me!"""
    numbers = range (2, number)
    if number > 1:
        if number == 2:
            return False
        i: int = 0
        while i < len(numbers):
            check: int = numbers[i]
            if (number % check) != 0:
                return False
                i += 1
            if (number % check) == 0:
                return True
    if number <= 1:
        return False

def list_primes(lower_number: int, upper_number: int) -> list[int]:
    """What are the prime numbers in this range?"""
    prime_numbers = []
    while(lower_number < upper_number):
        if is_prime(lower_number):
            prime_numbers.append(lower_number)
        lower_number += 1
    return prime_numbers


if __name__ == "__main__":
    main()