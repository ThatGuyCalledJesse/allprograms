from create_data import create_data
from validate import *

# This program is used to catch cheaters based on math, not 100% accurate

# Create player data for 1000 players
data = create_data(1000)
validation = validate(data)
print(validation)