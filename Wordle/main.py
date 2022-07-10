from words import words
import random
from utils.valid import validate

# Gets a random word from the pool and makes a list out of it
word = random.choice(words)
wordList = list(word)

# Takes an input word from the user
inputWord = input("Enter a 5-letter word: ")

# Checks if the word is 5 letters long
validate(word)
