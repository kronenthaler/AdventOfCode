import functools

from utils import *

# f = open('data/day19-sample.txt', 'r')
f = open('data/day19-final.txt', 'r')

towels = [t.strip() for t in f.readline().strip().split(',')]
f.readline()
designs = [l.strip() for l in f]


# bt + memo

def part1(towels, designs):
    @functools.cache
    def bt(target):
        if len(target) == 0:
            return 1
        for t in towels:
            if target.startswith(t) and bt(target[len(t):]):
                return 1
        return 0

    return sum([bt(d) for d in designs])


# likely find the optimal solution
def part2(towels, designs):
    @functools.cache
    def bt(target):
        if len(target) == 0:
            return 1
        total = 0
        for t in towels:
            if target.startswith(t):
                total += bt(target[len(t):])
        return total

    return sum([bt(d) for d in designs])


print("part1: ", part1(towels, designs))
print("part2: ", part2(towels, designs))
