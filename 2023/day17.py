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
    visited = set()  # (i,j)
    costs = list([[math.inf for j in range(m)] for i in range(n)])
    costs[0][0] = 0
    full_path = list([[(-1, -1, -1) for j in range(m)] for i in range(n)])

    q = queue()
    q.put(((0, 0, 0), []))  # right
    q.put(((0, 0, 1), []))  # down
    while not q.empty():
        (i, j, d), path = q.get()

        if (i, j) in visited:
            continue
        visited.add((i, j))

        # get last 3 elements to path i, j
        subpath = valid_path(full_path, i, j)
        [print(i, j, dsymbol[d]) for d in subpath]

        len(path) >= 3 and path[-3] == path[-2] == path[-1]
        start_range = 1 if len(set(subpath)) == 3 or (len(path) >= 3 and path[-3] == path[-2] == path[-1]) else 0
        for si, sj, nd in directions[d][start_range:]:
            ni, nj = (i + si, j + sj)

            # add the last 3 paths if sumx or sumy == 3 -> cannot move forward
            # check of the path lenght should be here...
            if (0 <= ni < n and 0 <= nj < m and
                    (ni, nj) not in visited
                    and costs[i][j] + board[ni][nj] < costs[ni][nj]
                ):

                costs[ni][nj] = costs[i][j] + board[ni][nj]
                full_path[ni][nj] = (i, j, d)
                q.put(((ni, nj, nd), path + [d]))

    [print(c) for c in costs]
    print_path(full_path, board, (12, 12))
    return costs[-1][-1]

def part2(l):
    pass


lines = [list(map(int, list(l.strip()))) for l in f]
print(lines)

print("part1: ", part1(lines))
print("part2: ", part2(lines))
