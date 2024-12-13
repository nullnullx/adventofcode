#!/usr/bin/env python3

"""
--- Day 4: Ceres Search ---

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. 
After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know 
if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. 
It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. 
Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved 
in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. How many times does XMAS appear?




Solution:
Use count() method to count number of XMAS appearances in the string.
Search for XMAS in every row, then every column, every left-to-right diagonal and every right-to-left diagonal.
To search for SAMX, reverse search word or search string using [::-1].
"""


import sys
sys.path.append('..')
from aoc import load_input

THE_WORD = 'XMAS'


def search_horizontal(input: tuple[str]) -> int:
    total_found = 0
    for row in input:
        total_found += row.count(THE_WORD)
        total_found += row.count(THE_WORD[::-1])
    return total_found


def search_vertical(input: tuple[str]) -> int:
    total_found = 0
    for column in map(lambda x: ''.join(x), zip(*input)):
        total_found += column.count(THE_WORD)
        total_found += column.count(THE_WORD[::-1])
    return total_found


def search_diagonal(input: tuple[str]) -> int:
    x_size = len(input[0])
    y_size = len(input)
    total_found = 0
    
    # TODO: merge first and third for loop. Merge second and fourth for loop.
    # TODO: stop for loop earlier - no need to check strings shorten than len("XMAS")
    for x_coordinate in range(x_size):
        diagonal = ''.join([input[i-x_coordinate][i] for i in range(x_coordinate, x_size)])
        total_found += diagonal.count(THE_WORD)
        total_found += diagonal.count(THE_WORD[::-1])

    for y_coordinate in range(1, y_size):
        diagonal = ''.join([input[i][i-y_coordinate] for i in range(y_coordinate, y_size)])
        total_found += diagonal.count(THE_WORD)
        total_found += diagonal.count(THE_WORD[::-1])

    for x_coordinate in range(x_size):
        diagonal = ''.join([input[i-x_coordinate][x_size-i-1] for i in range(x_coordinate, x_size)])
        total_found += diagonal.count(THE_WORD)
        total_found += diagonal.count(THE_WORD[::-1])

    for y_coordinate in range(1, y_size):
        diagonal = ''.join([input[i][x_size-i+y_coordinate-1] for i in range(y_coordinate, y_size)])
        # diagonal = ''
        # for i in range(1, y_size):
        #     print(f"{i} {x_size-i+y_coordinate-1}")
        #     diagonal += input[i][x_size-i+y_coordinate-1]
        # print(diagonal)
        total_found += diagonal.count(THE_WORD)
        total_found += diagonal.count(THE_WORD[::-1])

    return total_found
    

def main() -> None:
    all_input = tuple(load_input())
    total_found = search_horizontal(all_input) 
    total_found += search_vertical(all_input)
    total_found += search_diagonal(all_input)

    print(f"Times XMAS found: {total_found}")


if __name__ == "__main__":
    main()
