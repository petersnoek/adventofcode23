#!/usr/bin/env python3

import os
import sys
import re

# read input file into "lines"
# input_file = os.path.join(sys.path[0], "example01.txt")
input_file = os.path.join(sys.path[0], "input01.txt")
with open(input_file) as f:
    lines = f.read().splitlines()

line_counter = 1
first_digit = 0
last_digit = 0
total = 0
for line in lines:
    f = re.search(r'\d', line).group(0)
    l = re.search(r'(\d)(?!.*\d)', line).group(0)
    number = int(f + l)
    total = total + number
    print("Line: ", line_counter, ": ", line, f, l, number, total)
    line_counter = line_counter + 1

print('---------------')
print('ANSWER: ', total)