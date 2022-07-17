# A function that checks if the player

def validate(data: list):
    playerIndex = 0
    for i in data:
        playerIndex += 1
        if data[0] == data[1] and data[1] == data[2] and data[2] == data[3] and data[3] == data[4] and data[4] == data[5] and data[5] == "heads".lower():
            print(f"Player {playerIndex} is probably a cheater and returned positive from the test!")