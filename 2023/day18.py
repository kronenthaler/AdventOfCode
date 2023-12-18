import copy
import re
import math


# f = open('data/day18-sample.txt', 'r')
f = open('data/day18-final.txt', 'r')


directions = {
    'R': (0, 1),
    'D': (1, 0),
    'U': (-1, 0),
    'L': (0, -1)
}

trans = ['R','D','L','U']

def part1(inst):
    # expand map and find the minx, minj, maxx, maxy (keep track of the center)
    ci, cj = 0, 0
    mini, minj = math.inf, math.inf
    maxi, maxj = -math.inf, -math.inf

    for d, s, _ in inst:
        si, sj = directions[d]
        ci, cj = ci + (si*s), cj + (sj*s)
        mini = min(ci, mini)
        minj = min(cj, minj)
        maxi = max(ci, maxi)
        maxj = max(cj, maxj)

    sizei = maxi - mini + 3
    sizej = maxj - minj + 3
    ci, cj = 0 - mini + 1, 0 - minj + 1
    board = [['.'] * sizej for i in range(sizei)]
    board[ci][cj] = '#'
    for d, s, _ in inst:
        si, sj = directions[d]
        for t in range(s):
            ci, cj = ci + si, cj + sj
            board[ci][cj] = '#'

    # fill-in
    total = sum([l.count('#') for l in board])
    queue = [(0, 0)]
    while len(queue) != 0:
        i, j = queue.pop(0)
        if board[i][j] != '.': continue
        board[i][j] = ' '
        queue.extend(list([(i + sx, j + sy) for sx, sy in directions.values() if 0 <= i + sx < sizei and 0 <= j + sy < sizej]))

    total += sum([l.count('.') for l in board])
    return total


def part2(inst):
    # shoelace formula: 1/2 * sum((x0*y1 - x1*y0)) for each point in the polygon (including connection to start point)
    ci, cj = 0, 0
    points = [(ci, cj)]
    perimeter = 0
    for d, s, _ in inst:
        si, sj = directions[d]
        ci, cj = ci + (si*s), cj + (sj*s)
        perimeter += s
        points.append((ci, cj))

    polygon = list(zip(points, points[1:] + points[:1]))
    area = abs(sum([(x0*y1) - (x1*y0) for (x0, y0), (x1, y1) in polygon]))

    return 1 + ((area + perimeter) // 2)


inst = [re.match(r'([A-Z]) ([0-9]+) \(#([0-9a-f]+)\)', l.strip()).groups() for l in f]
inst = [(d, int(s), c) for d, s, c in inst]

print("part1: ", part1(inst))
print("part2: ", part2([(trans[int(c[-1])], int(c[0:5], 16), c) for _, _, c in inst]))
