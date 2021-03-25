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
    return(rows)
    file_handle.close()


    # TODO 0.1) Complete the implementation of this function here.
def column_values(rows: list[dict[str, str]], column: str) -> list[str]:
    """Arrange the CSV file by column."""
    charts: list[str] = []
    for row in rows:
        charts.append(row[column])

    return(charts)


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Convert rows into columns."""
    headers: dict[str, list[str]] = {}
    for row in rows:
        headers = {"subject_age": [column_values]}
    
    return(headers)


# TODO: Define the other functions here.