import re
import json
from copy import deepcopy
from functools import cmp_to_key

# f = open('data/day13-sample.txt', 'r')
f = open('data/day13-final.txt', 'r')


def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return l - r

    if isinstance(l, int):
        l = [l]
    if isinstance(r, int):
        r = [r]

    for le, re in zip(l, r):
        result = compare(le, re)
        if result != 0:
            return result

    if len(l) != len(r):
        return len(l) - len(r)

    return 0


def part1(l):
    return sum([int((i/2)+1) for i in range(0, len(l), 2) if compare(l[i], l[i + 1]) < 0])


def part2(l):
    l.append([[2]])
    l.append([[6]])
    l.sort(key=cmp_to_key(compare))
    return (l.index([[2]]) +1) * (l.index([[6]]) +1)


lines = [json.loads(l.strip()) for l in f if l.strip() != '']


print("part1: ", part1(deepcopy(lines)))
print("part2: ", part2(deepcopy(lines)))
