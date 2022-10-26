"""Dictionary related utility functions."""

__author__ = "730561113"
from io import TextIOWrapper
# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    lines: list[dict[str, str]] = []
    file_handle: TextIOWrapper = open(filename, "r")
    for line in file_handle:
        line = line.lower()
        line = line.strip()
        lines.append(line)
    return lines