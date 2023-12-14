import re
import copy

# f = open('data/day14-sample.txt', 'r')
f = open('data/day14-final.txt', 'r')


def print_map(map):
    [print("".join(r)) for r in map]
    print()


def roll(map, direction):
    def process(i, j):
        if map[i][j] == '#' or map[i][j] == '.':
            return

        pi, pj = i + di, j + dj
        while 0 <= pi < len(map) and 0 <= pj < len(map[0]) and map[pi][pj] == '.':
            x = map[pi - di][pj - dj]
            map[pi - di][pj - dj] = '.'
            map[pi][pj] = x
            pi, pj = pi+di, pj+dj

    di, dj = direction
    rows = range(len(map) - 1, -1, -1) if di > 0 else range(len(map))
    columns = range(len(map[0]) - 1, -1, -1) if dj > 0 else range(len(map[0]))

    # need to traverse right to left or bottom to top if di or dj is positive
    if di != 0:
        [process(i, j) for i in rows for j in columns]
    else:
        [process(i, j) for j in columns for i in rows]
    return map


def calc(new_map):
    return sum([r.count('O') * (len(new_map) - i) for i, r in enumerate(new_map)])


def part1(map):
    return calc(roll(copy.deepcopy(map), (-1, 0)))


def part2(map):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    new_map = copy.deepcopy(map)

    # detect a loop
    key = "".join(["".join(r) for r in new_map])
    previous = {key: 0}
    for t in range(1_000_000_000):
        [roll(new_map, d) for d in directions]

        key = "".join(["".join(r) for r in new_map])
        if key in previous:
            break
        else:
            previous[key] = t

    start_loop = previous[key]
    index = start_loop + ((1_000_000_000 - start_loop - 1) % (t - start_loop))

    map_key = next(k for k, v in previous.items() if v == index)

    # split the key into a map for the final calculation
    chunk_size = len(map)
    return calc([map_key[i:i + chunk_size] for i in range(0, len(map_key), chunk_size)])


lines = [list(l.strip()) for l in f]

print("part1: ", part1(lines))
print("part2: ", part2(lines))
