import re
import copy

# f = open('data/day14-sample.txt', 'r')
f = open('data/day14-final.txt', 'r')


def print_map(map):
    [print("".join(r)) for r in map]
    print()


def roll(map, direction):
    di, dj = direction

    rows = range(len(map))
    if di > 0:
        rows = range(len(map)-1, -1, -1)

    columns = range(len(map[0]))
    if dj > 0:
        columns = range(len(map[0])-1, -1, -1)

    def process(i, j):
        if map[i][j] == '#' or map[i][j] == '.':
            return

        pi, pj = i + di, j + dj
        while 0 <= pi < len(map) and 0 <= pj < len(map[0]) and map[pi][pj] == '.':
            x = map[pi - di][pj - dj]
            map[pi - di][pj - dj] = '.'
            map[pi][pj] = x
            pi += di
            pj += dj

    # need to traverse right to left or bottom to top if di or dj is positive
    if di != 0:
        [process(i, j) for i in rows for j in columns]
    else:
        [process(i, j) for j in columns for i in rows]


def calc(new_map):
    total = 0
    for i, r in enumerate(new_map):
        count = r.count('O')
        total += count * (len(new_map) - i)
    return total


def part1(map):
    new_map = copy.deepcopy(map)
    roll(new_map, (-1, 0))
    return calc(new_map)


def part2(map):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    new_map = copy.deepcopy(map)

    # detect a loop
    key = "".join(["".join(r) for r in new_map])
    previous = {key: 0}
    for t in range(1_000_000_000):
        for d in directions:
            roll(new_map, d)

        key = "".join(["".join(r) for r in new_map])
        if key in previous:
            break
        else:
            previous[key] = t

    start_loop = previous[key]
    loop_size = t - start_loop
    index = (1_000_000_000 - start_loop - 1) % loop_size

    map_key = next(k for k, v in previous.items() if v == index + start_loop)

    # split the key into a map for the final calculation
    chunk_size = len(map)
    return calc([map_key[i:i + chunk_size] for i in range(0, len(map_key), chunk_size)])


lines = [list(l.strip()) for l in f]

print("part1: ", part1(lines))
print("part2: ", part2(lines))
