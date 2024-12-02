import re
import collections

# f = open('data/day01-sample.txt', 'r')
f = open('data/day01-final.txt', 'r')


def part1(lines):
    left = sorted([int(l) for (l, r) in lines])
    right = sorted([int(r) for (l, r) in lines])
    print(left)
    print(right)

    return sum([abs(a-b) for (a,b) in zip(left, right)])


def part2(lines):
    left = sorted([int(l) for (l, r) in lines])
    right = sorted([int(r) for (l, r) in lines])
    freq = collections.Counter(right)

    return sum([freq[x]*x for x in left])


lines = [tuple(l.strip().replace('   ', ' ').split(' ')) for l in f]

print("part1: ", part1(lines))
print("part2: ", part2(lines))
