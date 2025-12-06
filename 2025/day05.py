from utils import *

f = open('data/day05-sample.txt', 'r')
# f = open('data/day05-final.txt', 'r')

lines = [l.strip() for l in f]
ranges = [tuple(map(int, l.split('-'))) for l in lines[0:lines.index('')]]
ids = [int(l) for l in lines[lines.index('')+1:]]


def part1(ranges, ids):
    return len(set(id for id in ids for min, max in ranges if min <= id <= max))


def part2(ranges):
    for i, range0 in enumerate(ranges):
        for j, range1 in enumerate(ranges[i + 1:], start=i + 1):
            if range0[1] >= range1[0] and range0[0] <= range1[1]:
                ranges[i] = (1, 0)  # generates a -1
                ranges[j] = (min(range0[0], range1[0]), max(range0[1], range1[1]))
                break
    return sum([r[1] - r[0] + 1 for r in ranges])


print("part1: ", part1(ranges, ids))
print("part2: ", part2(ranges))
# 390655532183531 high
# 344841852536362 low
# 347338785050515 < solution
# 347338785050330
# 367748692359946 high (binsearch)
