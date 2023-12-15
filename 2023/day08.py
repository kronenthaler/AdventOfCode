import re
import math

# f = open('data/day08-sample.txt', 'r')
f = open('data/day08-final.txt', 'r')

class Node:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right


def part1(inst, graph, src, goal):
    current = src
    steps = 0
    index = 0
    while current not in goal:
        current = graph[current][int(instructions[index])]
        index = (index + 1) % len(inst)
        steps += 1
    return steps


def part2(inst, graph):
    current = set([k for k in graph.keys() if k[2] == 'A'])
    goals = set([k for k in graph.keys() if k[2] == 'Z'])

    return math.lcm(*[part1(inst, graph, c, goals) for c in current])


lines = [l.strip() for l in f if l.strip() != '']
instructions = lines.pop(0).replace('R', '1').replace('L', '0')
graph = {}
for l in lines:
    src, left, right = re.match(r'(\w+) = \((\w+), (\w+)\)', l).groups()
    graph[src] = (left, right)

print("part1: ", part1(instructions, graph, 'AAA', set(['ZZZ'])))
print("part2: ", part2(instructions, graph))
