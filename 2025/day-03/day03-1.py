#!/usr/bin/env python3

"""
--- Day 3: Lobby ---

You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. 
When you get to the main elevators, however, you discover that each one has a red light above it: they're all offline.
"Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. 
I'll try to get them online soon."
You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, 
not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also offline."
"But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."
There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled 
with their joltage rating, a value from 1 to 9. You make a note of their joltage ratings (your puzzle input). For example:
987654321111111
811111111111119
234234234234278
818181911112111

The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, 
you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries 
you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. 
(You cannot rearrange batteries.)
You'll need to find the largest possible joltage each bank can produce. In the above example:
    In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
    In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
    In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
    In 818181911112111, the largest joltage you can produce is 92.

The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.
There are many batteries in front of you. Find the maximum joltage possible from each bank; what is the total output joltage?


Solution:
We need to find the two largest digits in each bank of batteries.
First search for the largest digit in the bank (excluding the last digit), 
then search for the largest digit in the remaining part of the bank (after the index of the first largest digit).
"""

import sys

sys.path.append('..')
from aoc import load_input


def find_max_digit(int_str: str) -> tuple[int, int]:
    digits = list(map(int, int_str))
    max_digit = max_index = 0
    for digit_index, digit in enumerate(digits):
        if digit > max_digit:
            max_digit = digit
            max_index = digit_index
    return max_index, max_digit


def get_max_jolts(bank: str) -> int:
    int1_index, max_int1 = find_max_digit(bank[:-1])
    _, max_int2 = find_max_digit(bank[int1_index+1:])
    return max_int1 * 10 + max_int2


def main() -> None:
    battery_banks = load_input()
    total_joltage = sum(map(lambda bank: get_max_jolts(bank), battery_banks))
    print(total_joltage)


if __name__ == "__main__":
    main()
