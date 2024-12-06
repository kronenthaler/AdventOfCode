import re
import numpy as np
from copy import deepcopy

# f = open('data/day06-sample.txt', 'r')
f = open('data/day06-final.txt', 'r')

step = [
    (-1, +0),  # up
    (+0, +1),  # right
    (+1, +0),  # down
    (+0, -1),  # left
]


def part1(m, start):
    visited = set()
    dir = 0  # up
    pos = start
    while True:
        ni, nj = tuple(np.add(pos, step[dir]))
        if 0 > ni or ni >= N or 0 > nj or nj >= M:
            break
        if m[ni][nj] == '#':
            dir = (dir + 1) % 4
            continue

        pos = (ni, nj)
        visited.add(pos)

    return len(visited)


def check(m, start):
    dir = 0  # up
    pos = start
    visited = set((pos, dir))  # pos + dir

    while True:
        ni, nj = tuple(np.add(pos, step[dir]))
        if 0 > ni or ni >= N or 0 > nj or nj >= M:
            break

        if m[ni][nj] == '#':
            dir = (dir + 1) % 4
            continue

        pos = (ni, nj)
        if (pos, dir) in visited:
            return True

        visited.add((pos, dir))
    return False


def part2(m, start):
    count = 0
    for i in range(N):
        for j in range(M):
            if (i, j) != start and m[i][j] == '.':
                nm = deepcopy(m)
                nm[i][j] = '#'
                if check(nm, start):
                    count += 1

    return count


lines = [list(l.strip()) for l in f]

start = (0, 0)
N = len(lines)
M = len(lines[0])
for i in range(N):
    for j in range(M):
        if '^' == lines[i][j]:
            start = (i, j)
            lines[i][j] = '.'
            break


print("part1: ", part1(lines, start))
print("part2: ", part2(lines, start))
