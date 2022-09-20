"""An example of a list utility algorithm."""

# Function with two parameters
# needle - what we're searching for
# haystack - what we're searching through
# Return Type: bool
def contains(needle: str, haystack: list[str]) -> bool:
    # Start from first index
    i: int = 0
    # Loop through each index of list
    while i < len(haystack):
        if needle == haystack[i]:
            return True
        i +=1
    # Test if equal to needle 
    #      Yes! return True
    return False