from utils import *

# f = open('data/day04-sample.txt', 'r')
f = open('data/day04-final.txt', 'r')

lines = [list(l.strip()) for l in f]


def positions(l):
    pos = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] != '@':
                continue
            count = 0
            for s in Steps2DAll:
                ni, nj = add((i,j), s)
                if 0 <= ni < len(l) and 0 <= nj < len(l[i]) and l[ni][nj] == '@':
                    count += 1
            if count < 4:
                pos.append((i, j))
    return pos


def part1(l):
    total = len(positions(l))
    return total


def part2(l):
    total = 0
    while (pos:=positions(l)) != []:
        total += len(pos)
        for i,j in pos:
            l[i][j] = 'x'
    return total


print("part1: ", part1(lines))
print("part2: ", part2(lines))
