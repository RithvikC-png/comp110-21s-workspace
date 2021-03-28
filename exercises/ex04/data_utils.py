"""Utility functions for wrangling data."""

__author__ = "730398645"


from csv import DictReader
from typing import Dict
from tabulate import tabulate


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return(rows)


    # TODO 0.1) Complete the implementation of this function here.
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
        for rows in column:
            for values in rows:
                N.append(values)
            Dictionary_A[column] = N
    return Dictionary_A