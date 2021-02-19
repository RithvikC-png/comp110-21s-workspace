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
    # TODO 4: Call future_date and store result in a variable.
    b = future_date(a)
    # TODO 5: Print the expected output using the variables above.\

    x = "We will reach " + str(target)
    y = "% vaccination in " + str(a)
    z = " days which falls on " + str(b)
    print(x + y + z)


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """A function to calculate the number of days to vaccination."""
    days = int(round(((target / int(100) * population * int(2)) - doses) / doses_per_day))
    return(days)


# TODO 3: Define future_date function
def future_date(a: int) -> str:
    """A function to calculate the date of target vaccination."""
    today: datetime = datetime.today()
    plus_days: timedelta = timedelta(a)
    date_raw: datetime = today + plus_days
    date = date_raw.strftime("%B %d, %Y")
    return(date)


if __name__ == "__main__":
    main()