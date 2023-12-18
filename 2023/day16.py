import copy
import re

# f = open('data/day16-sample.txt', 'r')
f = open('data/day16-final.txt', 'r')

def split(i, j, board, d1, d2):
    new_rays = []
    if 0 <= i + d1[0] < len(board) and 0 <= j + d1[1] < len(board[0]):
        new_rays.append((i + d1[0], j + d1[1], d1))
    if 0 <= i + d2[0] < len(board) and 0 <= j + d2[1] < len(board[0]):
        new_rays.append((i + d2[0], j + d2[1], d2))
    return new_rays


def part1(board, start):
    visited = set()
    queue = [start]
    while len(queue) != 0:
        i, j, (di, dj) = queue.pop(0)

        if (i, j, (di, dj)) in visited:
            continue

        visited.add((i, j, (di, dj)))

        if board[i][j] == '|' and ((di, dj) == (0, 1) or (di, dj) == (0, -1)):
            queue.extend(split(i, j, board, (1, 0), (-1, 0)))
            continue

        if board[i][j] == '-' and ((di, dj) == (1, 0) or (di, dj) == (-1, 0)):
            queue.extend(split(i, j, board, (0, 1), (0, -1)))
            continue

        if board[i][j] == '/':
            # if d == (0, 1) -> d' = (-1, 0)
            # if d == (0, -1) -> d' = (1, 0)
            # if d == (1, 0) -> d' = (0, -1)
            # if d == (-1, 0) -> d' = (0, 1)

            new_dir = (-dj, -di)
            if 0 <= i + new_dir[0] < len(board) and 0 <= j + new_dir[1] < len(board[0]):
                queue.append((i + new_dir[0], j + new_dir[1], new_dir))
            continue

        if board[i][j] == '\\':
            # if d == (0, 1) -> d' = (1, 0)
            # if d == (0, -1) -> d' = (-1, 0)
            # if d == (1, 0) -> d' = (0, 1)
            # if d == (-1, 0) -> d' = (0, -1)

            new_dir = (dj, di)
            if 0 <= i + new_dir[0] < len(board) and 0 <= j + new_dir[1] < len(board[0]):
                queue.append((i + new_dir[0], j + new_dir[1], new_dir))
            continue

        # keep moving in the same direction
        if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]):
            queue.append((i + di, j + dj, (di, dj)))

    return len(set([(i,j) for i,j,_ in visited]))


def part2(lines):
    best = 0
    for i in range(len(lines)):
        best = max(best, part1(lines, (i, 0, (0, 1))))
    for i in range(len(lines)):
        best = max(best, part1(lines, (i, len(lines[0])-1, (0, -1))))
    for j in range(len(lines[0])):
        best = max(best, part1(lines, (0, j, (1, 0))))
    for j in range(len(lines[0])):
        best = max(best, part1(lines, (len(lines)-1, j, (-1, 0))))
    return best


lines = [list(l.strip()) for l in f]

print("part1: ", part1(lines, (0, 0, (0, 1))))
print("part2: ", part2(lines))
