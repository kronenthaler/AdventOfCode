import copy
import re
import math
from queue import PriorityQueue

# f = open('data/day17-sample.txt', 'r')
f = open('data/day17-final.txt', 'r')


directions = [
    [(-1, 0), (1, 0)],  # up, down
    [(0, -1), (0, 1)]   # left, right
]
dir_to_symbol = {
    (-1, 0): '^',
    (1, 0): 'v',
    (0, -1): '<',
    (0, 1): '>'
}

def part1(board, min_d=1, max_d=3):
    # read up: https://cutonbuminband.github.io/AOC/qmd/2023.html#day-17-clumsy-crucible
    # dijsktra, however what matters are only the states where you turn, direction only need vertical/horizontal.
    N = len(board)
    M = len(board[0])
    target = len(board)-1, len(board[0])-1

    opened = PriorityQueue()
    opened.put((0, (0, 0, 0), ""))  # cost, (i, j, direction), path
    opened.put((0, (0, 0, 1), ""))

    visited = set()

    while not opened.empty():
        cost, (i, j, d), path = opened.get()

        if (i, j) == target:
            # print(path)
            return cost

        if (i, j, d) in visited:
            continue
        visited.add((i, j, d))

        # generate candidates
        for (di, dj) in directions[d]:
            step_cost = cost
            for s in range(1, max_d + 1):  # attempt to turn in s0, s1, s2 ... sN
                ni, nj = i + di * s, j + dj * s
                if not (0 <= ni < N and 0 <= nj < M):
                    continue

                step_cost += board[ni][nj]
                if (ni, nj, 1 - d) in visited:
                    continue

                if s >= min_d:
                    opened.put((step_cost, (ni, nj, 1 - d), path + dir_to_symbol[(di, dj)] * s))

    return -1


lines = [list(map(int, list(l.strip()))) for l in f]
print(lines)

print("part1: ", part1(lines))
print("part2: ", part1(lines, 4, 10))
