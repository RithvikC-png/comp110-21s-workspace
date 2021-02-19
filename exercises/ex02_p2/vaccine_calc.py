"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730398645"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))


    # TODO 2: Call days_to_target and store result in a variable.
    a = days_to_target(population, doses, doses_per_day, target)
    print(a)
    # TODO 4: Call future_date and store result in a variable.
    # TODO 5: Print the expected output using the variables above.

# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    days = int(round((target / int(100) * population * int(2)) - doses) / doses_per_day)
# TODO 3: Define future_date function

if __name__ == "__main__":
    main()