from allprograms.CaesarCipher.algorithm.algorithms import *

def useAlgorithm(input: str):
    input = input.lower()
    inputStripped = list(input)
    number = ""
    for i in inputStripped:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            number += i
        else:
            continue
    number = int(number)
    number -= 1
    return RotList[number]
