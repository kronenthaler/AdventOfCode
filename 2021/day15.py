import math
import re
import copy
from queue import PriorityQueue as queue


# f = open('data/day15-sample.txt', 'r')
f = open('data/day15-final.txt', 'r')
steps = [(1,0), (-1,0), (0,1), (0,-1)]


def part1(board):
    n = len(board)
    m = len(board[0])
    visited = set()  # (i,j)
    costs = list([[math.inf for j in range(m)] for i in range(n)])
    costs[0][0] = 0

    q = queue()
    q.put((0, (0, 0)))
    while not q.empty():
        value, (i, j) = q.get()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for si, sj in steps:
            ni, nj = (i+si, j+sj)
            if 0 <= ni < n and 0 <= nj < m and \
                    (ni, nj) not in visited and \
                    costs[i][j] + board[ni][nj] < costs[ni][nj]:
                costs[ni][nj] = costs[i][j] + board[ni][nj]
                q.put((costs[ni][nj], (ni, nj)))

    return costs[-1][-1]


def part2(board):
    n = len(board)
    m = len(board[0])

    newboard = list([[board[i][j] if i < n and j < m else 0 for j in range(m*5)] for i in range(n*5)])

    for i in range(0, n*5):
        for j in range(0, m*5):
            if 0 <= i < n and 0 <= j < m:
                continue
            if i >= n:
                newboard[i][j] = (newboard[i-n][j] % 9) + 1
            else:
                newboard[i][j] = (newboard[i][j-m] % 9) + 1
    return part1(newboard)


board = [[int(c) for c in l.strip()] for l in f]

print('part1: ', part1(copy.deepcopy(board)))
print('part2: ', part2(copy.deepcopy(board)))
