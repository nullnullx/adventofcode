#!/usr/bin/env python3

"""
--- Part Two ---

Thanks in part to your analysis, the Elves have figured out a little bit about the issue. 
They now know that the problematic data path passes through both dac (a digital-to-analog converter) 
and fft (a device which performs a fast Fourier transform).
They're still not sure which specific path is the problem, and so they now need you to find 
every path from svr (the server rack) to out. However, the paths you find must all also visit 
both dac and fft (in any order).
For example:

svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out

This new list of devices contains many paths from svr to out:

svr,aaa,fft,ccc,ddd,hub,fff,ggg,out
svr,aaa,fft,ccc,ddd,hub,fff,hhh,out
svr,aaa,fft,ccc,eee,dac,fff,ggg,out
svr,aaa,fft,ccc,eee,dac,fff,hhh,out
svr,bbb,tty,ccc,ddd,hub,fff,ggg,out
svr,bbb,tty,ccc,ddd,hub,fff,hhh,out
svr,bbb,tty,ccc,eee,dac,fff,ggg,out
svr,bbb,tty,ccc,eee,dac,fff,hhh,out

However, only 2 paths from svr to out visit both dac and fft.

Find all of the paths that lead from svr to out. How many of those paths visit both dac and fft?



Solution:
Represent the devices and their connections as a directed graph using dictionary of lists.
Then we use recursive depth-first search (DFS) to explore all possible paths from the "svr" node to the "out" node.
As we build DFS paths, we keep track of the nodes visited in the current path using a set.
When we reach the "out" node, we check if both "dac" and "fft" are in the visited set.
If they are, we count that path as valid.
This solution probably has a bug, as it doesn't produce results for the very long time.
"""

import sys

sys.path.append('..')
# from aoc import load_input
def load_input() -> list[str]:
    """Read input data from the file or STDIN.
    """
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as fh:
            return fh.read().splitlines()
    return sys.stdin.read().splitlines()


def dfs_path(graph: dict[str, list[str]], start: str, current_path: set[str] | None = None) -> int:
    path1 = set() if current_path is None else current_path.copy()
    if start == 'out':
        if {'dac', 'fft'}.issubset(path1):
            return 1
        else:
            return 0
    total_paths = 0
    if start in path1:
        print(f"Loop detected at {start}, current path: {path1}")
    path1.add(start)
    for neighbor in graph.get(start, []):
        total_paths += dfs_path(graph, neighbor, path1)
    return total_paths


def main() -> None:
    devices = load_input()
    devices_graph = {}
    for device in devices:
        name, outputs = device.split(': ')
        devices_graph[name] = outputs.split(' ') if outputs else []
    print(dfs_path(devices_graph, 'svr'))


if __name__ == "__main__":
    main()
