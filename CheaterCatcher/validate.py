# A function that checks if the player has 5 heads in a row, if so, the player gets marked as a cheater
def validate(data: list):
    playerIndex = 0
    amountFlagged = 0
    for i in data:
        playerIndex += 1
        if i[0] == i[1] and i[1] == i[2] and i[2] == i[3] and i[3] == i[4] and i[4] == "Heads":
            print(f"Player {playerIndex} flagged the test!")
            validation_2 = validate_2(data)
            amountFlagged += 1
    print(validation_2)
    return f"{amountFlagged} players flagged the test!"

# A function that checks if the results are false positive, or true positive
def validate_2(data: list):
    actualAmount = 0
    for i in data:
        if i[5] == "Cheater":
            actualAmount += 1
    return f"The actual amount of cheaters is {actualAmount}"