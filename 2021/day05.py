import re

# f = open('data/day05-sample.txt', 'r')
f = open('data/day05-final.txt', 'r')

coords = []
regex = r'([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)'
for line in f:
    toks = re.split(regex, line)
    coords.append(((int(toks[1]), int(toks[2])), (int(toks[3]), int(toks[4]))))


def print_b(b, n, m):
    for i in range(0, n):
        line = ""
        for j in range(0, m):
            line += str(b[i*n+j])
        print(line)
    print("")


def part1(input):
    coords = [(a, b) for (a, b) in input if a[0] == b[0] or a[1] == b[1]]
    maxN = (max([max(x1, x2) for (x1, _), (x2, _) in coords])+1,max([max(y1, y2) for (_, y1), (_, y2) in coords])+1)

    board = [0] * maxN[0] * maxN[0]
    # i * (maxX) + j
    for (x1, y1), (x2, y2) in coords:
        x0, xN = (min(x1, x2), max(x1, x2))
        y0, yN = (min(y1, y2), max(y1, y2))
        if x0 == xN:
            for i in range(y0, yN+1):
                board[(x0 * maxN[0]) + i] += 1
        else:
            for i in range(x0, xN+1):
                board[(i * maxN[0]) + y0] += 1

    return len([x for x in board if x >= 2])


def part2(corrds):
    maxN = (max([max(x1, x2) for (x1, _), (x2, _) in coords])+1,max([max(y1, y2) for (_, y1), (_, y2) in coords])+1)

    board = [0] * maxN[0] * maxN[1]
    # i * (maxX) + j
    for (x1, y1), (x2, y2) in coords:
        x0, xN = (min(x1, x2), max(x1, x2))
        y0, yN = (min(y1, y2), max(y1, y2))
        if x0 == xN:
            for i in range(y0, yN + 1):
                board[(x0 * maxN[0]) + i] += 1
        elif y0 == yN:
            for i in range(x0, xN + 1):
                board[(i * maxN[0]) + y0] += 1
        else:
            src = (x1, y1) if x1 < x2 else (x2, y2)
            dst = (x1, y1) if x1 >= x2 else (x2, y2)
            inc = 1 if src[1] < dst[1] else -1

            y = src[1]
            for i in range(x0, xN + 1):
                board[(i * maxN[0]) + y] += 1
                y += inc

    return len([x for x in board if x >= 2])


print("part1: {}".format(part1(coords)))
print("part2: {}".format(part2(coords)))
