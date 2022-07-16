import random
import os

def create_data(amountOfPlayers: int):
    results = []
    for i in range(5):
        results.append(random.choice(("Heads", "Tails")))

