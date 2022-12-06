import re

# f = open('data/day6-sample.txt', 'r')
f = open('data/day6-final.txt', 'r')


def part1(l, size):
    for i in range(0, len(l)-size):
         if len(set(l[i:i+size])) == size:
             return i+size


seq = "".join([l.strip() for l in f])
print(seq)

print("part1: ", part1(seq, 4))
print("part2: ", part1(seq, 14))