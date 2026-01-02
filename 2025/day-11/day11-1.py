#!/usr/bin/env python3

"""
--- Day 11: Reactor ---

You hear some loud beeping coming from a hatch in the floor of the factory, so you decide to check it out. 
Inside, you find several large electrical conduits and a ladder.
Climbing down the ladder, you discover the source of the beeping: a large, toroidal reactor which powers the factory above. 
Some Elves here are hurriedly running between the reactor and a nearby server rack, apparently trying to fix something.
One of the Elves notices you and rushes over. "It's a good thing you're here! We just installed a new server rack, 
but we aren't having any luck getting the reactor to communicate with it!" You glance around the room and see a tangle of 
cables and devices running from the server rack to the reactor. She rushes off, returning a moment later with a list of 
the devices and their outputs (your puzzle input).
For example:

aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out

Each line gives the name of a device followed by a list of the devices to which its outputs are attached. 
So, bbb: ddd eee means that device bbb has two outputs, one leading to device ddd and the other leading to device eee.
The Elves are pretty sure that the issue isn't due to any specific device, but rather that the issue is triggered 
by data following some specific path through the devices. Data only ever flows from a device through its outputs; 
it can't flow backwards.
After dividing up the work, the Elves would like you to focus on the devices starting with the one next to you 
(an Elf hastily attaches a label which just says you) and ending with the main output to the reactor 
(which is the device with the label out).
To help the Elves figure out which path is causing the issue, they need you to find every path from you to out.
In this example, these are all of the paths from you to out:

    Data could take the connection from you to bbb, then from bbb to ddd, then from ddd to ggg, then from ggg to out.
    Data could take the connection to bbb, then to eee, then to out.
    Data could go to ccc, then ddd, then ggg, then out.
    Data could go to ccc, then eee, then out.
    Data could go to ccc, then fff, then out.

In total, there are 5 different paths leading from you to out.

How many different paths lead from you to out?



Solution:
Represent the devices and their connections as a directed graph using dictionary of tuples.
Then we use recursive depth-first search (DFS) to explore all possible paths from the "you" node to the "out" node.
Use memoization (@cache decorator) to cache results of sub-graphs for efficiency.
@cache requires function arguments to be hashable, so we use frozendict to represent the graph.
"""

import sys
from functools import cache
from frozendict import frozendict

sys.path.append('..')
from aoc import load_input


@cache
def dfs_path(graph: frozendict[str, list[str]], start: str, stop: str) -> int:
    if start == stop:
        return 1
    total_paths = 0
    for neighbor in graph.get(start, ()):
        total_paths += dfs_path(graph, neighbor, stop)
    return total_paths


def main() -> None:
    devices = load_input()
    devices_graph = {}
    for device in devices:
        name, outputs = device.split(': ')
        devices_graph[name] = tuple(outputs.split(' ') if outputs else [])
    print(dfs_path(frozendict(devices_graph), 'svr', 'out'))


if __name__ == "__main__":
    main()
