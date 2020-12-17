
# f = open('data/day17-sample.txt', 'r')
f = open('data/day17-final.txt', 'r')

map = [list(l.strip()) for l in f]

steps = [-1, 0, 1]
neighbours = [(x, y, z, 0) for x in steps for y in steps for z in steps if x != 0 or y != 0 or z != 0]
neighbours4d = [(x, y, z, w) for x in steps for y in steps for z in steps for w in steps if x != 0 or y != 0 or z != 0 or w != 0]


def part1(map, rounds, neighbours):
    active = set([(i, j, 0, 0) for i in range(0, map.__len__()) for j in range(0, map[i].__len__()) if map[i][j] == '#'])

    for c in range(0, rounds):
        lower = min(min(*pos) for pos in active)
        higher = max(max(*pos) for pos in active)

        temp = set()
        for w in range(lower - 1, higher + 2):
            for z in range(lower - 1, higher + 2):
                for y in range(lower - 1, higher + 2):
                    for x in range(lower - 1, higher + 2):
                        count = sum([1 for o in neighbours if (x + o[0], y + o[1], z + o[2], w + o[3]) in active])
                        if count == 3 or (count == 2 and (x, y, z, w) in active):
                            temp.add((x, y, z, w))
        active = temp
    return active.__len__()


print('part1: ', part1(map, 6, neighbours))
print('part2: ', part1(map, 6, neighbours4d))
