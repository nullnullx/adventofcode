#!/usr/bin/env python3

"""
--- Day 1: Secret Entrance ---

You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the password seems to have been changed, so you can't get in. A document taped to the wall helpfully explains:
"Due to new security protocols, the password is locked in the safe below. Please see the attached document for the new combination."
The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order. As you turn the dial, it makes a small click noise as it reaches each number.
The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.
So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0.
Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0.
So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.
The dial starts by pointing at 50.
You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.
For example, suppose the attached document contained the following rotations:
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82

Following these rotations would cause the dial to move as follows:
    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32.

Because the dial points at 0 a total of three times during this process, the password in this example is 3.
Analyze the rotations in your attached document. What's the actual password to open the door?


Solution:
Use "map" to convert right rotation to positive integer and left rotation to negative integer.
Number of full circles in one rotation can be ignored and only the final position matters.
If the final position is 0, convert it to boolean True (1), otherwise False (0).
Sum up all boolean values to get the total number of times the dial points at 0. Use generator expression 
to avoid creating an intermediate list.
We could try to use map and lambda functions to avoid generator expression during summation,
but we can't use enclosing variable (dial_position) inside lambda in Python.
"""

import sys
sys.path.append('..')
from aoc import load_input

def main() -> None:
    rotations = load_input()
    dial_position = 50
    rotations_int = map(lambda x: int(x[1:]) if x[0] == 'R' else -int(x[1:]), rotations)
    total_zeros = sum((not (dial_position := (dial_position + rotation) % 100) for rotation in rotations_int))
    print(total_zeros)    

if __name__ == "__main__":
    main()
