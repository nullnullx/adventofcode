#!/usr/bin/env python3

"""
--- Part Two ---

Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, 
it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start 
of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13

This line describes two ranges of seed numbers to be planted in the garden. 
The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. 
The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, 
which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, 
and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. 
What is the lowest location number that corresponds to any of the initial seed numbers?


Solution:
Parse almanac data into dict with all numbers for each category. Dict key represents a category and value
is the list with all mapping numbers for the category.
Walk all possible combinations of the seed number to the location number and identify the minimal location number.
Algorithm relies on dict key order preservation in Python.
"""

import json
import aoc


def parse_almanac(almanac_text: str) -> tuple[list[int], dict[list[list[int]]]]:
    """Assemble almanac data into dict where key is a map name and value is a list 
    of lists with source and destination numbers.
    Relying on key order preservation in dict.

    Args:
        almanac_text (str): almanac as a list of strings

    Returns:
        tuple[list, dict]: list of seed numbers and almanac data in dict format.
    """
    
    seeds = almanac_text[0].split(':')[1]
    seeds = list(map(int, seeds.split()))
    almanac_data = {}
    for almanac_line in [s.strip() for s in almanac_text[1:]]:
        if almanac_line:
            if almanac_line[0].isalpha():
                almanac_key = almanac_line.rstrip(':')
                almanac_data[almanac_key] = []
            else:
                almanac_numbers = list(map(int, almanac_line.split()))
                almanac_data[almanac_key].append(almanac_numbers)
    return seeds, almanac_data

def find_location(map_source: int, almanac_data: dict[list[list[int]]]) -> int:
    for one_map in almanac_data.values():
        for one_line in one_map:
            if one_line[1] <= map_source < one_line[1] + one_line[2]:
                map_source = one_line[0] + map_source - one_line[1]
                break
    return map_source

def main():
    almanac_text = aoc.load_input()
    seeds, almanac_data = parse_almanac(almanac_text)
    # print(seeds)
    # print(json.dumps(almanac_data, indent=4))
    locations = []
    for seed_number, seed_range in zip(seeds[0::2], seeds[1::2]):
        for seed in range(seed_number, seed_number + seed_range):
            locations.append(find_location(seed, almanac_data))
    print(min(locations))


if __name__ == "__main__":
    main()
