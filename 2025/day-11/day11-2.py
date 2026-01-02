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
Represent the devices and their connections as a directed graph using dictionary of tuples.
If requirement is to find paths that visit intermediate node A, it is more efficient to split the problem:
Find all paths from start to A, then from A to stop and multiply the results.
We use recursive depth-first search (DFS) to explore all possible paths in six smaller sub-graphs:
svr->fft, fft->dac, dac->out and svr->dac, dac->fft, fft->out.
Result is the sum of the products of the number of paths in each sub-graph.
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
    svr_fft = dfs_path(frozendict(devices_graph), 'svr', 'fft')
    svr_dac = dfs_path(frozendict(devices_graph), 'svr', 'dac')
    fft_dac = dfs_path(frozendict(devices_graph), 'fft', 'dac')
    dac_fft = dfs_path(frozendict(devices_graph), 'dac', 'fft')
    fft_out = dfs_path(frozendict(devices_graph), 'fft', 'out')
    dac_out = dfs_path(frozendict(devices_graph), 'dac', 'out')
    print(svr_fft * fft_dac * dac_out + svr_dac * dac_fft * fft_out)


if __name__ == "__main__":
    main()
