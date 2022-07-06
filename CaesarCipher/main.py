from allprograms.CaesarCipher.algorithm.algorithms import *
from utils.encrypt import encrypt

# TODO: Write the program that actually encrypts and decrypts a string (Done)
# TODO: Add a menu that lets the user choose between encrypting and decrypting (In Progress)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

characterIndex1 = 0
for letter in alphabet:
    characterIndex2 = characterIndex1 + 10
    print(f"\"{alphabet[characterIndex1]}\": \"{alphabet[characterIndex2]}\",")
    characterIndex1 += 1

# Driver code
if __name__ == "__main__":
    encryptString = input("What string do you want to encrypt? Write down the algorithm, or else you can't decrypt it!\n")
    encrypted = encrypt(encryptString, chooseAlgorithm())
    print(encrypted)
    with open("output.txt", "a") as file:
        file.write(f"\nEncrypted string: {encrypted}")
    print("For your conveniences, the output is also written to a file called output.txt")