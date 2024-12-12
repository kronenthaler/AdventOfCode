import functools
import math
import re
import numpy as np

# f = open('data/day12-sample.txt', 'r')
f = open('data/day12-final.txt', 'r')

lines = [list(l.strip()) for l in f]
N = len(lines)
M = len(lines[0])

steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
steps2 = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def add(a: tuple, b: tuple) -> tuple:
    return tuple(map(lambda i, j: i + j, a, b))


def valid(t, min=(0, 0), max=(N, M)):
    return all(map(lambda m, t, M: m <= t < M, min, t, max))


def neighbors(c, target, m):
    return sum(_neighbors(c, target, m))


def _neighbors(c, target, m):
    ns = []
    for s in steps:
        n = add(c, s)
        is_valid = valid(n)
        ns.append(1 if (is_valid and m[n[0]][n[1]] != target) or (not is_valid) else 0)
    return ns


def corners(c, target, m):
    pos = _neighbors(c, target, m)
    outer = 0
    inner = 0
    for i in range(len(steps)):
        # count outer corners
        if pos[i] and pos[(i+1) % len(steps)]:
            outer += 1
        # count inner corners
        if not pos[i] and not pos[(i+1) % len(steps)]:
            n = add(c, steps2[i])
            inner += 1 if (valid(n) and m[n[0]][n[1]] != target) else 0

    return outer + inner


def bfs(s, m, visited, neigh):
    target = m[s[0]][s[1]]
    p = neigh(s, target, m)
    q = [s]
    region = set([s])
    visited.add(s)

    while len(q) != 0:
        c = q.pop(0)
        region.add(c)

        for s in steps:
            n = add(c, s)
            if valid(n) and m[n[0]][n[1]] == target and n not in visited:
                visited.add(n)
                q.append(n)
                p += neigh(n, target, m)

    return len(region), p, target


def part1(l, f):
    visited = set()
    regions = [bfs((i, j), l, visited, f) for i in range(N) for j in range(M) if (i, j) not in visited]
    return sum([a * p for (a, p, _) in regions])


print("part1: ", part1(lines, neighbors))
print("part2: ", part1(lines, corners))
