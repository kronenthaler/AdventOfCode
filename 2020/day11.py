# f = open('day11-sample.txt', 'r')
f = open('day11-final.txt', 'r')

content = [l.strip() for l in f]

sx = [+0, +0, +1, +1, +1, -1, -1, -1]
sy = [-1, +1, -1, +0, +1, -1, +0, +1]


def part1(content, f, limit):
    changes = True

    while changes:
        changes = False
        n = content.__len__()
        m = content[0].__len__()
        buffer = [''] * n

        for y in range(0, n):
            for x in range(0, m):
                occupied = f(content, x, y, n, m)

                if content[y][x] == 'L' and occupied == 0:
                    changes = True
                    buffer[y] += '#'
                elif content[y][x] == '#' and occupied >= limit:
                    changes = True
                    buffer[y] += 'L'
                else:
                    buffer[y] += content[y][x]
        # print('')
        # [print(x) for x in buffer]
        content = buffer

    free = 0
    for l in content:
        free += sum([1 for c in l if c == '#'])

    return free

def neighbours(content, x, y, n, m):
    occupied = 0
    for k in range(0, 8):
        i = sx[k]
        j = sy[k]
        if 0 <= y + j < n and 0 <= x + i < m and content[y + j][x + i] == '#':
            occupied += 1
    return occupied

def neighbours2(content, x, y, n, m):
    occupied = 0
    for k in range(0, 8):
        i = sx[k]
        j = sy[k]
        while 0 <= y + j < n and 0 <= x + i < m and content[y + j][x + i] == '.':
            i += sx[k]
            j += sy[k]

        if 0 <= y + j < n and 0 <= x + i < m and content[y + j][x + i] == '#':
            occupied += 1
    return occupied

print("part1: ", part1(content, neighbours, 4))
print("part2: ", part1(content, neighbours2, 5))