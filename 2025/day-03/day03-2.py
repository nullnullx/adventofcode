#!/usr/bin/env python3

"""
--- Part Two ---

The escalator doesn't move. The Elf explains that it probably needs more joltage to overcome the static friction of the system 
and hits the big red "joltage limit safety override" button. You lose count of the number of times she needs to confirm "yes, 
I'm sure" and decorate the lobby a bit while you wait.
Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.
The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference 
is that now there will be 12 digits in each bank's joltage output instead of two.
Consider again the example from before:
987654321111111
811111111111119
234234234234278
818181911112111

Now, the joltages are much larger:
    In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
    In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
    In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
    In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.

The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.
What is the new total output joltage?



Solution:
We will need to find the twelve largest digits in each bank of batteries.
Start with the full bank, find the largest digit within the range that allows for enough remaining digits to reach twelve total.
Then, recursively find the next largest digit in the remaining part of the bank, until twelve digits have been selected.
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


def get_max_jolts(bank: str, batteries_to_use: int) -> int:
    batteries_left = len(bank)
    if batteries_to_use == 0:
        return 0
    if batteries_left > batteries_to_use:
        max_index, max_digit = find_max_digit(bank[:batteries_left-batteries_to_use+1])
        return  max_digit * 10 ** (batteries_to_use - 1) + get_max_jolts(bank[max_index+1:], batteries_to_use - 1)
    else:
        return int(bank)


def main() -> None:
    battery_banks = load_input()
    total_joltage = sum(map(lambda bank: get_max_jolts(bank, 12), battery_banks))
    print(total_joltage)


if __name__ == "__main__":
    main()
