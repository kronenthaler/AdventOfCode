import re

# f = open('data/day04-sample.txt', 'r')
f = open('data/day04-final.txt', 'r')


def part1(l):
    incs = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
    target = 'XMAS'
    counter = 0
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] != 'X':
                continue

            for si, sj in incs:
                if i + (si * 3) < 0 or i + (si * 3) >= len(l) or j + (sj * 3) < 0 or j + (sj * 3) >= len(l[0]):
                    continue

                for t in range(1, len(target)):
                    if l[i+(si*t)][j+(sj*t)] != target[t]:
                        break
                else:
                    counter += 1

    return counter


def part2(l):
    counter = 0
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] != 'A' or i - 1 < 0 or i + 1 >= len(l) or j - 1 < 0 or j + 1 >= len(l[0]):
                continue

            if ((l[i-1][j-1] == 'M' and l[i+1][j+1] == 'S') or (l[i-1][j-1] == 'S' and l[i+1][j+1] == 'M')) and \
               ((l[i+1][j-1] == 'M' and l[i-1][j+1] == 'S') or (l[i+1][j-1] == 'S' and l[i-1][j+1] == 'M')):
                counter += 1

    return counter


lines = [l.strip() for l in f]

print("part1: ", part1(lines))
print("part2: ", part2(lines))
