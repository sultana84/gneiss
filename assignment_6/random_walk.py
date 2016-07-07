import random

def get_random_direction():
    direction = ""
    probability = random.random()

    if probability < 0.5:
        direction = "west"

    elif probability > 0.5:
        direction = "north"

    elif probability = 0.5:
        direction = "south"

    else:
        direction = "east"

    return direction

def get_direction_displacement(dir_key):
    displacements = {
        'west': (-1, 0),
        'east': (1, 0),
        'north': (0, 1),
        'south': (0, -1)
        }

