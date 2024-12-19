from utils import *

# f = open('data/day18-sample.txt', 'r'); N=7; iterations=12
f = open('data/day18-final.txt', 'r'); N=71; iterations=1024

lines = [tuple(map(int, l.strip().split(','))) for l in f]


def valid(t, min=(0, 0), max=(N, N)):
    return all(map(lambda m, t, M: m <= t < M, min, t, max))


def bfs(bytes, iterations, target):
    start = (0, 0)
    queue = [(start, 0, [])]

    visited = set()
    while len(queue):
        current, t, path = queue.pop(0)

        if current == target:
            return t

        for step in Steps2D:
            new = add(current, step)
            if valid(new) and new not in bytes[0: iterations] and new not in visited:
                queue.append((new, t + 1, path + [new]))
                visited.add(new)
    return -1


def part1(bytes, iterations, target):
    return bfs(bytes, iterations, target)


def part2(bytes, target):
    lo = 0
    hi = len(bytes)
    while lo < hi:
        mid = (hi + lo) // 2
        result = bfs(bytes, mid, target)
        if result < 0:
            hi = mid
        else:
            lo = mid + 1

    return f'{bytes[lo-1][0]},{bytes[lo-1][1]}'


print("part1: ", part1(lines, iterations, (N-1, N-1)))
print("part2: ", part2(lines, (N-1, N-1)))
