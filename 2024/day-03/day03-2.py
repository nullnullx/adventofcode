#!/usr/bin/env python3

"""
--- Day 3: Mull It Over ---
--- Part Two ---

As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. 
If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

    The do() instruction enables future mul instructions.
    The don't() instruction disables future mul instructions.

Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are 
disabled because there is a don't() instruction before them. The other mul instructions function normally, including 
the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?



Solution:
Use regular expression to find any valid mul, do() and don't() patterns.
Iterate over found patterns and turn summarization "on" and "off" when we come across do() and don't().
"""


import re
import sys
sys.path.append('..')
from aoc import load_input


def main() -> None:
    any_pattern = re.compile(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)')
    total_sum = 0
    add_to_sum = True
    for memory_dump in load_input():
        all_patterns = any_pattern.finditer(memory_dump)
        for pattern in all_patterns:
            if add_to_sum and pattern.group()[:4] == 'mul(':
               total_sum += int(pattern.group(1)) * int(pattern.group(2))
            elif pattern.group() == "do()":
               add_to_sum = True
            elif pattern.group() == "don't()":
               add_to_sum = False
    print(f"Total sum of all mul: {total_sum}")


if __name__ == "__main__":
    main()
