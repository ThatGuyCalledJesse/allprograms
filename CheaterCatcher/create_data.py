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
        result = []
        for i in range(5):
            result.append(random.choice(("Heads", "Tails")))
        with open("data.txt", 'a') as file:
            file.write(f'Player {playerIndex}: {result} | {random.choice(("Cheater", "No Cheater"))}\n')
        all_results.append(result)
    return all_results
