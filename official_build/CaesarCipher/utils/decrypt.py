from allprograms.official_build.CaesarCipher.algorithm.Algorithm import Algorithm

# This function decrypts the given string
def decrypt(decryptString: str, algorithm: Algorithm):
    stringOriginal = ""
    encryptedStripped = list(decryptString)
    key_list = list(algorithm.ciphering.keys())
    value_list = list(algorithm.ciphering.values())
    for i in encryptedStripped:
        position = key_list[value_list.index(i)]
        stringOriginal += position
    return stringOriginal

