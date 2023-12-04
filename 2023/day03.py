import re
from itertools import chain

# f = open('data/day03-sample.txt', 'r')
f = open('data/day03-final.txt', 'r')

steps = [(-1, -1), (+0, -1), (+1, -1),
         (-1, +0), (+0, +0), (+1, +0),
         (-1, +1), (+0, +1), (+1, +1)]


def is_part(lines, i, j):  # return a set((i,j,*))
    neighbours = set()
    for sx, sy in steps:
        if sx == 0 and sy == 0: continue
        if (0 <= i+sx < len(lines) and 0 <= j+sy < len(lines[i]) and
                not lines[i+sx][j+sy].isdigit() and lines[i+sx][j+sy] != '.'):
            neighbours.add((i+sx, j+sy, lines[i+sx][j+sy]))
    return neighbours


def part1(lines):
    numbers = []  # (number, neighbours)
    isnew = False
    number = ''
    for i, l in enumerate(lines):
        neighbours = None
        for j, c in enumerate(l):
            if c.isdigit():
                if isnew:
                    number += c
                else:
                    isnew = True
                    number = c
                    neighbours = set()
                neighbours.update(is_part(lines, i, j))
            elif isnew:
                isnew = False
                if neighbours is not None and len(neighbours) > 0:
                    numbers.append((int(number), neighbours))
                number = ''
                continue

        if isnew and len(neighbours) > 0:
            numbers.append((int(number), neighbours))

    return numbers # 550934


def part2(items):
    # invert the graph
    matrix = {} # (i,j,*)
    for number, neighbours in items:
        for i, j, symbol in neighbours:
            if symbol != '*': continue
            if (i, j, symbol) not in matrix:
                matrix[(i, j, symbol)] = []
            matrix[(i, j, symbol)].append(number)

    return sum([x[0]*x[1] for x in matrix.values() if len(x) == 2])


lines = [l.strip() for l in f]

processed = part1(lines)
print("part1: ", sum([x for x, _ in processed]))
print("part2: ", part2(processed))
