import copy
import re
import math
from queue import PriorityQueue as queue

f = open('data/day17-sample.txt', 'r')
# f = open('data/day17-final.txt', 'r')


steps = [(1,0), (-1,0), (0,1), (0,-1)]

dsymbol = ['>', 'v', '<', '^']

RIGHT=(0, 1, 0)
DOWN=(1, 0, 1)
LEFT=(0, -1, 2)
UP=(-1, 0, 3)

directions = [  # (i,j, d-index)
    # straight, left,  right
    [RIGHT, UP, DOWN],  # 0: right >
    [DOWN, LEFT, RIGHT],  # 1: down v
    [LEFT, UP, DOWN],  # 2: left <
    [UP, LEFT, RIGHT]   # 3: up ^
]


def print_path(path, b, target):
    board = copy.deepcopy(b)
    current = target
    while current != (0, 0):
        i, j, d = path[current[0]][current[1]]
        board[i][j] = dsymbol[d]
        current = i, j

    [print("".join(str(x) for x in l)) for l in board]


def valid_path(path, i, j):
    subpath = []
    steps = 0
    while steps < 3 and (i, j) != (0, 0):
        i, j, d = path[i][j]
        steps += 1
        subpath.append(d)

    return subpath


def part1(board):
    # funky-dijsktra
    # shortest path with additional constraints (not longer than 3 steps in the same direction)
    # 3 moves: left, right, straight (all depend on entry direction)
    n = len(board)
    m = len(board[0])
    visited = set()  # (i, j, d)
    # costs = list([[math.inf for j in range(m)] for i in range(n)])
    # costs[0][0] = 0
    # full_path = list([[(-1, -1, -1) for j in range(m)] for i in range(n)])

    q = list()
    q.append(((0, 0, 0, 0), []))  # right
    q.append(((0, 0, 1, 0), []))  # down

    best = math.inf
    best_path = None
    while len(q) != 0:
        (i, j, d, cost), path = q.pop(0)

        if len(path) > 3 * n * m:
            continue

        if (i, j) == (n-1, m-1):
            print('found solution: ', cost + board[-1][-1], path)
            if best > cost + board[-1][-1]:
                best = min(best, cost + board[-1][-1])
                best_path = path
            continue

        start_range = 1 if len(path) >= 3 and path[-3] and path[-2] == path[-1] == d else 0
        for si, sj, nd in directions[d][start_range:]:
            ni, nj = (i + si, j + sj)

            if (0 <= ni < n and 0 <= nj < m and
                (ni, nj) not in visited and
                cost + board[ni][nj] < best):
                q.append(((ni, nj, nd, cost + board[ni][nj]), path + [d]))

    print(best_path)
    return best

def part2(l):
    pass


lines = [list(map(int, list(l.strip()))) for l in f]
print(lines)

print("part1: ", part1(lines))
print("part2: ", part2(lines))
