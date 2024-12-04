import re
from itertools import chain

# f = open('data/day03-sample.txt', 'r')
f = open('data/day03-final.txt', 'r')


def part1(lines):
    mults = list(chain.from_iterable([re.findall(r'mul\([0-9]{0,3},[0-9]{0,3}\)', l) for l in lines]))
    elem = list(chain.from_iterable([re.findall(r'\(([0-9]{0,3}),([0-9]{0,3})\)', exp) for exp in mults]))
    return sum([int(x) * int(y) for x, y in elem])


def part2(l):
    mults = list(chain.from_iterable([re.findall(r'(mul\([0-9]{0,3},[0-9]{0,3}\)|do\(\)|don\'t\(\))', l) for l in lines]))
    do = True
    total = 0
    for t in mults:
        if t == "don't()" or t == 'do()':
            do = t == 'do()'
            continue
        if not do:
            continue

        x, y = re.findall(r'\(([0-9]{0,3}),([0-9]{0,3})\)', t)[0]
        total += int(x) * int(y)
    return total


lines = [l.strip() for l in f]

print("part1: ", part1(lines))
print("part2: ", part2(lines))
