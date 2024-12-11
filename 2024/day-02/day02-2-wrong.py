#!/usr/bin/env python3

"""
--- Part Two ---

The engineers are surprised by the low number of safe reports until they realize they forgot to tell you 
about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level 
in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, 
the report instead counts as safe.

More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.

Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. 
How many reports are now safe?




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


def check_if_safe(report: list[int]) -> bool:
    bad_levels = 0
    level_direction = 0
    for index, current_level in enumerate(report[:-1]):
        delta = report[index+1] - current_level
        if not 1 <= abs(delta) <= 3:
            bad_levels += 1
        elif delta < 0 and level_direction > 0 or \
             delta > 0 and level_direction < 0:
            bad_levels += 1
            level_direction = delta
        else:
            level_direction = delta
        if bad_levels > 1:
            return False
    return True


def main():
    safe_reports = 0
    for report_str in load_input():
        report_int = list(map(int, report_str.split()))
        if check_if_safe(report_int):
            safe_reports += 1
    print(f"Safe reports: {safe_reports}")


if __name__ == "__main__":
    main()
