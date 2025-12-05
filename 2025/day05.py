from utils import *

# f = open('data/day05-sample.txt', 'r')
f = open('data/day05-final.txt', 'r')

lines = [l.strip() for l in f]
ranges = []
ids = []
flip = False
for l in lines:
    if len(l) == 0:
        flip = True
        continue
    if not flip:
        ranges.append(tuple(map(int, l.split('-'))))
    else:
        ids.append(int(l))

def part1(ranges, ids):
    fresh = 0
    for id in ids:
        for min, max in ranges:
            if min <= id <= max:
                fresh += 1
                break
    return fresh

def part2(ranges):
    for i, range0 in enumerate(ranges):
        for j, range1 in enumerate(ranges[i + 1:], start=i + 1):
            if range0[1] >= range1[0] and range0[0] <= range1[1]:
                ranges[i] = [1, 0]
                ranges[j] = [min(range0[0], range1[0]), max(range0[1], range1[1])]
                break
    return sum([r[1] - r[0] for r in ranges]) + len(ranges)

print("part1: ", part1(ranges, ids))
print("part2: ", part2(ranges))
# 390655532183531 high
# 344841852536362 low
# 347338785050515 < solution
# 347338785050330
# 367748692359946 high (binsearch)
