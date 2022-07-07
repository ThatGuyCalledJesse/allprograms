from allprograms.CaesarCipher.algorithm.algorithms import *
from utils.encrypt import encrypt
from allprograms.utils import *

# TODO: Write the program that actually encrypts and decrypts a string (Done)
# TODO: Add a menu that lets the user choose between encrypting and decrypting (In Progress)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

path = "output.txt"

# Driver code
if __name__ == "__main__":
    # Clears the "output.txt" file
    clearFile(path)

    # Asks if the user wants to encrypt a string or decrypt a string
    activity = input("Do you want to encrypt a string? Or do you want to decrypt a string?\n")

    # An "If Statement" that gives the code respective to the user's choice
    if activity.lower() == "encrypt":
        encryptString = input("What string do you want to encrypt?\n")
        encrypted = encrypt(encryptString, chooseAlgorithm())
        print(encrypted)
        with open(path, "a") as file:
            file.write(f"\nEncrypted string: {encrypted}")
        print("For your conveniences, the output is also written to a file called output.txt")
    elif activity.lower() == "decrypt":
        decryptString = input("")
