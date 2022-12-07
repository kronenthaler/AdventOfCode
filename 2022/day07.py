import re

# f = open('data/day7-sample.txt', 'r')
f = open('data/day7-final.txt', 'r')

class Node:
    def __init__(self, name, size=0):
        self.parent = None
        self.name = name
        self.children = []
        self.size = size
        self.dir_size = 0

    def add_children(self, child):
        self.children.append(child)
        child.parent = self

    def select_child(self, name):
        for c in self.children:
            if c.name == name:
                return c

    def populate_dir_size(self):
        if self.size != 0:
            return self.size

        for c in self.children:
            self.dir_size += c.populate_dir_size()

        return self.dir_size

    def sum(self, limit): # 1667443 correct
        if self.size != 0:  # leaf
            return 0

        total = 0
        for c in self.children:
            if c.size == 0 and c.dir_size <= limit:
                total += c.dir_size
            total += c.sum(limit)
        return total

    def dir_bigger_than(self, limit, result):  # 8998590 correct
        if self.size != 0:  # leaf
            return []

        for c in self.children:
            if c.size == 0 and c.dir_size >= limit:
                result.append(c.dir_size)
            c.dir_bigger_than(limit, result)
        return result


def part1(root, size):
    return root.sum(size)


def part2(root, total, min):
    return sorted(root.dir_bigger_than(min - (total - root.dir_size), []))[0]


cmds = [l.strip() for l in f]
root = Node('')
root.add_children(Node('/'))
current = root
for l in cmds:
    if l[0] == '$':  # command, ls can be skipped, cd needs parsing
        if 'cd' in l:
            dir = l.replace('$ cd ', '')
            if dir == '..':
                current = current.parent
            else:
                current = current.select_child(dir)
    else:  # data
        if 'dir' in l: # it is a dir => create a node
            dir = l.replace('dir ', '')
            current.add_children(Node(dir))
        else:
            tokens = l.split(' ')
            current.add_children(Node(tokens[1], size=int(tokens[0])))
root.populate_dir_size()

print("part1: ", part1(root, 100000))
print("part2: ", part2(root, 70000000, 30000000))