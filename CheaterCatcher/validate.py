# A function that checks if the player

def validate(data: list):
    playerIndex = 0
    amountFlagged = 0
    for i in data:
        playerIndex += 1
        if i[0] == i[1] and i[1] == i[2] and i[2] == i[3] and i[3] == i[4] and i[4] == "Heads":
            print(f"Player {playerIndex} is probably a cheater and returned positive from the test!")
            amountFlagged += 1