from utils import *


# f = open('data/day13-sample.txt', 'r')
f = open('data/day13-final.txt', 'r')

lines = [l.strip() for l in f if len(l.strip()) != 0]
group = list(zip(*(iter(lines),) * 3))
machines = [(
    tuple(map(int, re.findall(r'Button .: X\+([0-9]+), Y\+([0-9]+)', a)[0])),
    tuple(map(int, re.findall(r'Button .: X\+([0-9]+), Y\+([0-9]+)', b)[0])),
    tuple(map(int, re.findall(r'Prize: X=([0-9]+), Y=([0-9]+)', p)[0]))) for a,b,p in group]


def equation(t, a, b, limit=math.inf, offset=0):
    ax, ay = a
    bx, by = b
    x, y = add(t, (offset, offset))

    den = ax * by - ay * bx
    if den == 0:
        return 0

    gamma = int((ax * y - ay * x) / den)
    alpha = int((x - bx * gamma) / ax)

    if alpha <= limit and gamma <= limit and \
            (x == ax * alpha + bx * gamma) and \
            (y == ay * alpha + by * gamma):
        return alpha * 3 + gamma
    return 0


def part1(machines):
    return sum([equation(t, a, b, limit=100) for (a, b, t) in machines])


def part2(machines):
    return sum([equation(t, a, b, offset=10000000000000) for (a, b, t) in machines])


print("part1: ", part1(machines))
print("part2: ", part2(machines))
