import re

# f = open('data/day09-sample.txt', 'r')
f = open('data/day09-final.txt', 'r') # 13676 failed: too high

steps_head = {'U': (1, 0), 'L': (0, -1), 'D': (-1, 0), 'R': (0, 1)}
neighbours = [(0, 0), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]


def is_neighbour(hx, hy, tx, ty):
    for nx, ny in neighbours:
        if tx + nx == hx and ty + ny == hy:
            return True
    return False


def calculate_move(hx, hy, tx, ty):
    return (hx - tx) / abs(hx - tx) if hx != tx else 0, (hy - ty) / abs(hy - ty) if hy != ty else 0


def move(h, t, visited):
    if not is_neighbour(*h, *t):
        incx, incy = calculate_move(*h, *t)
        t = (t[0] + incx, t[1] + incy)
        visited.add(t)
    return t


def part2(moves, n):
    rope = [(0, 0)] * n
    visited = [set(rope[i]) for i in range(0, n)]

    for d, inc in moves:
        for i in range(0, inc):
            rope[0] = rope[0][0] + steps_head[d][0], rope[0][1] + steps_head[d][1]
            for r in range(0, len(rope)-1):
                rope[r+1] = move(rope[r], rope[r+1], visited[r+1])

    return len(visited[-1])


lines = [(l.strip().split(' ')[0], int(l.strip().split(' ')[1]))  for l in f]

print("part1: ", part2(lines, 2))
print("part2: ", part2(lines, 10))
