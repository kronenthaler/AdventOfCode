from utils import *

f = open('data/day06-sample.txt', 'r')
# f = open('data/day06-final.txt', 'r')

lines = [l for l in f]


def part1(lines):
    l = [re.split(r'\s+', l.strip()) for l in lines]
    first = list(map(int, l[0]))
    ops = [_sum if o == '+' else _mul for o in l[-1]]

    for row in l[1:-1]:
        for i in range(len(row)):
            first[i] = ops[i](first[i], int(row[i]))

    return sum([a for a in first])


def part2(lines):
    ops = lines[-1]
    # the ops are in the position of the most significant number and at the edge of the column break.
    breaks = [0] + list(i-1 for i in range(1, len(ops)) if ops[i] != ' ')

    # separate the numbers per column retaining the spaces
    columns = [[] for i in range(len(breaks)+1)]
    for r in lines:
        prev = 0
        for i in range(1, len(breaks)):
            columns[i].append(r[prev: breaks[i]])
            prev = breaks[i]+1
        columns[-1].append(r[prev:])

    # process each column
    total = 0
    for c in columns[1:]:
        op = _sum if c[-1].strip() == '+' else _mul
        prep = [list(reversed(d.replace('\n', ''))) for d in c[:-1]]

        # create the numbers per column
        numbers = ["" for i in range(len(breaks))]
        for i, p in enumerate(prep):
            for j, d in enumerate(p):
                if d != ' ' and d != '\n':
                    numbers[j] += d

        # clean up the numbers and process them
        numbers = [n.strip() for n in numbers[:-1]]
        numbers = [int(n) for n in numbers if len(n) != 0]
        total += functools.reduce(op, [int(n) for n in numbers])

    return total


def _sum(a,b):
    return a+b


def _mul(a, b):
    return a*b


print("part1: ", part1(lines))
print("part2: ", part2(lines))
