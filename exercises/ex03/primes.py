"""EX03 - prime functions."""

__author__: str = "730398645"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    print(is_prime(20))
    print(list_primes(5, 13))


def is_prime(x: int) -> bool:
    """Talk prime to me!"""
    numbers = range(2, x)
    if x > 1:
        if x == 2:
            return False
        i: int = 0
        while i < len(numbers):
            check: int = numbers[i]
            if (x % check) != 0:
                return True
                i += 1
            if (x % check) == 0:
                return False
    if x <= 1:
        return False


def list_primes(ln: int, un: int) -> list[int]:
    """What are the prime numbers in this range?"""
    prime_numbers = []
    while(ln < un):
        if is_prime(ln):
            prime_numbers.append(ln)
        ln += 1
    return prime_numbers


if __name__ == "__main__":
    main()