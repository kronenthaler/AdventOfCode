import re
from copy import deepcopy
import numpy as np


# f = open('data/day08-sample.txt', 'r')
f = open('data/day08-final.txt', 'r')

def cmp(a, bounds):
    return 0 <= a[0] < bounds[0] and 0 <= a[1] < bounds[1]

def part1(l, antennas):
    antinode = set()
    for ref, antenna in antennas.items():
        for a in range(len(antenna)-1):
            for b in range(1, len(antenna)):
                if a == b:
                    continue

                delta = tuple(np.subtract(antenna[a], antenna[b]))
                na = tuple(np.add(antenna[a], delta))
                nb = tuple(np.subtract(antenna[b], delta))

                if cmp(na, (N, M)):
                    antinode.add(na)
                if cmp(nb, (N, M)):
                    antinode.add(nb)
    return len(antinode)


def part2(l, antennas):
    antinode = set()
    for ref, antenna in antennas.items():
        for a in range(len(antenna) - 1):
            for b in range(1, len(antenna)):
                if a == b:
                    continue

                delta = tuple(np.subtract(antenna[a], antenna[b]))

                na = antenna[a]
                while cmp(na, (N, M)):
                    antinode.add(na)
                    na = tuple(np.add(na, delta))

                nb = antenna[b]
                while cmp(nb, (N, M)):
                    antinode.add(nb)
                    nb = tuple(np.subtract(nb, delta))

    return len(antinode)


lines = [list(l.strip()) for l in f]
N = len(lines)
M = len(lines[0])
antennas = {}
for i in range(N):
    for j in range(M):
        if lines[i][j] != '.':
            antennas[lines[i][j]] = antennas.get(lines[i][j], []) + [(i, j)]


print("part1: ", part1(lines, antennas))
print("part2: ", part2(lines, antennas))
