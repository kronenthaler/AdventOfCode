import re

# f = open('data/day09-sample.txt', 'r')
f = open('data/day09-final.txt', 'r')

def doit(l, f):
    # if all elements in l are 0 return 0
    if [0]*len(l) == l:
        return 0

    diffs = []
    for i in range(len(l) - 1):
        diffs.append(l[i+1] - l[i])

    last = doit(diffs, f)
    return f(l, last)


def part1(lines, f):
    total = [doit(l, f) for l in lines]
    return sum(total)


lines = [l.strip() for l in f]

print("part1: ", part1([[int(n) for n in l.split(' ')] for l in lines], lambda l, last: l[-1] + last))
print("part2: ", part1([[int(n) for n in l.split(' ')] for l in lines], lambda l, last: l[0] - last))
