"""Dictionary related utility functions."""

__author__ = "730561113"

from csv import DictReader
# Define your functions below


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Iterates through a csv and turns it into a list of the rows."""
    result: list[dict[str,str]] = []
    file_handle = open(path, "r", encoding = "utf8")
    csv_reader = DictReader(path)
    for line in csv_reader:
        result.append(line)
    file_handle.close()
    return result



def column_values(xs: list[dict[str, str]], column: str) -> list[str]:
    """Creates a list of strings that contains all of the values in a column."""
    result: list[str] = []
    for row in xs:
        x: str = row[column]
        result.append(x)
    return result


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Takes a table of rows and turns into a table of columns."""
    result: dict[str, list[str]] = []
    first: dict[str,str] = rows[0]
    for column in first:
        result[column] = column_values(rows, column)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Takes a table of rows and turns the number of rows specified."""
    result: dict[str, list[str]] = []
    for x in table:
        xs: list[str] = []
        for row in table[x]:
            if len(xs) < rows:
                xs.append(row)
        result[x] = xs
    return result


def select(xs: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Takes a table of columns and creates a smaller one with only the names provided for the columns."""
    result: dict[str, list[str]] = {}
    for column in names:
        result[column] = xs[column]
    return result


def concat(xs: dict[str, list[str]], ys: dict[str, list[str]]) -> dict[str, list[str]]:
    """Takes two tables of columns and combines them into one table."""
    result: dict[str, list[str]] = {}
    for x in xs:
        result[x] = xs[x]
    for x in ys:
        if x in result:
            result[x] += ys[x]
        else:
            result[x] = ys[x]
    return result


def count(xs: list[str]) -> dict[str, int]:
    """Takes a list and creates a dictionary with each key being an item in the list and each value being the number of times it appears in the list."""
    result: dict[str, int] = {}
    for i in range(len(xs)):
        if xs[i] in result:
            result[list[i]] += 1
        else:
            result[list[i]] = 1
    return result