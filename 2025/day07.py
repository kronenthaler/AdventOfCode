from google.api_core.retry.retry_unary_async import retry_target

from utils import *

# f = open('data/day07-sample.txt', 'r')
f = open('data/day07-final.txt', 'r')

lines = [l.strip() for l in f]


def part1(l):
    sx, sy = [(i, r.index('S')) for i, r in enumerate(l) if 'S' in r][0]
    queue = [(sx+1, sy)]
    visited = set()
    splits = set()
    while queue:
        (i, j) = queue.pop(0)

        if l[i][j] != '^' and i+1 < len(l):
            queue.append((i+1, j))
        elif l[i][j] == '^' and i+1 < len(l):
            splits.add((i, j))
            if j-1 >= 0 and (i, j-1) not in visited:
                visited.add((i, j-1))
                queue.append((i, j-1))
            if j+1 < len(l[0]) and (i, j+1) not in visited:
                visited.add((i, j+1))
                queue.append((i, j+1))
    return len(splits)


@functools.cache
def doit(i, j):
    if lines[i][j] != '^':
        if i + 1 >= len(lines):
            return 1
        else:
            return doit(i + 1, j)

    if j - 1 >= 0:
        a = doit(i, j - 1)
    if j + 1 < len(lines[0]):
        b = doit(i, j + 1)

    return a + b


def part2(l):
    sx, sy = [(i, r.index('S')) for i, r in enumerate(l) if 'S' in r][0]
    result = doit(sx, sy)
    return result


print("part1: ", part1(lines))
print("part2: ", part2(lines))
