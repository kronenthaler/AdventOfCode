import re

# f = open('data/day07-sample.txt', 'r')
f = open('data/day07-final.txt', 'r')


def bt(target, accum, l, funcs):
    if len(l) == 0:
        return accum == target

    for f in funcs:
        if bt(target, f(accum, l[0]), l[1:], funcs):
            return True

    return False


def solve(l, ops):
    return sum([target for target, operands in l if bt(target, operands[0], operands[1:], ops)])


lines = [(int(t), [int(x) for x in v.strip().split(' ')]) for t, v in [tuple(l.strip().split(':')) for l in f]]

part1_ops = [lambda x, y: x + y, lambda x, y: x * y]
part2_ops = [lambda x, y: x+y, lambda x,y: x*y, lambda x,y: int(str(x)+str(y))]

print("part1: ", solve(lines, part1_ops))
print("part2: ", solve(lines, part2_ops))
