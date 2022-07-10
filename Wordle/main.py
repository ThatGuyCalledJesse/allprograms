from words import words
import random

word = random.choice(words)
inputWord = input("Enter a 5-letter word: ")

# Checks if the word is 5 letters long
if len(inputWord) != 5:
    raise Exception("It has to be 5 letters")

