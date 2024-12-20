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

--- Part Two ---

The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS 
puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?



Solution:
Solving for more general search of any THE_WORD and not just "MAS".
First helper generator function to extract the next square from the input size of len(THE_WORD) x len(THE_WORD).
Second helper function to check if both main diagonals have THE_WORD in forward or reverse direction.
Count number of squares with THE_WORD on the diagonals.
"""


from typing import Generator
import sys
sys.path.append('..')
from aoc import load_input

THE_WORD = 'MAS'


def get_next_square(input: tuple[str]) -> Generator[list[str], None, None]:
    the_word_len = len(THE_WORD)
    for y_coordinate in range(len(input)-the_word_len+1):
        for x_coordinate in range(len(input[0])-the_word_len+1):
            square = []
            for row in input[y_coordinate:y_coordinate+the_word_len]:
                square.append(row[x_coordinate:x_coordinate+the_word_len])
            yield square


def is_x_word(square: list[str]) -> bool:
    diagonal1 = ''.join([square[i][i] for i in range(len(THE_WORD))])
    diagonal2 = ''.join([square[i][-i-1] for i in range(len(THE_WORD))])
    return (diagonal1 == THE_WORD or diagonal1 == THE_WORD[::-1]) and \
            (diagonal2 == THE_WORD or diagonal2 == THE_WORD[::-1])


def main() -> None:
    all_input = tuple(load_input())
    total_x_words = sum(map(lambda x: int(is_x_word(x)), get_next_square(all_input)))

    print(f"Times X-MAS found: {total_x_words}")


if __name__ == "__main__":
    main()
