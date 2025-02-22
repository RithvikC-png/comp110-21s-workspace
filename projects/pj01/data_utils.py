"""Utility functions for wrangling data."""

__author__ = "730398645"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return(rows)


def column_values(rows: list[dict[str, str]], column: str) -> list[str]:
    """Arrange the CSV file by column."""
    charts: list[str] = []
    for row in rows:
        charts.append(row[column])
    return(charts)


# TODO: Define the other functions here.
def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Convert rows into columns."""
    table: dict[str, list[str]] = {}
    for column in rows[0]:
        values = column_values(rows, column)
        table[column] = values
    return table


def head(columns: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Create a table of values under each header."""
    Dictionary_A: dict[str, list[str]] = {}
    for column in columns:
        N: list[str] = []
        column_values = columns[column]
        if rows >= len(column_values):
            rows = len(column_values)
        for i in range(rows):
            N.append(column_values[i])
        Dictionary_A[column] = N
    return Dictionary_A


def select(columns: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """A function to select particular columns."""
    Dictionary_Select: dict[str, list[str]] = {}
    for headers in names:
        List_A: list[str] = []
        List_A = columns[headers]
        Dictionary_Select[headers] = List_A
    return Dictionary_Select


def count(values: list[str]) -> dict[str, int]:
    """Display the number of each category."""
    Dictionary_A: dict[str, int] = {}
    for lines in values:
        if lines in Dictionary_A:
            Dictionary_A[lines] += 1
        else:
            Dictionary_A[lines] = 1
    return Dictionary_A 
