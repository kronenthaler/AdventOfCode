import re
import copy
import os
from functools import reduce

f = open('data/day16-sample.txt', 'r')
# f = open('data/day16-final.txt', 'r')


def literal(s, v, t, i):  # -> Tree, index
    value = ""
    d = '-'
    while d[0] != '0':
        d = s[i:(i := i+5)]
        value += d[1:]
    return Tree(v, t, int(value, 2)), i


def operator_count(s, v, t, l, index):
    values = []
    for n in range(l):
        node, index = packet(s, index)
        values.append(node)
    return Tree(v, t, f'c{l}', children=values), index


def operator_bits(s, v, t, l, index):  # [value], index
    values = []
    n = index + l
    while index < n:
        node, index = packet(s, index)
        values.append(node)
    return Tree(v, t, f'b{l}', children=values), index


def packet(s, i):  # tree, index
    v = int(s[i:(i := i+3)], 2)
    t = int(s[i:(i := i+3)], 2)

    if t == 4:
        return literal(s, v, t, i)

    bits = "".join(s[i:(i:=i+1)]) == "0"
    l = int(s[i:(i := i+15)] if bits else s[i:(i := i+11)], 2)
    return operator_bits(s, v, t, l, i) if bits else operator_count(s, v, t, l, i)


class Tree:
    def __init__(self, version, type, root, children = None):
        self.version = version
        self.type = type
        self.root = root
        self.children = children if children else []

    def versions(self):
        return self.version + sum([t.versions() for t in self.children])

    @staticmethod
    def eval(tree):
        if tree.type == 4:
            return tree.root

        if tree.type == 0:
            return sum(map(Tree.eval, tree.children))

        if tree.type == 1:
            return reduce((lambda x, y: x * y), map(Tree.eval, tree.children))

        if tree.type == 2:
            return min(map(Tree.eval, tree.children))

        if tree.type == 3:
            return max(map(Tree.eval, tree.children))

        if tree.type == 5:
            return 1 if Tree.eval(tree.children[0]) > Tree.eval(tree.children[1]) else 0

        if tree.type == 6:
            return 1 if Tree.eval(tree.children[0]) < Tree.eval(tree.children[1]) else 0

        if tree.type == 7:
            return 1 if Tree.eval(tree.children[0]) == Tree.eval(tree.children[1]) else 0


for line in [l.strip() for l in f]:
    print(line)
    tree, _ = packet(f'{int(line, 16):0>{len(line)*4}b}', 0)

    print('part1: ', tree.versions())
    print('part2: ', Tree.eval(tree))
    print()