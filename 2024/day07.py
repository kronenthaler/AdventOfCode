import re

# f = open('data/day07-sample.txt', 'r')
f = open('data/day07-final.txt', 'r')


def bt(target, accum, l, part2=False):
    if len(l) == 0:
        return accum == target

    if bt(target, accum + l[0], l[1:], part2):
        return True
    if bt(target, accum * l[0], l[1:], part2):
        return True
    if part2 and bt(target, int(str(accum)+str(l[0])), l[1:], part2):
        return True

    return False


def part1(l):
    total = 0
    for target, values in l:
        target = int(target)
        operands = [int(x) for x in values.strip().split(' ')]
        if bt(target, operands[0], operands[1:]):
            total += target

    return total


def part2(l):
    total = 0
    for target, values in l:
        target = int(target)
        operands = [int(x) for x in values.strip().split(' ')]
        if bt(target, operands[0], operands[1:], True):
            total += target

    return total


lines = [tuple(l.strip().split(':')) for l in f]

print("part1: ", part1(lines))
print("part2: ", part2(lines))
