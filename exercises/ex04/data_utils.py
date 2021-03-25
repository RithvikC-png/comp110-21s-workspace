"""Utility functions for wrangling data."""

__author__ = "730398645"


from csv import DictReader

table: dict[str, list[str]] = {}
column: list = []
rows: list[dict[str, str]] = []

def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_file:
        rows.append(row)
    return(rows)
    file_handle.close()
    # TODO 0.1) Complete the implementation of this function here.
def column_values(rows: list[dict[str, str]], column: str) -> list[str]:
    """Arrange the CSV file by column"""
    charts: list[str] = []
    for row in rows:
        charts.append(column)
    
    return(charts)

print(read_csv_rows(csv_file))
print(column_values(table, column))

# TODO: Define the other functions here.