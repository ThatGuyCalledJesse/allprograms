from allprograms.CaesarCipher.algorithm.algorithms import *

# This function links the input string to the corresponding algorithm
def useAlgorithm(input: str):
    input = input.lower()
    inputStripped = list(input)
    number = ""
    if 'rot' not in input:
        raise Exception("That is not a valid algorithm")

    if input != "":
        if input.startswith("rot"):
            for i in inputStripped:
                if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    number += i
                else:
                    continue
            number = int(number)
            if number > 25:
                raise Exception("Woah! The algorithms don't go that high")
            number -= 1
            return RotList[number]
        else:
            raise Exception("Make sure the algorithm name starts with \"rot\"!")
    else:
        raise Exception("You have to enter an algorithm, it cannot be empty")
