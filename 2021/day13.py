import re

# f = open('data/day13-sample.txt', 'r')
f = open('data/day13-final.txt', 'r')


def part1(ps, ins):
    points = set(ps)
    for fx, fy in ins:
        if fx != 0:
            fold = [p for p in points if p[0] > fx]
            [points.remove(p) for p in fold]
            points.update([(fx-(x-fx), y) for x, y in fold])
        else:
            fold = [p for p in points if p[1] > fy]
            [points.remove(p) for p in fold]
            points.update([(x, fy-(y-fy)) for x, y in fold])
    return points

def part2(ps, ins):
    points = part1(ps, ins)
    maxX = max([x for x, _ in points]) + 1
    maxY = max([y for _, y in points]) + 1
    board = []
    for y in range(maxY):
        board.append([])
        for x in range(maxX):
            board[y].append(' ')

    for x, y in points:
        board[y][x] = '#'

    line = "\n"
    for y in range(maxY):
        for x in range(maxX):
            line += str(board[y][x])
        line+='\n'
    return line


points = []
for l in f:
    if l.strip() == '':
        break
    t = l.split(',')
    points.append((int(t[0]), int(t[1])))

instructions = []
for l in f:
    groups = re.match('fold along ([xy])=([0-9]*)', l)
    x_or_y = groups[1] == 'x'
    value = int(groups[2])
    instructions.append((value if x_or_y else 0, value if not x_or_y else 0))


print('part1: ', len(part1(points.copy(), [instructions[0]])))
print('part2: ', part2(points.copy(), instructions))