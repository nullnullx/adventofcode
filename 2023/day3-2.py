#!/usr/bin/env python3

"""
--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine springs to life, 
you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, 
the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, 
holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. 
You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol 
that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out 
which gear needs to be replaced.

Consider the same engine schematic again:

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

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, 
so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. 
(The * adjacent to 617 is not a gear because it is only adjacent to one part number.) 
Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

Solution:
Build a dict with potential gear (*) position as a key and list of connected part numbers.
If list is only two part numbers then * is a actual gear and should be counted.
"""

import sys
import re


def load_input() -> list[str]:
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as fh:
            return fh.read().splitlines()
    return sys.stdin.read().splitlines()

def get_all_gears(engine_schematic: list[str]) -> int:
    gear_locations = {}
    for line_number, line_text in enumerate(engine_schematic):
        for number in re.finditer(r'\d+', line_text):
            start_position = number.start()
            end_position = number.end()   # index after the matching character
            # collect character on the left
            if start_position > 0:
                start_position -= 1
                if line_text[start_position] == '*':
                    update_gear_key(gear_locations, (line_number, start_position), number.group())
            # collect character on the right
            if end_position < len(line_text):
                if line_text[end_position] == '*':
                    update_gear_key(gear_locations, (line_number, end_position), number.group())
            # collect characters above
            if line_number > 0:
                surrounding_characters = engine_schematic[line_number-1][start_position:end_position+1]
                # find all potential gears in the string
                for gear in re.finditer(r'\*', surrounding_characters):
                    gear_position = start_position + gear.start()
                    update_gear_key(gear_locations, (line_number-1, gear_position), number.group())
            # collect characters below
            if line_number < len(engine_schematic)-1:
                surrounding_characters = engine_schematic[line_number+1][start_position:end_position+1]
                # find all potential gears in the string
                for gear in re.finditer(r'\*', surrounding_characters):
                    gear_position = start_position + gear.start()
                    update_gear_key(gear_locations, (line_number+1, gear_position), number.group())
    return gear_locations

def update_gear_key(gear_locations: dict, gear_key: tuple, part_number: str) -> None:
    """Add or update gear key in gear_locations argument.

    Args:
        gear_locations (dict): dictionary with all gears
        gear_key (tuple): gear key (coordinate) to be added or updated
        part_number (str): part number to associate with a gear

    Returns:
        None
    """
    gear_locations[gear_key] = gear_locations.get(gear_key, []) + [int(part_number)]

engine_schematic = load_input()
all_gears = get_all_gears(engine_schematic)
# Find gears connected to only two part numbers. Multiply those part numbers and sum up all together.
sum_of_parts = sum([part[0] * part[1] for part in all_gears.values() if len(part)==2])
print(sum_of_parts)
