from shapely.geometry import Polygon
from utils import *

# f = open('data/day09-sample.txt', 'r')
f = open('data/day09-final.txt', 'r')

lines = [tuple(map(int, l.strip().split(','))) for l in f]


def part1(l):
    return max((abs(l[i][0] - l[j][0])+1) * (abs(l[i][1] - l[j][1])+1) for i in range(len(l)) for j in range(i+1, len(l)))


def part2(l):
    polygon = Polygon(lines)
    result = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            a = (l[i][0], l[i][1])
            c = (l[i][0], l[j][1])
            b = (l[j][0], l[j][1])
            d = (l[j][0], l[i][1])
            if polygon.contains(Polygon([a, c, b, d])): # the polygon has holes!
                r = (abs(l[i][0] - l[j][0]) + 1) * (abs(l[i][1] - l[j][1]) + 1)
                result = max(result, r)
    return result

print("part1: ", part1(lines))
print("part2: ", part2(lines))
