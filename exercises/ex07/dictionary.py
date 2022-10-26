"""Exercise to gain a better understanding of dictionaries."""


__author__ = "730561113"


def invert(xs: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary and returns a dictionary that shows the keys and values swapped."""
    ys = dict()
    for key in xs:
        if xs[key] in ys:
            raise KeyError("KeyError")
        else:
            ys[xs[key]] = key
    return ys


def favorite_color(xs: dict[str, str]) -> str:
    """Takes a dictionary with colors and tells which color is listed the most."""
    favorite: str = ""
    store: dict[str, int] = {}
    count: int = 0
    for i in xs:
        if xs[i] in store:
            store[xs[i]] += 1
        elif xs[i] not in store:
            store[xs[i]] = 1
        if store[xs[i]] > count:
            favorite = xs[i] 
            count = store[xs[i]]
    return favorite 


def count(xs: list[str]) -> dict[str, int]:
    """Takes a list and returns a dictionary that includes the number of times each word appears in the list."""
    result: dict[str, int] = {}
    for i in range(len(xs)):
        if xs[i] in result:
            result[xs[i]] += 1
        else:
            result[xs[i]] = 1
    return result
