#!/usr/bin/env python3

"""
--- Part Two ---

The clerk quickly discovers that there are still invalid IDs in the ranges in your list. 
Maybe the young Elf was doing other silly patterns as well?
Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. 
So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and
1111111 (1 seven times) are all invalid IDs.
From the same example as before:
    11-22 still has two invalid IDs, 11 and 22.
    95-115 now has two invalid IDs, 99 and 111.
    998-1012 now has two invalid IDs, 999 and 1010.
    1188511880-1188511890 still has one invalid ID, 1188511885.
    222220-222224 still has one invalid ID, 222222.
    1698522-1698528 still contains no invalid IDs.
    446443-446449 still has one invalid ID, 446446.
    38593856-38593862 still has one invalid ID, 38593859.
    565653-565659 now has one invalid ID, 565656.
    824824821-824824827 now has one invalid ID, 824824824.
    2121212118-2121212124 now has one invalid ID, 2121212121.

Adding up all the invalid IDs in this example produces 4174379265.
What do you get if you add up all of the invalid IDs using these new rules?



Solution:
We will need to check repeated sequences of varying lengths. Maximum sequence length is half the number of digits in the ID.
Break out of loop when a non-matching sequence is found.
Skip checking for the sequence length if the ID length is not a multiple of the sequence length.
Use generator to yield invalid IDs within each range to avoid storing them all in memory.
"""

import sys
from typing import Generator

sys.path.append('..')
from aoc import load_input


def is_invalid_id(product_id: int) -> bool:
    str_id = str(product_id)
    length = len(str_id)
    # Check only sequences up to half the length
    for sequence_len in range(1, length // 2 + 1):
        # Skip if length is not multiple of sequence_len
        if length % sequence_len != 0:
            continue
        str_match = str_id[0:sequence_len]
        for i in range(sequence_len, length, sequence_len):
            # Break if any sequence does not match
            if str_id[i:i + sequence_len] != str_match:
                break
        else:
            return True
    return False


def get_invalid_ids(id_range: str) -> Generator[int, None, None]:
    start_str, end_str = id_range.split('-')
    first_id, last_id = int(start_str), int(end_str)
    for current_id in range(first_id, last_id + 1):
        if is_invalid_id(current_id):
            yield current_id


def main() -> None:
    id_ranges = load_input()
    invalid_id_sum = sum(map(lambda id_range: sum(get_invalid_ids(id_range)), id_ranges[0].split(',')))
    print(invalid_id_sum)


if __name__ == "__main__":
    main()
