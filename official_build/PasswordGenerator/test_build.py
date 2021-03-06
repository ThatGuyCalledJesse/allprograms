import random
import os
from test_build_variables import *

possibleCharacters = ['a', 'b', 'c', 'd', 'e',
                      'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o',
                      'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y',
                      'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
specials = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
capitals = []
password = ""
config = ""
numbersEnabled = 'no'
specialsEnabled = 'no'
capitalsEnabled = 'no'

for character in possibleCharacters:
    character = character.upper()
    capitals.append(character)

with open("config.txt", "r") as file:
    config = file.read()

load_config_choice = input("Would you wish to load settings from config file?")

if load_config_choice != 'yes' and load_config_choice != 'no':
    raise Exception("Please enter yes or no")

if load_config_choice == 'yes':
    if numbers_test_build in config:
        possibleCharacters.append(numbers)
else:
    capitalsEnabled = input("Do you want to enable uppercase letters? [YES] [NO]\n>")
    numbersEnabled = input("Do you want to enable numbers? [YES] [NO]\n>")
    specialsEnabled = input("Do you want to enable special characters? [YES] [NO]\n>")

while True:
    try:
        passLength = input("How long should the password be?")
        if numbersEnabled.lower() == "yes":
            for number in numbers:
                possibleCharacters.append(number)
        if specialsEnabled.lower() == "yes":
            for special in specials:
                possibleCharacters.append(special)
        if capitalsEnabled.lower() == "yes":
            for capital in capitals:
                possibleCharacters.append(capital)
        passLength = int(passLength)
        generatedPassLength = 0

        while generatedPassLength < passLength:
            character = random.choice(possibleCharacters)
            password = password + character
            generatedPassLength += 1

        os.system("cls")
        print(password)
        input("Press enter to quit...")
        exit()
    except ValueError:
        print("This is not a valid number! Please try again")
