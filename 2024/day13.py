import functools
import math
import re
import numpy as np
from queue import PriorityQueue


# f = open('data/day13-sample.txt', 'r')
f = open('data/day13-final.txt', 'r')

lines = [l.strip() for l in f if len(l.strip()) != 0]
group = list(zip(*(iter(lines),) * 3))
machines = [(
    tuple(map(int, re.findall(r'Button .: X\+([0-9]+), Y\+([0-9]+)', a)[0])),
    tuple(map(int, re.findall(r'Button .: X\+([0-9]+), Y\+([0-9]+)', b)[0])),
    tuple(map(int, re.findall(r'Prize: X=([0-9]+), Y=([0-9]+)', p)[0]))) for a,b,p in group]


def part1(machines, limit=100):
    return sum([equation(t, a, b) for (a, b, t) in machines])


def equation(t, a, b, offset=0):
    ax, ay = a
    bx, by = b
    x, y = t
    x += offset
    y += offset

    den = ax*by - ay*bx
    if den == 0:
        return 0

    gamma = int((ax*y - ay * x) / den)
    alpha = int((x - bx * gamma) / ax)

    if(x == ax * alpha + bx * gamma) and (y == ay * alpha + by * gamma):
        return int(alpha * 3 + gamma)

    return 0


def part2(machines):
    return sum([equation(t, a, b, 10000000000000)
                for (a, b, t) in machines])


print("part1: ", part1(machines))
print("part2: ", part2(machines))
