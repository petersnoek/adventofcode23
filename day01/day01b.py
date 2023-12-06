#!/usr/bin/env python3

import os
import sys
import re

# read input file into "lines"
# input_file = os.path.join(sys.path[0], "example01b.txt")
input_file = os.path.join(sys.path[0], "input01.txt")
with open(input_file) as f:
    lines = f.read().splitlines()

valid_items = [
    'one', '1',
    'two', '2',
    'three', '3',
    'four', '4',
    'five', '5',
    'six', '6',
    'seven', '7',
    'eight', '8',
    'nine', '9',
    'zero', '0',
]

replace_word_to_number = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0',
}

total = 0
for line in lines:      # eightwothree
    matches = []
    for x in range(len(line)):    # loop over alle karakters in de regel: 0, 1, 2, ... 11
        part = line[x:]    # neem steeds een nieuw stukje tekst, 0:eightwothree,  1:ightwothree

        for item in valid_items:    # one, 1, two, 2
            if part.startswith(item):
                if item in replace_word_to_number:  # moet 't vervangen worden?
                    matches.append(replace_word_to_number[item])
                else:       # het is al een getal (0, 1, 2)
                    matches.append(item)
        # print(line, part, matches)

    first_digit = matches[0]
    last_digit = matches[-1]

    total = total + int(first_digit + last_digit)

    print(line, first_digit, last_digit, total)

print('---------------')
print('ANSWER: ', total)