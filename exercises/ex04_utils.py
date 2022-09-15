"""Practice using lists."""

__author__: str = "730561113"

def all(nums: list[int], n: int) -> bool :
    """Checks if all the numbers in a list of ints are the same as the other int provided."""
    i: int = 0
    while i < len(nums):
        if nums[i] != n:
            return False
        i += 1
    return True


def max(nums: list[int]) -> int:
    """Finds the max value in a list of ints."""
    max: int = 0
    i: int = 0
    if len(nums) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(nums):
        if nums[i] > max:
            max = nums[i]
        i += 1
    return max


def is_equal(input: list[int], input2: list[int]) -> bool:
    """Determines whether two lists contain the same values in the exact same order."""
    assert len(input) == len(input2)
    i: int = 0
    while i < len(input):
        if input[i] != input2[i]:
            return False
        i += 1
    return True