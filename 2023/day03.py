import re
from itertools import chain

f = open('data/day03-sample.txt', 'r')
# f = open('data/day03-final.txt', 'r')

steps = [(-1, -1), (+0, -1), (+1, -1),
         (-1, +0), (+0, +0), (+1, +0),
         (-1, +1), (+0, +1), (+1, +1)]


def is_part(lines, i, j):
    for sx, sy in steps:
        if sx == 0 and sy == 0: continue
        if 0 <= i+sx < len(lines) and 0 <= j+sy < len(lines[i]) and (not lines[i+sx][j+sy].isdigit() and lines[i+sx][j+sy] != '.'):
            return True
    return False


def part1(lines):
    numbers = []
    isnew = False
    number = ''
    for i, l in enumerate(lines):
        valid_part = False
        for j, c in enumerate(l):
            if c.isdigit():
                is_valid = is_part(lines, i, j)
                valid_part |= is_valid
                if isnew:
                    number += c
                else:
                    isnew = True
                    number = c
            elif isnew:
                isnew = False
                if valid_part:
                    numbers.append(int(number))
                number = ''
                valid_part = False
                continue

        if not isnew:
            if valid_part:
                if len(number) > 0:
                    numbers.append(int(number))
    
    print(numbers) # 553577 too high ; 550882 too low
    return sum(numbers)

def part2(l):
    pass


lines = [l for l in f]

print([int(x) for x in list(chain.from_iterable([re.findall(r'(\d+)', l) for l in lines]))])
    

print("part1: ", part1(lines))
print("part2: ", part2(lines))
