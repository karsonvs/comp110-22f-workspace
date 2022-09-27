"""A tester code for utils program."""

__author__ = "730561113"


from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_single_even() -> None:
    xs: list[int] = [1,3,5,6,7]
    assert only_evens(xs) == [6]


def test_only_evens_many_evens() -> None:
    xs: list[int] = [4,4,4]
    assert only_evens(xs) == [4,4,4]


def test_sub_empty_list() -> None:
    xs: list[int] = []
    x: int = 1
    y: int = 3
    assert sub(xs, x, y) == []

def test_sub_negative_start() -> None:
    xs: list[int] = [1,2]
    x: int = -1
    y: int = 1
    assert sub(xs, x, y) == [1]


def test_sub_high_end_value() -> None:
    xs: list[int] = [1,2,3]
    x: int = 0
    y: int = 6
    assert sub(xs, x, y) == [1,2]


def test_concat_two_empty_lists() -> None:
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_one_empty_list() -> None:
    xs: list[int] = []
    ys: list[int] = [1,2]
    assert concat(xs, ys) == [1,2]


def test_concat_two_full_lists() -> None:
    xs: list[int] = [1,2]
    ys: list[int] = [3,4]
    assert concat(xs, ys) == [1,2,3,4]
