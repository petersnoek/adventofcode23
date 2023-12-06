#!/usr/bin/env python3

import os
import sys
import re

# read input file into "lines"
# input_file = os.path.join(sys.path[0], "example01.txt")
input_file = os.path.join(sys.path[0], "input01.txt")
with open(input_file) as f:
    lines = f.read().splitlines()

replace = {
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

first_digit = 0
last_digit = 0
total = 0
for line in lines:
    replaced = line.translate(replace)
    f = re.search(r'\d', line).group(0)
    l = re.search(r'(\d)(?!.*\d)', line).group(0)
    number = int(f + l)
    total = total + number

print('---------------')
print('ANSWER: ', total)