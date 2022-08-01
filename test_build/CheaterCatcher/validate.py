# A function that checks if the player has 5 heads in a row, if so, the player gets marked as a cheater
def validate(data: list):
    false_positives = []
    indexFalsePositive = 0
    playerIndex = 0
    amountFlagged = 0
    for i in data:
        playerIndex += 1
        if i[0] == i[1] and i[1] == i[2] and i[2] == i[3] and i[3] == i[4] and i[4] == "Heads":
            if i[5] == "Not Cheater":
                false_positives.append(f"Player {(indexFalsePositive + 1)}")
            indexFalsePositive += 1
            print(f"Player {playerIndex} flagged the test!")
            validation_2 = validate_2(data)
            amountFlagged += 1
    return f"""
{amountFlagged} players flagged the test!
The actual amount of cheaters is {validation_2}
That means that the amount of false positives is {(amountFlagged - validation_2)}
False positives:
{false_positives}"""

# A function that checks if the results are false positive, or true positive
def validate_2(data: list):
    actualAmount = 0
    for i in data:
        if i[5] == "Cheater":
            actualAmount += 1
    return actualAmount