import re
import math


# f = open('data/day02-sample.txt', 'r')
f = open('data/day02-final.txt', 'r')


def part1(lines):
    return sum([1 for level in lines if check_level(level)])


def is_safe(diffs):
    for i in range(0, len(diffs), 1):
        if (i + 1 < len(diffs) and diffs[i] * diffs[i + 1] < 0) or (0 >= abs(diffs[i]) or abs(diffs[i]) > 3):
            return False
    else:
        return True


def check_level(level):
    pairs = list(zip(level, level[1:]))
    if is_safe([a - b for (a, b) in pairs]):
        return True
    return False


def part2(lines):
    safe = 0

    for level in lines:
        if check_level(level):
            safe += 1
        else:
            for i in range(0, len(level)):
                if check_level(level[0:i] + level[i+1:]):
                    safe += 1
                    break
    return safe



lines = [list(map(int, l.strip().split(' '))) for l in f]

print("part1: ", part1(lines))
print("part2: ", part2(lines))
