import re
from itertools import chain


# f = open('data/day15-sample.txt', 'r')
f = open('data/day15-final.txt', 'r')


def HASH(s, salt):
    for c in s:
        salt += ord(c)
        salt *= 17
        salt %= 256
    return salt


def part1(inst):
    return sum([HASH(i, 0) for i in inst])


def apply(op, boxes):
    label, strenght = op
    index = HASH(label, 0)
    box = boxes[index]

    if strenght is None: # remove
        for index, (l, s) in enumerate(box.copy()):
            if l == label:
                box.pop(index)
                break
    else:
        for index, (l, s) in enumerate(box):
            if l == label:
                box[index] = (label, strenght)
                break
        else:
            box.append((label, strenght))


def focus_power(boxes):
    return sum([(index + 1) * (slot + 1) * int(strength)
                for index, values in enumerate(boxes)
                for slot, (_, strength) in enumerate(values)])


def part2(inst):
    boxes = [[] for i in range(257)]
    for i in inst:
        # split into label + op
        i = (i[0:-1], None) if "-" in i else tuple(i.split("="))
        apply(i, boxes)

    return focus_power(boxes)


lines = list(chain.from_iterable([l.strip().split(',') for l in f]))

print("part1: ", part1(lines))
print("part2: ", part2(lines))
