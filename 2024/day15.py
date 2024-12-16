from utils import *
from copy import deepcopy

# f = open('data/day15-sample.txt', 'r')
f = open('data/day15-final.txt', 'r')

board = []
for l in f:
    l = list(l.strip())
    if len(l) == 0:
        break
    board.append(l)
N = len(board)
M = len(board[0])
commands = "".join(l.strip() for l in f)


def find_next_free(p, dir, m):
    while True:
        ni, nj = add(p, dir)
        if m[ni][nj] == '.':
            return (ni, nj), p
        if m[ni][nj] == '#':
            return None
        p = (ni, nj)


def part1(m, commands):
    robot = (0, 0)
    for i in range(N):
        for j in range(M):
            if m[i][j] == '@':
                robot = (i, j)
                break

    for d in commands:
        step = DirFromArrow[d]
        ni, nj = add(robot, step)
        if m[ni][nj] == 'O':
            result = find_next_free((ni, nj), step, m)
            if result is None:
                continue
            (fi, fj), (bi, bj) = result
            m[fi][fj] = m[bi][bj]
            m[ni][nj] = '@'
            m[robot[0]][robot[1]] = '.'
            robot = (ni, nj)
        if m[ni][nj] == '.':
            m[ni][nj] = '@'
            m[robot[0]][robot[1]] = '.'
            robot = (ni, nj)

    total = 0
    for i in range(N):
        for j in range(M):
            if m[i][j] == 'O':
                total += i * 100 + j
    return total


def part2(m, commands):
    # expand according to rules.
    # rules for movement are different.
    # pain in the ass.
    pass


print("part1: ", part1(deepcopy(board), commands))
print("part2: ", part2(deepcopy(board), commands))
