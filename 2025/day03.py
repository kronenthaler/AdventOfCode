from utils import *

# f = open('data/day03-sample.txt', 'r')
f = open('data/day03-final.txt', 'r')

lines = [list(l.strip()) for l in f]


def doit(l, n):
    if n == 0:
        return ""
    first = max(l[0:len(l) - (n-1)])
    return first + doit(l[l.index(first)+1:], n-1)


def part1(l):
    return sum([int(doit(b, 2)) for b in l])


def part2(l):
    return sum([int(doit(b, 12)) for b in l])


print("part1: ", part1(lines))
print("part2: ", part2(lines))
