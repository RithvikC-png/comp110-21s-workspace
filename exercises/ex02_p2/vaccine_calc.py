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
    a = days_to_target

    # TODO 4: Call future_date and store result in a variable.
    c = future_date
    return(future_date)

    # TODO 5: Print the expected output using the variables above.
    print(days_to_target)

# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """The number of days to the target vaccination"""

    dtg: int(round(((target / int(100) * population * int(2)) - doses) / doses_per_day))

    today: datetime = datetime.today()
    b: timedelta = timedelta(dtg)
    g: datetime = today + b
    
    x = "We will reach " + str(target)
    y = "% vaccination in " + str(a)
    z = " days, which falls on " + str(g.strftime("%B %d, %Y"))

# TODO 3: Define future_date function
def future_date(datetime: int) -> str:
    """The date of target vaccination"""

if __name__ == "__main__":
    main()