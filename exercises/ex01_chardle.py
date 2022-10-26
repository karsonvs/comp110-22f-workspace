"""EX01 - Chardle - A cute step toward Wordle"""

__author__ = "730561113"
word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
char: str = input("Enter a single character: ")
if len(char) != 1:
    print("Error: Character must be a single character.")
    exit()
char_count: int = 0
print("Searching for " + char + " in hello")
if word[0] == char:
    print(char + " found at index 0.")
    char_count = char_count + 1
if word[1] == char:
    print(char + " found at index 1.")
    char_count = char_count + 1
if word[2] == char:
    print(char + " found at index 2.")
    char_count = char_count + 1
if word[3] == char:
    print(char + " found at index 3.")
    char_count = char_count + 1
if word[4] == char:
    print(char + " found at index 4.")
    char_count = char_count + 1
if char_count != 0:
    print(char_count + " instances of " + char + " found in " + word)
else:
    print("No instances of " + char + " found in " + word)

