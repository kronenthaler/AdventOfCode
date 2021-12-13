import re

# f = open('data/day13-sample.txt', 'r')
f = open('data/day13-final.txt', 'r')


def part1(ps, ins):
    points = set(ps)
    for fx, fy in ins:
        fold = [p for p in points if (fx != 0 and p[0] > fx) or (fy != 0 and p[1] > fy)]
        [points.remove(p) for p in fold]
        points.update([(2*fx-x, y) if fx != 0 else (x, 2*fy-y) for x, y in fold])
    return points


def part2(ps, ins):
    points = part1(ps, ins)
    maxX = max([x for x, _ in points]) + 1
    maxY = max([y for _, y in points]) + 1
    board = [[' ' for x in range(maxX)] for y in range(maxY)]
    for x, y in points:
        board[y][x] = '░'
    return "\n"+"\n".join(["".join([str(board[y][x]) for x in range(maxX)]) for y in range(maxY)])


points = []
for l in f:
    if l.strip() == '':
        break
    points.append(tuple(list(map(int, l.strip().split(',')))))

instructions = []
for l in f:
    groups = re.match('fold along ([xy])=([0-9]*)', l)
    x_or_y, value = groups[1] == 'x', int(groups[2])
    instructions.append((value if x_or_y else 0, value if not x_or_y else 0))


print('part1: ', len(part1(points.copy(), [instructions[0]])))
print('part2: ', part2(points.copy(), instructions))