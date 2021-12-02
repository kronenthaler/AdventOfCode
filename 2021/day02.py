# f = open('data/day02-sample.txt', 'r')
f = open('data/day02-final.txt', 'r')


def part1(ins, pos):
    moves = {
        'forward':  (1,  0),
        'down':     (0,  1),
        'up':       (0, -1)
    }

    for i in ins:
        pos = (pos[0] + moves[i[0]][0]*i[1], pos[1] + moves[i[0]][1]*i[1])
    return pos[0]*pos[1]


def part2(ins, pos):
    moves = {
        'forward': lambda x, y: (x[1], x[1]*y[2], 0),
        'down': lambda x, y: (0, 0, x[1]),
        'up': lambda x, y: (0, 0, -x[1])
    }

    for i in ins:
        pos = tuple(map(sum, zip(pos, moves[i[0]](i, pos))))

    return pos[0]*pos[1]


input = [(x.split(' ')[0].strip(), int(x.split(' ')[1].strip())) for x in f]

print("part1: ", part1(input, (0, 0)))
print("part2: ", part2(input, (0, 0, 0)))