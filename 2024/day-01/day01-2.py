#!/usr/bin/env python3

"""
--- Part Two ---

Your analysis only confirmed what everyone feared: the two lists of location IDs are indeed very different.

Or are they?

The Historians can't agree on which group made the mistakes or how to read most of the Chief's handwriting, 
but in the commotion you notice an interesting detail: a lot of location IDs appear in both lists! 
Maybe the other numbers aren't location IDs at all but rather misinterpreted handwriting.

This time, you'll need to figure out exactly how often each number from the left list appears in the right list. 
Calculate a total similarity score by adding up each number in the left list after multiplying it by the number 
of times that number appears in the right list.

Here are the same example lists again:

3   4
4   3
2   5
1   3
3   9
3   3

For these example lists, here is the process of finding the similarity score:

    The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
    The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
    The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
    The fourth number, 1, also does not appear in the right list.
    The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
    The last number, 3, appears in the right list three times; the similarity score again increases by 9.

So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

Once again consider your left and right lists. What is their similarity score?


Solution:
Sort both columns.
Get the number from the left column - number_left.
Get sequence length of the same number in the left column - count_left.
Get sequence length of matching number in the right column - count_right. Or 0 if no matching number found.
Amount to add to the total sum for the current step is number_left * count_right * count_left.
Thus left and right columns are scanned only once and complexity is O(n) for this portion of code.
"""

import sys
sys.path.append('..')
from aoc import load_input

def main() -> None:
    locations_text = load_input()
    locations_left = sorted(map(lambda x: int(x.split()[0]), locations_text))
    locations_right = sorted(map(lambda x: int(x.split()[1]), locations_text))
    result = 0
    index_left = 0
    index_right = 0
    # Iterate over both columns until the end
    while index_left < len(locations_left) and index_right < len(locations_right):
        number_left = locations_left[index_left]
        count_left = 0
        # Count the same numbers in the sequence in the left column.
        while index_left < len(locations_left) and number_left == locations_left[index_left]:
            count_left += 1
            index_left += 1
        count_right = 0
        # Count the matching numbers in the sequence in the right column.
        while index_right < len(locations_right) and locations_right[index_right] <= number_left:
            if number_left == locations_right[index_right]:
                count_right += 1
            index_right += 1
        result += number_left * count_right * count_left

    print(result)

if __name__ == "__main__":
    main()
