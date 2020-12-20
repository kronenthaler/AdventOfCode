import re
import math


f = open('data/day20-sample.txt', 'r')
# f = open('data/day20-final.txt', 'r')

tiles = {}
while True:
    l = f.readline().strip()
    id = re.match('Tile (.*):', l)
    if id is None or id == '':
        break
    id = id.group(1)
    left = ''
    right = ''
    top = ''
    bottom = ''
    for i in range(0, 10):
        l = f.readline().strip()
        if i == 0:
            top = int(l.replace('.', '0').replace('#', '1'), 2)
        elif i == 9:
            bottom = int(l.replace('.', '0').replace('#', '1'), 2)
        left += l[0]
        right += l[9]

    f.readline()  #\n
    tiles[id] = [(top,
                  int(right.replace('.', '0').replace('#', '1'), 2),
                  bottom,
                  int(left.replace('.', '0').replace('#', '1'), 2))]


def rotate(tiles):
    for k, tile in tiles.items():
        (t, l, b, r) = tile[0]
        tf = int("{0:b}".format(t)[::-1], 2)
        bf = int("{0:b}".format(b)[::-1], 2)
        lf = int("{0:b}".format(l)[::-1], 2)
        rf = int("{0:b}".format(r)[::-1], 2)

        # normal
        tile.append((l, b, r, t))
        tile.append((b, r, t, l))
        tile.append((r, t, l, b))
        # v-flip
        tile.append((tf, l, bf, r))
        tile.append((l, bf, r, tf))
        tile.append((bf, r, tf, l))
        tile.append((r, tf, l, bf))
        # h-flip
        tile.append((t, lf, b, rf))
        tile.append((lf, b, rf, t))
        tile.append((b, rf, t, lf))
        tile.append((rf, t, lf, b))
        # double flip
        tile.append((tf, lf, bf, rf))
        tile.append((lf, bf, rf, tf))
        tile.append((bf, rf, tf, lf))
        tile.append((rf, tf, lf, bf))

    return tiles

def neighbours(i,j,n):
    neighbours = (True, True, True, True)  # default
    if i == 0 and j == 0:
        neighbours = (False, False, True, True)
    elif i == 0 and j == n - 1:
        neighbours = (False, True, True, False)
    elif i == n - 1 and j == 0:
        neighbours = (True, False, False, True)
    elif i == n - 1 and j == n - 1:
        neighbours = (True, True, False, False)
    elif i == 0:
        neighbours = (False, True, True, True)
    elif i == n - 1:
        neighbours = (True, True, False, True)
    elif j == 0:
        neighbours = (True, False, True, True)
    elif j == n - 1:
        neighbours = (True, True, True, False)
    return neighbours


def bt(G, tile, i, j, n, visited, table):
    if i >= n and j >= n:
        return

    next = neighbours(i, j, n)
    for g, e in G:
        for o in tiles[g]:
            for node in e:




def part1(tiles):
    contacts = {}

    for id, t in tiles.items():
        for id1, t1 in tiles.items():
            if t == t1: continue
            for i in range(0, t.__len__()):
                o1 = t[i]
                for j in range(0, t1.__len__()):
                    o2 = t1[j]
                    if o1[0] == o2[2] or o1[2] == o2[0] or o1[1] == o2[3] or o1[3] == o1[1]:
                        contacts[id] = contacts.get(id, set()) | set([id1]) #, i, j, o1[0] == o2[2], o1[2] == o2[0], o1[1] == o2[3], o1[3] == o1[1]
                        contacts[id1] = contacts.get(id1, set()) | set([id]) #, j, i, o2[0] == o1[2], o2[2] == o1[0], o2[1] == o1[3], o2[3] == o1[1]

    n = int(math.sqrt(tiles.__len__()))
    table = list([[''*n] for _ in range(0, n)])
    bt(contacts, tiles, 0, 0, n, set(), table)
    print(table)

print('part1:', part1(rotate(tiles)))


