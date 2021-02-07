"""A vaccination calculator."""

__author__ = "730398645"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
"""This program calculates how quickly people can be vaccinated from covid"""

__author__ = "730398645"

population = int(input("What is the population? "))
administered = int(input("How many doses have been administered? "))
doses = int(input("How many doses are being administered per day? "))
tp = int(input("What is your target percent vaccinated? "))

dtt = round((tp / int(100) * population * int(2)) - administered) / doses

today: datetime = datetime.today()
plus_days: timedelta = timedelta(dtt)
tgt: datetime = today + plus_days

print("We will reach " + str(tp) + "% vaccination in " + str(int(dtt)) + " days which falls on " + str(tgt.strftime("%B %d, %Y")))