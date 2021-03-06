import random

def create_data(amountOfPlayers: int):
    # List that contains all results
    all_results = []

    # Clears the already existing file
    with open("data.txt", "w") as file:
        file.write("")

    # A loop that iterates through all the players
    for i in range(amountOfPlayers):
        playerIndex = i + 1
        isCheater = random.choice(("Cheater", "Not Cheater"))
        result = []
        if isCheater.lower() == "cheater":
            for i in range(5):
                result.append("Heads")
        else:
            for i in range(5):
                result.append(random.choice(("Heads", "Tails")))
        result.append(isCheater)
        with open("data.txt", 'a') as file:
            file.write(f'Player {playerIndex}: {result}\n')
        all_results.append(result)
    return all_results
