import re

# f = open('data/day21-sample.txt', 'r')
f = open('data/day21-final.txt', 'r')


def part1(current):
    if isinstance(current, int):
        return current

    op1, op, op2 = current
    if op == '+':
        return part1(operations[op1]) + part1(operations[op2])
    if op == '-':
        return part1(operations[op1]) - part1(operations[op2])
    if op == '*':
        return part1(operations[op1]) * part1(operations[op2])
    if op == '/':
        return part1(operations[op1]) / part1(operations[op2])


def find(key, current):
    if current == key:
        return True

    current = operations[current]
    if isinstance(current, int):
        return False

    op1, _, op2 = current
    if op1 == key or op2 == key:
        return True

    return find(key, op1) or find(key, op2)


def resolve(target, tree):
    current = operations[tree]
    if isinstance(current, int):
        return target

    op1, op, op2 = current

    left = find('humn', op1)
    value = part1(operations[op2]) if left else part1(operations[op1])
    next = op1 if left else op2

    if op == '+':
        return resolve(target - value, next)
    if op == '*':
        return resolve(target / value, next)
    if op == '-':
        return resolve((target + value) if left else (value - target), next)
    if op == '/':
        return resolve((target * value) if left else (value / target), next)


def part2(root):
    op1, op, op2 = root

    left = find('humn', op1)
    value = part1(operations[op2]) if left else part1(operations[op1])

    return resolve(value, op1 if left else op2)


lines = [l.strip() for l in f]
operations = {}
for l in lines:
    parts = l.split(':')
    name = parts[0]
    op = parts[1].strip()
    if '+' in op or '*' in op or '/' in op or '-' in op:
        operations[name] = tuple(op.split(' '))
    else:
        operations[name] = int(op)

print("part1: ", part1(operations['root']))
print("part2: ", part2(operations['root']))
