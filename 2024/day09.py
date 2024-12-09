import re
from copy import deepcopy

# f = open('data/day09-sample.txt', 'r')
f = open('data/day09-final.txt', 'r')


def find_free(b, last, count=1):
    for i in range(0, last):
        if -1 not in b[i] or (index := b[i].index(-1)) == -1 or index + count > len(b[i]):
            continue

        for j in range(index, count):
            if b[i][j] != -1:
                break
        else:
            return i
    return -1


def part1(buckets):
    for last in range(len(buckets)-1, -1, -1):
        if last % 2 != 0:
            continue
        for x in list(buckets[last]):
            free = find_free(buckets, last)
            if free == -1:
                break
            index = buckets[free].index(-1)
            buckets[free][index] = x
            del buckets[last][len(buckets[last])-1]
    return checksum(buckets)


def checksum(buckets):
    index = 0
    total = 0
    for bucket in buckets:
        for x in bucket:
            if x != -1:
                total += x * index
            index += 1
    return total


def part2(buckets):
    for last in range(len(buckets) - 1, -1, -1):
        if last % 2 != 0:
            continue

        free = find_free(buckets, last, len(buckets[last]))

        if free == -1:
            continue

        index = buckets[free].index(-1)
        for i in range(index, index + len(buckets[last])):
            buckets[free][i] = buckets[last][-1]
            buckets[last][i - index] = -1

    return checksum(buckets)


lines = [l.strip() for l in f]
lines = lines[0]

buckets = list([None for l in range(len(lines))])
id = 0
occupied = True
for i in range(len(lines)):
    size = int(lines[i])
    if occupied:
        buckets[i] = [id] * size
        id += 1
    else:
        buckets[i] = [-1] * size
    occupied = not occupied

print("part1: ", part1(deepcopy(buckets)))
print("part2: ", part2(deepcopy(buckets)))
