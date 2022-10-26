"""Tester file for dictionary functions."""


__author__ = "730561113"


import pytest
from dictionary import invert, favorite_color, count


def test_empty_dictionary() -> None:
    """Tests invert when there is an empty dictionary."""
    assert invert({}) == {}


def test_keyerror() -> None:
    """Tests if it returns the proper error if duplicate key is found."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_one_key() -> None:
    """Looks at a dicionary with one key-value pair and flips them."""
    assert invert({"Kris": "Jordan"}) == {"Jordan": "Kris"}


def test_multiple_keys() -> None:
    """Tests if invert works properly with multiple key-value pairs inputted."""
    assert invert({"Kris": "Jordan", "cat": "apple"}) == {"Jordan": "Kris", "apple": "cat"}


def test_empty_color() -> None:
    """Tests if function still works if there is an empty dictionary."""
    assert favorite_color({}) == ""


def test_color_tie() -> None:
    """Tests to find what the most repeated color in a dictionary is."""
    assert favorite_color({"Chris": "blue", "Karson": "green"}) == "blue"


def test_multiple_colors() -> None:
    """Tests if function works when a color appears multiple times."""
    assert favorite_color({"Karson": "blue", "Collin": "yellow", "Chuck": "yellow"}) == "yellow"


def test_empty_list() -> None:
    """Tests if count works with an empty list."""
    assert count([]) == {}


def test_single_values() -> None:
    """Tests when there are multiple different values."""
    list = ["a", "b", "c", "d"]
    assert count(list) == {"a": 1, "b": 1, "c": 1, "d": 1}


def test_repeated_values() -> None:
    """Tests when a value is repeated in the list."""
    list = ["a", "a", "b", "c", "b"]
    assert count(list) == {"a": 2, "b": 2, "c": 1}