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
    game_number = int(line.split(':')[0][5:])      # ------
    sets = line.split(':')[1].split(';')    #         ---------------------- -----------------------
    sets_has_errors = 0
    for set_text in sets:
        set_parts = set_text.split(',')
        for part in set_parts:
            part = part[1:]
            amount = int(part.split(' ')[0])
            for max in maximums.keys():         # 'red', 'blue', 'green'

                if (part.endswith(max)):
                    if (amount > int(maximums[max])):
                        sets_has_errors = sets_has_errors + 1
                        break
    if(sets_has_errors == 0): total = total + game_number

print("============")
print(total)