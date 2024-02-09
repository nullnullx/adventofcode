#!/usr/bin/env python3

"""
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take 
you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. 
"Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while 
before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, 
but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, 
it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. 
There are lots of numbers and symbols you don't really understand, but apparently any number 
adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. 
(Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 
114 (top right) and 58 (middle right). 
Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. 
What is the sum of all of the part numbers in the engine schematic?

Solution:
Use regex to find numbers, their start and end position in the input.
Build the string of all characters surrounding the number including diagonals.
Use set comparison to check if the string of characters contains any special symbols.

Used references:
https://pynative.com/python-find-position-of-regex-match-using-span-start-end/
"""

import sys
import re


def load_input() -> list[str]:
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as fh:
            return fh.read().splitlines()
    return sys.stdin.read().splitlines()

def get_part_number(engine_schematic: list[str]) -> int:
    non_symbols = set('0123456789.')
    for line_number, line_text in enumerate(engine_schematic):
        for number in re.finditer(r'\d+', line_text):
            start_position = number.start()
            end_position = number.end()   # index after the matching character
            surrounding_characters = ""
            # print(f"Line: {line_text}\n Start position: {start_position} End position: {end_position}")
            # collect character on the left
            if start_position > 0:
                start_position -= 1
                surrounding_characters += line_text[start_position]
            # collect character on the right
            if end_position < len(line_text):
                surrounding_characters += line_text[end_position]
            # collect characters above
            if line_number > 0:
                surrounding_characters += engine_schematic[line_number-1][start_position:end_position+1]  # End index over the limit is Ok
            # collect characters below
            if line_number < len(engine_schematic)-1:
                surrounding_characters += engine_schematic[line_number+1][start_position:end_position+1]  # End index over the limit is Ok
            # check if any collected character is a symbol
            if not set(surrounding_characters).issubset(non_symbols):
                yield int(number.group())
            

sum_of_parts = 0
engine_schematic = load_input()
for part_number in get_part_number(engine_schematic):
    # print(f"Part: {part_number}")
    sum_of_parts += part_number
print(sum_of_parts)
