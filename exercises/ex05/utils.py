"""List utility function program."""

__author__ = "730561113"


def only_evens(xs: list[int]) -> list[int]:
    evens: list[int] = []
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            evens.append(xs[i])
        i += 1
    return evens


def concat(xs: list[int], ys: list[int]) -> list[int]:
    concat_list: list[int] = []
    i: int = 0
    while i < len(xs):
        concat_list.append(xs[i])
        i += 1
    i = 0
    while i < len(ys):
        concat_list.append(ys[i])
        i += 1
    return concat_list


def sub(xs: list[int], x: int, y: int) -> list[int]:
    assert x < y
    sub_list: list[int] = []
    if x < 0:
        x = 0
    if y > (len(xs)):
        y = (len(xs) - 1)
    if len(xs) == 0:
        return []
    while x < y:
        sub_list.append(xs[x])
        x += 1
    return sub_list