import re

# f = open('data/day09-sample.txt', 'r')
f = open('data/day09-final.txt', 'r')


def doit(l, f):
    # if all elements in l are 0 return 0
    if [0]*len(l) == l:
        return 0

    diffs = [l[i+1] - l[i] for i in range(len(l) - 1)]
    return f(l, doit(diffs, f))


def part1(lines, f):
    return sum([doit(l, f) for l in lines])


lines = [l.strip() for l in f]

print("part1: ", part1([[int(n) for n in l.split(' ')] for l in lines], lambda l, last: l[-1] + last))
print("part2: ", part1([[int(n) for n in l.split(' ')] for l in lines], lambda l, last: l[0] - last))
