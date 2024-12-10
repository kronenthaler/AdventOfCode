import re
import numpy as np

# f = open('data/day10-sample.txt', 'r')
f = open('data/day10-final.txt', 'r')

steps = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]


def bfs(s, l):
    found = {}
    q = [s]
    while len(q) != 0:
        i, j = q.pop(0)
        if l[i][j] == 9:
            found[(i, j)] = found.get((i, j), 0) + 1
            continue

        for s in steps:
            ni, nj = tuple(np.add((i, j), s))
            if 0 <= ni < N and 0 <= nj < M and l[ni][nj] == l[i][j] + 1:
                q.append((ni, nj))

    return len(found), sum(found.values())


def solve(l):
    total = (0, 0)  #score/rating

    for i in range(N):
        for j in range(M):
            if l[i][j] == 0:
                total = tuple(np.add(total, bfs((i, j), l)))

    return total


lines = [list(map(int, list(l.strip()))) for l in f]
N = len(lines)
M = len(lines[0])

score, rating = solve(lines)
print("part1: ", score)
print("part2: ", rating)
