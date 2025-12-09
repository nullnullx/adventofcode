#!/usr/bin/env python3

"""
--- Day 4: Printing Department ---

You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of 
large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).
Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into 
the North Pole base while the elevators are offline.
"Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's 
a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. 
It's too bad all of our forklifts are so busy moving those big rolls of paper around."
If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.
The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) 
indicating where everything is located.
For example:

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. 
If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking 
down the wall to the cafeteria.
In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?



Solution:
Walk through the grid and for each roll of paper, count the number of adjacent rolls of paper.
Since we are working in cartesian coordinates itertools.product can be used to generate all row and column indices for the grid.
Also itertools.product can be used to create a list of relative row and column offsets to check adjacent positions.
Break out of loop as soon as four adjacent rolls of paper are found.
To sum up all accessible rolls of paper, use a generator expression within the sum function and boolean 1 and 0 equivalence.
"""

import sys
import itertools

sys.path.append('..')
from aoc import load_input


def is_roll_accessible(grid: list[str], row: int, column: int) -> bool:
    adjacent_rolls = 0
    for dr, dc in itertools.product([-1, 0, 1], repeat=2):
        if dr == 0 and dc == 0:
            continue
        r, c = row + dr, column + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            adjacent_rolls += grid[r][c] == '@'
            if adjacent_rolls >= 4:
                return False
    return True


def main() -> None:
    grid = load_input()
    accessible_rolls = sum((grid[row][col] == '@' and is_roll_accessible(grid, row, col) \
                           for row, col in itertools.product(range(len(grid)), range(len(grid[0])))))
    print(accessible_rolls)


if __name__ == "__main__":
    main()
