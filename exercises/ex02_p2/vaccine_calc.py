"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730398645"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))

    today: datetime = datetime.today()

    # TODO 2: Call days_to_target and store result in a variable.
    return(days_to_target)
    days_to = days_to_target
    # TODO 4: Call future_date and store result in a variable.
    return(future_date)
    # TODO 5: Print the expected output using the variables above.

    plus_days: timedelta = timedelta(days_to)    

    x = "We will reach " + str(target)
    y = "% vaccination in " + str(days_to_target)
    z = " days, which falls on " + str(future_date.strftime("%B %d, %Y"))

    print(x + y + z)

# TODO 1: Define days_to_target function
def days_to_target() -> None:
    """The number of days to the target vaccination"""

    days_to_target = int(round(((target / int(100) * population * int(2)) - doses) / doses_per_day))

# TODO 3: Define future_date function
def future_date() -> None:
    """The date of target vaccination"""

    datetime = today + plus_days

if __name__ == "__main__":
    main()

print(main)




