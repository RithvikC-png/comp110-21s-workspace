"""Example reading csv files."""

from csv import DictReader

file_handle = open("data/weather.csv", "r", encoding = "utf8")
csv_reader = DictReader(file_handle)

# A "Table" can be modeled as a list of rows, where a row
# is a dictionary with the column title as the key.
table: list[dict[str, str]] = []

for row in csv_reader:
    print(row)


# When we're done reading / working with a file, we should close it
file_handle.close()