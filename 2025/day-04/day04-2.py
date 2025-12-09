#!/usr/bin/env python3

"""
--- Part Two ---

Now, the Elves just need help accessing as much of the paper as they can.
Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, 
the forklifts might be able to access more rolls of paper, which they might also be able to remove. 
How many total rolls of paper could the Elves remove if they keep repeating this process?
Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, 
using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:

Initial state:
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

Remove 13 rolls of paper:
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

Remove 12 rolls of paper:
.......x..
.@@.x.x.@x
x@@@@...@@
x.@@@@..x.
.@.@@@@.x.
.x@@@@@@.x
.x.@.@.@@@
..@@@.@@@@
.x@@@@@@@.
....@@@...

Remove 7 rolls of paper:
..........
.x@.....x.
.@@@@...xx
..@@@@....
.x.@@@@...
..@@@@@@..
...@.@.@@x
..@@@.@@@@
..x@@@@@@.
....@@@...

Remove 5 rolls of paper:
..........
..x.......
.x@@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@@.
....@@@...

Remove 2 rolls of paper:
..........
..........
..x@@.....
..@@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@x.
....@@@...

Remove 1 roll of paper:
..........
..........
...@@.....
..x@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
...x@.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
....x.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.
Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?




Solution:
Use the same is_roll_accessible function as in part one to check if a roll of paper can be removed.
Create a recursive function that will walk through the grid, count the number of accessible rolls of paper,
remove them from the copy of grid, and call itself again until no more rolls of paper can be removed.
Since strings are not mutable, convert the grid to a list of lists for easier manipulation.
"""

import sys
from copy import deepcopy
import itertools

sys.path.append('..')
from aoc import load_input


def is_roll_accessible(grid: list[list[str]], row: int, column: int) -> bool:
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


def count_accessible_rolls(grid: list[list[str]]) -> int:
    updated_grid = deepcopy(grid)
    accessible_rolls = 0
    for row, col in itertools.product(range(len(grid)), range(len(grid[0]))):
        if grid[row][col] == '@' and is_roll_accessible(grid, row, col):
            updated_grid[row][col] = '.'
            accessible_rolls += 1
    if accessible_rolls == 0:
        return 0
    return accessible_rolls + count_accessible_rolls(updated_grid)


def main() -> None:
    grid = list(map(list, load_input()))
    accessible_rolls = count_accessible_rolls(grid)
    print(accessible_rolls)


if __name__ == "__main__":
    main()
