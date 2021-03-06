from allprograms.official_build.CaesarCipher.algorithm.algorithms import *
from utils.encrypt import encrypt
from utils.decrypt import decrypt
from utils.useAlgorithm import useAlgorithm

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

path = "output.txt"

# Driver code
if __name__ == "__main__":
    # Clears the "output.txt" file
    with open(path, "w") as file:
        file.write("")

    # Asks if the user wants to encrypt a string or decrypt a string
    activity = input("Do you want to encrypt a string? Or do you want to decrypt a string?\n")

    # An "If Statement" that gives the code respective to the user's choice
    if activity.lower() == "encrypt":
        # The things that happen when the user enters "encrypt"
        encryptString = input("What string do you want to encrypt?\n")
        encrypted = encrypt(encryptString, chooseAlgorithm())
        print(encrypted)
        with open(path, "a") as file:
            file.write(f"\nEncrypted string: {encrypted}")
        print("For your conveniences, the output is also written to a file called output.txt")
    elif activity.lower() == "decrypt":
        # The things that happen when the user enters "decrypt"
        decryptString = input("What string do you want to decrypt?\n")
        decryptAlgorithm = input("With what algorithm what that string encrypted?\n").lower()
        print(decrypt(decryptString, useAlgorithm(decryptAlgorithm)))
    else:
        # An error gets raised when the user doesn't enter a valid option
        raise Exception("That is not a valid option! Please try again")