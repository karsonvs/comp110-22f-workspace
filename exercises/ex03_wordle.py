"""An attempt at a more familiar version of Wordle."""

__author__ = "730561113"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(full: str, char: str) -> bool:
    """Checks if string contains the character specified."""
    assert len(char) == 1
    i: int = 0
    while i < len(full):
        if (full[i] == char):
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Uses the contain_char function to assess what color boxes to use in the output."""
    assert len(guess) == len(secret)
    result: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX    
        i += 1
    return result


def input_guess(n: int) -> str:
    """Takes user input and checks if it is the proper number of characters."""
    user: str = input(f"Enter a {n} character word: ")
    while len(user) != n:
        user = input(f"That wasn't {n} chars! Try again: ")
    return user


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    guess: str = ""
    secret: str = "codes"
    while turn <= 6 and guess != secret:
        print(f"=== Turn {turn} out of 6 ===")
        guess = input_guess(5)
        print(emojified(guess, secret))
        turn += 1
    if guess == secret:
        print(f"You won in {turn + 1}/6 turns!")
    else:
        print("X/6 - Sorry try again tomorrow!")


if __name__ == "__main__":
    main()