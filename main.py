from time import sleep
import random
import os
from argparser import get_params

clear_command = 'cls' if os.name == 'nt' else 'clear'
global_params = get_params()

HEIGHT = global_params.height
WIDTH = global_params.width
MAX_ITERS = global_params.iters
FISH = global_params.fish
SHRIMP = global_params.shrimp
ROCK = global_params.rock
EMPTY = global_params.empty

def show_field():
    os.system(clear_command)
    for line in field: print(''.join(line))

def get_neighbors():
    if y == 0:
        if x == 0:
            neighbors = [field[y][x+1], field[y+1][x], field[y+1][x+1]]
        elif x == WIDTH - 1:
            neighbors = [field[y][x-1], field[y+1][x], field[y+1][x-1]]
        else:
            neighbors = [field[y][x-1], field[y][x+1], field[y+1][x-1], 
                         field[y+1][x], field[y+1][x+1]]
    elif y == HEIGHT - 1:
        if x == 0:
            neighbors = [field[y][x+1], field[y-1][x], field[y-1][x+1]]
        elif x == WIDTH - 1:
            neighbors = [field[y][x-1], field[y-1][x], field[y-1][x-1]]
        else:
            neighbors = [field[y][x-1], field[y][x+1], field[y-1][x-1], 
                         field[y-1][x], field[y-1][x+1]]
    else:
        if x == 0:
            neighbors = [field[y][x+1], field[y-1][x], field[y-1][x+1], 
                         field[y+1][x], field[y+1][x+1]]
        elif x == WIDTH - 1:
            neighbors = [field[y][x-1], field[y-1][x], field[y-1][x-1], 
                         field[y+1][x], field[y+1][x-1]]
        else:
            neighbors = [field[y][x-1], field[y][x+1], field[y-1][x-1], 
                         field[y-1][x], field[y-1][x+1], field[y+1][x-1], 
                         field[y+1][x], field[y+1][x+1]]
    return neighbors

field = [[random.choice([FISH, SHRIMP, ROCK, EMPTY]) for j in range(WIDTH)] for i in range(HEIGHT)]
iters = 0

while True:
    iters += 1
    show_field()
    new_field = [[0 for j in range(WIDTH)] for i in range(HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            cur_cell = field[y][x]

            if cur_cell != ROCK:
                neighbors = get_neighbors()
                if cur_cell == EMPTY:
                    if neighbors.count(FISH) == 3:
                        new_field[y][x] = FISH
                    elif neighbors.count(SHRIMP) == 3:
                        new_field[y][x] = SHRIMP
                    else:
                        new_field[y][x] = EMPTY
                else:
                    if 1 < neighbors.count(cur_cell) < 4:
                        new_field[y][x] = cur_cell
                    else: 
                        new_field[y][x] = EMPTY
            else:
                new_field[y][x] = ROCK

    if field == new_field:
        break
    if iters == MAX_ITERS:
        break

    field = new_field
    sleep(1)
    
input()