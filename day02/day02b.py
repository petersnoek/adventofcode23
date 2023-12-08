#!/usr/bin/env python3

import os
import sys
import re

# max
maximums = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

# read input file into "lines"
# input_file = os.path.join(sys.path[0], "example02.txt")
input_file = os.path.join(sys.path[0], "input02.txt")
with open(input_file) as f:
    lines = f.read().splitlines()

total = 0
for line in lines:                          # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    game_minimums = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    sets = line.split(':')[1].split(';')    #         ---------------------- -----------------------

    for set_text in sets:
        set_parts = set_text.split(',')
        for part in set_parts:
            part = part[1:]
            amount = int(part.split(' ')[0])
            for min in game_minimums.keys():         # 'red', 'blue', 'green'
                if (part.endswith(min)):
                    if amount > int(game_minimums[min]):
                        game_minimums[min] = amount
    power = game_minimums['red'] * game_minimums['green'] * game_minimums['blue']
    total = total + power
    print(f"Line {line}  -- min(r,g,b)=({game_minimums['red']},{game_minimums['green']},{game_minimums['blue']}), power={power}")

print("============")
print(total)