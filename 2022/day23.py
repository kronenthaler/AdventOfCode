import re
from collections import deque
from functools import cmp_to_key

# f = open('data/day23-sample.txt', 'r')
f = open('data/day23-final.txt', 'r')

incs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
neighbors = [
    [(-1, -1), (-1, 0), (-1, 1)],
    [(1, -1), (1, 0), (1, 1)],
    [(-1, -1), (0, -1), (1, -1)],
    [(-1, 1), (0, 1), (1, 1)],
]


def check(i, j, elves):
    for d in range(len(incs)):
        n = neighbors[d]
        for x, y in n:
            if (i + x, j + y) in elves:
                return True
    return False


def check_dir(i, j, d, elves):
    n = neighbors[d]
    for x, y in n:
        if (i + x, j + y) in elves:
            return False
    return True


def print_b(elves):
    space = list(elves)
    mini, minj = space[0]
    maxi, maxj = space[0]

    for i, j in space:
        mini, minj, maxi, maxj = min(mini, i), min(minj, j), max(maxi, i), max(maxj, j)

    for i in range(mini, maxi+1):
        line = ''
        for j in range(minj, maxj+1):
            line += '#' if (i,j) in elves else '.'
        line += '\n'
    return line

def pos(a, b):
    x1, y1 = a
    x2, y2 = b
    if x1 == x2:
        return y1 - y2
    return x1 - x2



def part1(elves, rounds):
    dir = deque([0, 1, 2, 3])
    changed = True
    round = 0

    while True:
        if rounds is None:
            if not changed:
                break
        else:
            if round >= rounds:
                break

        round += 1
        proposed = {}  # pos, elf
        unmoved = set()

        # phase 1
        for i, j in sorted(elves, key=cmp_to_key(pos)):
            if check(i, j, elves):
                for d in dir:
                    ni, nj = incs[d]
                    new_pos = i+ni, j+nj
                    if check_dir(i, j, d, elves):
                        proposed[new_pos] = proposed.get(new_pos, []) + [(i,j)]
                        break
                else:
                     unmoved.add((i,j))
            else:
                unmoved.add((i,j))

        # phase 2
        new_elves = set()
        for new_pos, cands in proposed.items():
            if len(cands) == 1:
                new_elves.add(new_pos)
            else:
                for old_pos in cands:
                    new_elves.add(old_pos)

        new_elves.update(unmoved)
        changed = len(elves - new_elves) != 0

        elves = new_elves
        dir.rotate(-1)


    space = list(elves)
    mini, minj = space[0]
    maxi, maxj = space[0]

    for i,j in space:
        mini, minj, maxi, maxj = min(mini, i), min(minj, j), max(maxi, i), max(maxj, j)

    return abs(maxi-mini+1) * abs(maxj-minj+1) - len(elves), round


def part2(l):
    pass


elves = set()
i = 0
while True:
    l = f.readline()
    if not l:
        break
    elves.update(set([(i, j) for j in range(len(l)) if l[j] == '#']))
    i += 1

print("part1: ", part1(elves, 10))
print("part2: ", part1(elves, None))
