import re
import copy

# f = open('data/day17-sample.txt', 'r')
f = open('data/day17-final.txt', 'r')


def part1(box):
    tl, br = box
    miny = tl[1]
    maxy = br[1]

    # p(i) = v0 * i - ((i-1)*i / 2)
    # v(t) = v0 - t
    # v(t) = 0 -> v0 = t => max_t

    max_v = 0
    for v0 in range(0, 1000):
        v = v0
        p = 0
        for i in range(1000):
            p = p + v
            v -= 1
            if miny <= p <= maxy:
                max_v = max(max_v, v0)
                break

    max_t = max_v
    max_p = int(max_v * max_t - ((max_t-1)*max_t / 2))
    return max_p


def part2(box):
    tl, br = box
    minx = tl[0]
    maxx = br[0]
    miny = tl[1]
    maxy = br[1]

    valid = set()
    drag = 1 if box[0][0] < 0 else -1
    clip = max if drag < 0 else min
    n = 500
    for vx in range(n):
        for vy in range(-n, n):
            p = (0, 0)
            v = (vx, vy)
            for t in range(1000):
                p = (p[0]+v[0], p[1]+v[1])
                v = (clip(0, v[0]+drag), v[1]-1)
                if abs(p[0]) > abs(maxx):
                    break

                if minx <= p[0] <= maxx and miny <= p[1] <= maxy:
                    valid.add((vx, vy))
                    break

    return len(valid)

input = re.match(r'target area: x=([-]?[0-9]*)\.\.([-]?[0-9]*), y=([-]?[0-9]*)\.\.([-]?[0-9]*)', f.readline())
box = ((int(input.group(1)), int(input.group(3))), (int(input.group(2)), int(input.group(4))))

print('part1: ', part1(copy.deepcopy(box)))
print('part2: ', part2(copy.deepcopy(box)))
