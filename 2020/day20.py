import math
import re

# data = open('data/day20-sample.txt', 'r').read()
data = open('data/day20-final.txt', 'r').read()

P = {int(p[5:9]): p[11:] for p in data.split('\n\n')}
edge = lambda p, i: [p[:10], p[9::11], p[-10:], p[0::11]][i]


def transform(p):
    for _ in range(4):
        yield p
        yield '\n'.join(l[::-1] for l in p.split('\n'))  # flip
        p = '\n'.join(''.join(l[::-1]) for l in zip(*p.split('\n')))  # rotate


# greedy calculation
def part1(board, orientations):
    corners = set()
    for k, v in board.items():
        edges = set()
        for _, o in board.items():
            if o == v: continue
            for ot in orientations(o):
                for i in range(4):
                    e1 = edge(ot, (i + 2) % 4)
                    e2 = edge(v, i)
                    if e1 == e2:
                        edges.add(ot)
        if len(edges) == 2:
            corners.add(k)
    return math.prod(list(corners))

def bt(board, index, n, order, table):
    if len(order) == len(board):
        return order

    for id, t in board.items():
        if id in order: continue
        i = index // n
        j = index % n

        for o in transform(t):
            first = i == 0 or edge(o, 0) == edge(table[i-1][j], 2)
            second = j == 0 or edge(o, 3) == edge(table[i][j-1], 1)
            if first and second:
                table[i][j] = o
                if result := bt(board, index+1, n, order + [id], table):
                    return result
                table[i][j] = ''
    return None

def part2(board, orientations):
    # need to bt to place all tiles in the right position
    n = int(len(board) ** 0.5)
    m = 10
    table = [['' for _ in range(n)] for _ in range(n)]
    order = bt(board, 0, n, [], table)

    map = [''] * n * (m-2)
    for i in range(n):
        for j in range(n):
            # convert the strings into matrix
            t = [list(l) for l in table[i][j].split('\n')]
            # remove edges
            table[i][j] = list([l[1:m-1] for l in t[1:m-1]])

    for j in range(n):
        t = 0
        for i in range(n):
            for k in range(len(table[i][j])):
                joined = ''.join(table[i][j][k])
                map[t] = map[t] + joined
                t += 1

    monster = (".{}(..................#.)", "(#....##....##....###)", ".{}(.#..#..#..#..#..#...)")
    for t in transform('\n'.join(map)):
        count = 0
        lines = t.split('\n')
        for i in range(len(lines)):
            l = lines[i]

            for match in re.finditer(monster[1], l):
                index = match.start(1)
                up = i - 1 >= 0 and re.match(monster[0].format("{" + str(index) + "}"), lines[i - 1]) is not None
                down = i + 1 < len(lines) and re.match(monster[2].format("{" + str(index) + "}"), lines[i + 1]) is not None

                if up and down:
                    count += 1
        if count != 0:
            hashes = sum([1 for c in '\n'.join(map) if c == '#'])
            return hashes - count*15
    return order[0] * order[n-1] * order[(n-1) * n] * order[((n-1) * n) + (n-1)]


print('part1:', part1(P, transform))
print('part2:', part2(P, transform))


