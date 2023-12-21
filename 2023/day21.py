import re

# f = open('data/day21-sample.txt', 'r')
f = open('data/day21-final.txt', 'r')

steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def part1(board, start, target):
    q = [(start, 0)]
    visited = set()
    even = set()
    odds = set()
    while len(q) > 0:
        (i, j), current_step = q.pop(0)

        if current_step > target:
            break

        if (i, j) in visited:
            continue
        visited.add((i, j))

        for si, sj in steps:
            ni, nj = i + si, j + sj
            if ni < 0 or nj < 0 or ni >= len(board) or nj >= len(board[ni]):
                continue
            if board[ni][nj] == '#':
                continue

            if (current_step + 1) % 2 == 0:
                even.add((ni, nj))
            else:
                odds.add((ni, nj))
            q.append(((ni, nj), current_step + 1))

    return len(even)


def part2(l):
    # cant simulate, there must be a cycle/pattern to exploit and
    # then use the remainder + offset to determine the answer
    pass


lines = [list(l.strip()) for l in f]
start = None
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'S':
            start = i, j
            lines[i][j] = '.'


print("part1: ", part1(lines, start, 64))
print("part2: ", part2(lines))
