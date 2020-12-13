import re

#f = open('day3-sample.txt', 'r')
f = open('data/day3-final.txt', 'r')
content = [line.strip() for line in f.readlines()]

height = content.__len__()
width = content[0].__len__()
increments = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
aggregated = 1
for increment in increments:
    trees = 0
    column = 0
    for row in range(0, height, increment[0]):
        if content[row][column] == '#':
            trees += 1
        column = (column + increment[1]) % width

    if increment[0] == 1 and increment[1] == 3:
        print("part1:", trees)

    aggregated *= trees
print("part2:", aggregated)