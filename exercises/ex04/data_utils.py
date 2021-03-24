"""Utility functions for wrangling data."""

__author__ = "730398645"


from csv import DictReader
DATA_DIRECTORY="../../data"
DATA_FILE_PATH=f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_27.csv"

file_handle = open("data/nc_durham_2015_march_21_to_27.csv", "r", encoding="utf8")
csv_file = DictReader(file_handle)

def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []

    for row in csv_file:
        rows.append(row)

    return(rows)
    file_handle.close()
    
    # TODO 0.1) Complete the implementation of this function here.

print(read_csv_rows(csv_file))

# TODO: Define the other functions here.