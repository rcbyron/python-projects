""" A simulator for the monty hall problem """
import random

NUM_GAMES = 10000

correct = 0
for game_count in range(NUM_GAMES):
    # 0 = goat, 1 = car
    doors = [0, 0, 1]
    random.shuffle(doors)

    door_indices = [0, 1, 2]
    guess = random.choice(door_indices)  # pick a random door index

    host_reveal = random.choice([door_index for door_index, prize in enumerate(doors) if prize != 1 and door_index != guess])

    switch = random.choice([door_index for door_index in door_indices if door_index != guess and door_index != host_reveal])

    if doors[switch] is 1:
        correct += 1

print(str(correct*100 / (game_count+1))+"% correct")