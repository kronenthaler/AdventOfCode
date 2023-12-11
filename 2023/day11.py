import re

# f = open('data/day11-sample.txt', 'r')
f = open('data/day11-final.txt', 'r')


def part1(galaxies):
    total = 0
    for a in galaxies:
        for b in galaxies:
            if a == b: continue
            total += abs(a[0] - b[0]) + abs(a[1]-b[1])

    return total // 2


lines = [l.strip() for l in f]


def expand(lines, factor=2):
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                galaxies.append((i, j))

    empty_lines = []
    total = 0
    for i in range(len(lines)):
        if '#' not in lines[i]:
            total += factor-1
        empty_lines.append(total)

    empty_columns = []
    total = 0
    for j in range(len(lines[0])):
        for i in range(len(lines)):
            if lines[i][j] == '#':
                break
        else:
            total += factor-1
        empty_columns.append(total)

    expanded_galaxies = []
    for i,j in galaxies:
        expanded_galaxies.append((i + (empty_lines[i]), j + (empty_columns[j])))
    return expanded_galaxies

print("part1: ", part1(expand(lines, 2)))
print("part2: ", part1(expand(lines, 1_000_000)))
