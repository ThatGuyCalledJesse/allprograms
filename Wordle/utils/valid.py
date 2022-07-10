# Checks if the word the user submitted is 5 characters
def validate(word: str):
    if len(word) != 5:
        # An error gets raised if the word is not 5 characters long
        raise Exception("That word is not 5 letters long!")