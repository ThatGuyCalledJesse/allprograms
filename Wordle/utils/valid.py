# Checks if the word the user submitted is 5 letters
def validate(word: str):
    if len(word) != 5:
        raise Exception("That word is not 5 letters long!")