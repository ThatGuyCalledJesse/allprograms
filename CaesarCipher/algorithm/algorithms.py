from algorithm.Algorithm import Algorithm
import random

# Rot: Rotations
# The number defines what type of rotation it is (Rot1 = A : B, Rot3 = A: D)

# TODO: Add more algorithms and implement them (In Progress)

Rot1 = Algorithm(1, {"a": "b",
                     "b": "c",
                     "c": "d",
                     "d": "e",
                     "e": "f",
                     "f": "g",
                     "g": "h",
                     "h": "i",
                     "i": "j",
                     "j": "k",
                     "k": "l",
                     "l": "m",
                     "m": "n",
                     "n": "o",
                     "o": "p",
                     "p": "q",
                     "q": "r",
                     "r": "s",
                     "s": "t",
                     "t": "u",
                     "u": "v",
                     "v": "w",
                     "w": "x",
                     "x": "y",
                     "y": "z",
                     "z": "a",
                     " ": " "}, "Rot1")

Rot2 = Algorithm(2, {"a": "c",
                     "b": "d",
                     "c": "e",
                     "d": "f",
                     "e": "g",
                     "f": "h",
                     "g": "i",
                     "h": "j",
                     "i": "k",
                     "j": "l",
                     "k": "m",
                     "l": "n",
                     "m": "o",
                     "n": "p",
                     "o": "q",
                     "p": "r",
                     "q": "s",
                     "r": "t",
                     "s": "u",
                     "t": "v",
                     "u": "w",
                     "v": "x",
                     "w": "y",
                     "x": "z",
                     "y": "a",
                     "z": "b",
                     " ": " "}, "Rot2")

Rot3 = Algorithm(3, {"a": "d",
                     "b": "e",
                     "c": "f",
                     "d": "g",
                     "e": "h",
                     "f": "i",
                     "g": "j",
                     "h": "k",
                     "i": "l",
                     "j": "m",
                     "k": "n",
                     "l": "o",
                     "m": "p",
                     "n": "q",
                     "o": "r",
                     "p": "s",
                     "q": "t",
                     "r": "u",
                     "s": "v",
                     "t": "w",
                     "u": "x",
                     "v": "y",
                     "w": "z",
                     "x": "a",
                     "y": "b",
                     "z": "c", }, "Rot3")

Rot4 = Algorithm(4, {"a": "e",
                     "b": "f",
                     "c": "g",
                     "d": "h",
                     "e": "i",
                     "f": "j",
                     "g": "k",
                     "h": "l",
                     "i": "m",
                     "j": "n",
                     "k": "o",
                     "l": "p",
                     "m": "q",
                     "n": "r",
                     "o": "s",
                     "p": "t",
                     "q": "u",
                     "r": "v",
                     "s": "w",
                     "t": "x",
                     "u": "y",
                     "v": "z",
                     "w": "a",
                     "x": "b",
                     "y": "c",
                     "z": "d", }, "Rot4")

Rot5 = Algorithm(5, {"a": "f",
                     "b": "g",
                     "c": "h",
                     "d": "i",
                     "e": "j",
                     "f": "k",
                     "g": "l",
                     "h": "m",
                     "i": "n",
                     "j": "o",
                     "k": "p",
                     "l": "q",
                     "m": "r",
                     "n": "s",
                     "o": "t",
                     "p": "u",
                     "q": "v",
                     "r": "w",
                     "s": "x",
                     "t": "y",
                     "u": "z",
                     "v": "a",
                     "w": "b",
                     "x": "c",
                     "y": "d",
                     "z": "e", }, "Rot5")

Rot6 = Algorithm(6, {}, "Rot6")

RotList = [Rot1, Rot2, Rot3, Rot4, Rot5, Rot6]

def chooseAlgorithm():
    with open("../output.txt", "w") as file:
        file.write("")
    randomAlgorithm = random.choice(RotList)
    print(f"The chosen algorithm is {randomAlgorithm.name}! Write that down!")
    with open("../output.txt", "w") as file:
        file.write(f"Algorithm: {randomAlgorithm.name}")
    return randomAlgorithm