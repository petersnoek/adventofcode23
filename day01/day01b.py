#!/usr/bin/env python3

import os
import sys
import re

# read input file into "lines"
input_file = os.path.join(sys.path[0], "example01b.txt")
# input_file = os.path.join(sys.path[0], "input01.txt")
with open(input_file) as f:
    lines = f.read().splitlines()

# als een van deze woorden 'one', 'two' gevonden is, hebben we het nummer nodig '1', '2'
replacements = {
    'one': '1',     'two': '2',     'three': '3',   'four': '4',    'five': '5',
    'six': '6',     'seven': '7',   'eight': '8',   'nine': '9',    'zero': '0',
}

total = 0
for line in lines:                      # eightwothree
    matches = []
    for x in range(len(line)):          # loop over alle karakters in de regel: 0, 1, 2, ... 11
        part = line[x:]                 # neem steeds een nieuw stukje tekst, 0:eightwothree,  1:ightwothree
        if part[0].isdigit():           # is het eerste teken een getal?
            matches.append(part[0])     # voeg het gevonden getal toe aan matches
        else:                           # het eerste teken is geen getal; is het een toegestaan woord?
            for item in replacements.keys():    # loop over alle toegestane "woorden": one, two
                if part.startswith(item):   # string begint met een woord
                    matches.append(replace_word_to_number[item])    # vervang "eight" door 8 en bewaar in matches

    first_digit = matches[0]    # eerste match
    last_digit = matches[-1]    # laatste match
    total = total + int(first_digit + last_digit)
    print(line, first_digit, last_digit, total)

print('---------------')
print('ANSWER: ', total)