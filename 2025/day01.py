from utils import *

# f = open('data/day01-sample.txt', 'r')
f = open('data/day01-final.txt', 'r')

lines = [l.strip() for l in f]
lines = [(1 if l[0] == 'R' else -1, int(l[1:])) for l in lines]

def part1(l, start):
    pos = start
    count = 0
    for d, c in l:
        pos = (pos + (d * c)) % 100
        if pos == 0:
            count += 1
    return count


def part2(l, start):
    pos = start
    count = 0
    for d, c in l:
        for i in range(1, c+1):
            pos = (pos + d) % 100
            if pos == 0:
                count += 1

    return count


print("part1: ", part1(lines, 50))
print("part2: ", part2(lines, 50))  # 6659 low < 7113 high
