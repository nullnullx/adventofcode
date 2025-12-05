#!/usr/bin/env python3

"""
--- Part Two ---

You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.
As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:
"Due to newer security protocols, please use password method 0x434C49434B until further notice."
You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.
Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:
    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.

In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.
Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!
Using password method 0x434C49434B, what is the password to open the door?


Solution:
Use "map" to convert right rotation to positive integer and left rotation to negative integer.
Count number of full circles in one rotation to calculate how many times the dial points at 0 during the rotation.
Add one more if dial crosses 0 during the partial rotation to the final position. 
Use implicit type conversion to convert boolean to 1 or 0.
"""

import sys
sys.path.append('..')
from aoc import load_input

def main() -> None:
    rotations = load_input()
    dial_position = 50
    rotations_int = map(lambda x: int(x[1:]) if x[0] == 'R' else -int(x[1:]), rotations)
    total_zeros = 0
    for rotation in rotations_int:
        previous_position = dial_position
        dial_position = (dial_position + rotation) % 100
        total_zeros += abs(rotation) // 100
        total_zeros += rotation > 0 and dial_position < previous_position or \
                       rotation < 0 and (dial_position > previous_position or dial_position == 0) and previous_position != 0        
    print(total_zeros)    

if __name__ == "__main__":
    main()
