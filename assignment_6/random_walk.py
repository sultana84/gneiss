import random

def get_random_direction():
    direction = ""
    probability = random.random()

    if probability < 0.25:
        direction = "west"
    elif probability < 0.5:
        direction = "north"
    elif probability < 0.75:
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
    return displacements[dir_key] 

random_dir = get_random_direction()
displacement = get_direction_displacement(random_dir)

current_position = [0, 0]
current_position[0] = 

print(random_dir)
print(displacement)

def take_walk(steps):
    current_location = [0, 0]
    for step_index in range(steps):
        direction = get_random_direction()
