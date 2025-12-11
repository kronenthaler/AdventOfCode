from utils import *

# f = open('data/day11-sample.txt', 'r')
f = open('data/day11-final.txt', 'r')

lines = {l.strip().split(':')[0]: l.split(':')[1].strip().split(' ') for l in f}


def part1(start, G):
    queue = [start]
    total = 0
    while queue:
        current = queue.pop(0)

        if current == 'out':
            total += 1
            continue

        for c in G[current]:
            queue.append(c)

    return total


@functools.cache
def doit(current, dac, fft):
    if current == 'out':
        return 1 if dac and fft else 0

    return sum(doit(c, dac or c == 'dac', fft or c == 'fft') for c in lines[current])


def part2(start, G):
    return doit('svr', False, False)


print("part1: ", part1('you', lines))
print("part2: ", part2('svr', lines))
