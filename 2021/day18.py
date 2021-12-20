import functools
import re
import copy
import math

# f = open('data/day18-sample.txt', 'r')
f = open('data/day18-final.txt', 'r')


class Tree:
    @staticmethod
    def parse(input, index=0):  # -> Tree
        valid = '0123456789'
        if input[index] == '[':
            left, index = Tree.parse(input, index+1)
            right, index = Tree.parse(input, index)

            if index < len(input) and input[index] not in valid:
                index += 1
            return Pair(left, right), index

        start = index
        while input[index] in valid:
            index += 1

        value = int(input[start:index])
        return Value(value), index+1

    def add(self, tree):
        return Pair(self, tree).reduce()

    def reduce(self):
        change = True
        while change:
            change = False
            linear = self.inorder()
            explode = self.find_pair(0)
            new = None
            if explode is not None:
                parent = explode.parent
                change = True
                index = linear.index(parent)
                left = None
                for i in range(index, -1, -1):
                    n = linear[i]
                    if isinstance(n, Value) and n.parent != explode:
                        left = linear[i]
                        break
                if left is not None:
                    left.value += explode.left.value

                right = None
                for i in range(index, len(linear)):
                    n = linear[i]
                    if isinstance(n, Value) and n.parent != explode:
                        right = linear[i]
                        break
                if right is not None:
                    right.value += explode.right.value

                new = Value(0)
                target = explode
            else:
                for v in linear:
                    if isinstance(v, Value) and v.value >= 10:
                        change = True
                        parent = v.parent
                        new = Pair(Value(int(v.value / 2)), Value(int(math.ceil(v.value / 2))))
                        target = v
                        break
            if change:
                new.parent = parent
                if parent.left == target:
                    parent.left = new
                else:
                    parent.right = new
            pass
        return self

    def find_pair(self, current_depth=0):
        if current_depth == 4:
            return self
        from_left = self.left.find_pair(current_depth + 1)
        if from_left is not None:
            return from_left
        from_right = self.right.find_pair(current_depth + 1)
        if from_right is not None:
            return from_right
        return None

    def inorder(self):
        return self.left.inorder() + [self] + self.right.inorder()

class Value(Tree):
    def __init__(self, v):
        self.parent = None
        self.value = v

    def __repr__(self):
        return str(self.value)

    def mag(self):
        return self.value

    def find_pair(self, current_depth):
        return None

    def inorder(self):
        return [self]


class Pair(Tree):
    def __init__(self, l, r):
        self.parent = None
        self.left = l
        self.right = r
        self.left.parent = self
        self.right.parent = self

    def __repr__(self):
        return "[{},{}]".format(self.left.__repr__(), self.right.__repr__())

    def mag(self):
        return self.left.mag() * 3 + self.right.mag() * 2


raw_numbers = []
for l in f:
    raw_numbers.append(l.strip())


def part1(numbers):
    n = Tree.parse(numbers[0])[0]
    for i in range(1, len(numbers)):
        n = n.add(Tree.parse(numbers[i])[0])
    return n.mag()


def part2(numbers):
    mag = 0
    for a in numbers:
        for b in numbers:
            mag = max(mag, Tree.parse(a)[0].add(Tree.parse(b)[0]).mag(),Tree.parse(b)[0].add(Tree.parse(a)[0]).mag())
    return mag

print('part1: ', part1(copy.deepcopy(raw_numbers)))
print('part2: ', part2(copy.deepcopy(raw_numbers)))
