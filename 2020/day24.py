import re

# f = open('data/day24-sample.txt', 'r')
f = open('data/day24-final.txt', 'r')

seq = [l.strip() for l in f]

neighbours = {
    'e': (-1, 0),
    'se': (0, -1),
    'sw': (1, -1),
    'w': (1, 0),
    'nw': (0, 1),
    'ne': (-1, 1),
}


def part1(seq):
    tiles = {}
    for l in seq:
        # apply all the instructions
        pos = (0, 0)
        for i in re.findall(r'(w|e|se|sw|ne|nw|ne)', l):
           pos = pos[0]+neighbours[i][0], pos[1]+neighbours[i][1]

        # record the result in tiles
        tiles[pos] = not tiles.get(pos, False)

    return tiles, sum([1 for v in tiles.values() if v])


def part2(tiles):
    blacks = set([k for k, v in tiles.items() if v])

    for i in range(100):
        whites = {}
        next = set()
        for b in blacks:
            count = 0
            for inc in neighbours.values():
                n = b[0]+inc[0], b[1]+inc[1]
                if n not in blacks:
                    whites[n] = whites.get(n, 0) + 1
                else:
                    count += 1
            if count != 0 and count <= 2:
                next.add(b)

        for k in [k for k, w in whites.items() if w == 2]:
            next.add(k)
        blacks = next

    return len(blacks)


print('part1: ', part1(seq)[1])
print('part2: ', part2(part1(seq)[0]))