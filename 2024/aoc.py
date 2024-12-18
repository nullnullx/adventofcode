"""Helper functions for the Advent of Code problems.
"""

import sys


def load_input() -> list[str]:
    """Read input data from the file or STDIN.
    """
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as fh:
            return fh.read().splitlines()
    return sys.stdin.read().splitlines()
