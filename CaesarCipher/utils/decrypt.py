from algorithm.Algorithm import Algorithm


# TODO: Implement decrypting (Done)

def decrypt(decryptString: str, algorithm: Algorithm):
    stringOriginal = ""
    encryptedStripped = list(decryptString)
    key_list = list(algorithm.ciphering.keys())
    value_list = list(algorithm.ciphering.values())
    for i in encryptedStripped:
        position = key_list[value_list.index(i)]
        stringOriginal += position
    return stringOriginal
