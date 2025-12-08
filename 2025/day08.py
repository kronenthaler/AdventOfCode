from utils import *
from disjoint_set import DisjointSet


# f = open('data/day08-sample.txt', 'r'); count = 10
f = open('data/day08-final.txt', 'r'); count = 1000

lines = [tuple(map(int, l.strip().split(','))) for l in f]

distances = []
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        d = math.sqrt((lines[i][0] - lines[j][0]) ** 2 + (lines[i][1] - lines[j][1]) ** 2 + (lines[i][2] - lines[j][2]) ** 2)
        distances.append((d, lines[i], lines[j]))
distances = sorted(distances, key=lambda x: x[0])

def part1(l):
    ds = DisjointSet.from_iterable(l)
    for (d, a, b) in distances[0:count]:
        if not ds.connected(a, b):
            ds.union(a, b)
    bysize = sorted(list(ds.itersets()), key=lambda x: len(x), reverse=True)
    return functools.reduce(lambda a, b: a * b, list(len(b) for b in bysize[0:3]))

def part2(l):
    ds = DisjointSet.from_iterable(l)
    for (d, a, b) in distances:
        if not ds.connected(a, b):
            ds.union(a, b)
            if len(list(ds.itersets())) == 1:
                return a[0] * b[0]
    return -666


print("part1: ", part1(lines))
print("part2: ", part2(lines))
