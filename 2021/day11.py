import re
import copy

# f = open('data/day11-sample.txt', 'r')
f = open('data/day11-final.txt', 'r')

steps = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def print_b(b):
    for i in range(10):
        line = ""
        for j in range(10):
            line += "%d" % b[i][j]
        print(line)
    print("")


def part1(input, n):
    total = 0
    for t in range(n):
        visited = set()
        # increment
        for i in range(10):
            for j in range(10):
                input[i][j] += 1

        # flash
        q = []
        for i in range(10):
            for j in range(10):
                if input[i][j] > 9:
                    q.append((i, j))
                    visited.add((i, j))

        while len(q) != 0:
            i, j = q.pop()
            for sx, sy in steps:
                if 0 <= i+sx < 10 and 0 <= j+sy < 10:
                    input[i+sx][j+sy] += 1
                    if input[i+sx][j+sy] > 9 and (i+sx, j+sy) not in visited:
                        visited.add((i+sx, j+sy))
                        q.append((i+sx, j+sy))

        # reset to 0
        for i, j in visited:
            input[i][j] = 0

        total += len(visited)

    return total


def part2(input, n):
    for t in range(n):
        total = part1(input, 1)
        if total == 100:
            return t + 101


input = [[int(x) for x in l.strip()] for l in f]

print('part1: ', part1(input, 100))
print('part2: ', part2(input, 10000))