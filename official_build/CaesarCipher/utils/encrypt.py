from allprograms.official_build.CaesarCipher.algorithm.Algorithm import *

# This function encrypts the given string
def encrypt(encryptString: str, algorithm: Algorithm):
    try:
        stringEncrypted = ""
        wordStripped = list(encryptString)
        for i in wordStripped:
            encryptedCharacter = algorithm.ciphering[i]
            stringEncrypted += encryptedCharacter
        return stringEncrypted
    except AttributeError:
        print("That is the required type! Please try again.")