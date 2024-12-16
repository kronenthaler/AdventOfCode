from utils import *

# f = open('data/day14-sample.txt', 'r'); M = 11; N = 7
f = open('data/day14-final.txt', 'r'); M = 101; N = 103

lines = [l.strip() for l in f]
lines = [tuple(map(int, re.findall(r'p=([-0-9]*),([-0-9]*) v=([-0-9]*),([-0-9]*)', l)[0])) for l in lines]
lines = [((x, y), (vx, vy)) for x, y, vx, vy in lines]
# 8158 too low | 18561 too high, 18561 not, 18562?

def detect(l):
    flat = ''
    points = set([p for p, v in l])
    for i in range(N):
        for j in range(M):
            flat += '*' if (j, i) in points else '.'
    if '************' in flat:
        return True, points
    return False, points


def _print(t, points):
    print('run: ', t)
    for i in range(N):
        for j in range(M):
            print('*' if (j, i) in points else '.', end='')
        print()
    print('-----------------\n')


def part1(l, times, display=False):
    print(len(l))
    for t in range(1, times+1):
        new_pos = []
        for (x, y), (vx, vy) in l:
            nx = (x + vx) % M
            ny = (y + vy) % N
            new_pos.append(((nx, ny), (vx, vy)))
        l = new_pos

    results = [[], [], [], []]
    quads = [
        ((0, 0), (M//2, N//2)),
        ((0, (N//2)+1), (M//2, N)),
        (((M//2)+1, 0), (M, N//2)),
        (((M//2)+1, (N//2)+1), (M, N))
    ]
    for (x, y), _ in l:
        for i, ((mx, my), (Mx, My)) in enumerate(quads):
            if mx <= x < Mx and my <= y < My:
                results[i].append((x, y))
                break
    return math.prod([len(r) for r in results])


def part2(l, times):
    for t in range(1, times+1):
        new_pos = []
        for (x, y), (vx, vy) in l:
            nx = (x + vx) % M
            ny = (y + vy) % N
            new_pos.append(((nx, ny), (vx, vy)))
        l = new_pos

        value, points = detect(l)
        if value:
            _print(t, points)
            return t
    return -1

print("part1: ", part1(lines, 100))
print("part2: ", part2(lines, 20000))
