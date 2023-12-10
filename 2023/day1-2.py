#!/usr/bin/env python3

"""
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out 
with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. 
For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. 
Adding these together produces 281.

What is the sum of all of the calibration values?

Solution:
Build the dictionary of valid numerical and spelled out digits with their proper integer values.
Search numerical or spelled out digits in the input.
"""

import sys

valid_digits = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def find_digit(substring: str) -> list[int]:
    for digit_as_string in valid_digits:
        if substring.startswith(digit_as_string):
            return [valid_digits[digit_as_string]]
    return []

calibration_values_sum = 0
for line in sys.stdin:
    all_digits = []
    for substring in [line[i:] for i in range(len(line)-1)]:
        # print(f"String: {substring}"
        #       f"Digit: {find_digit(substring)}\n")
        all_digits.extend(find_digit(substring))
    calibration_value = all_digits[0] * 10 + all_digits[-1]
    # print(calibration_value)
    calibration_values_sum += calibration_value
print(calibration_values_sum)
