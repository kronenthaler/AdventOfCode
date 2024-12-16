import math

from utils import *
from copy import deepcopy
from queue import PriorityQueue as pqueue

# f = open('data/day16-sample.txt', 'r')
f = open('data/day16-final.txt', 'r')

lines = [list(l.strip()) for l in f]
N = len(lines)
M = len(lines[0])
S = tuple([(i, j) for i in range(N) for j in range(M) if lines[i][j] == 'S'][0])
E = tuple([(i, j) for i in range(N) for j in range(M) if lines[i][j] == 'E'][0])


def valid(t, min=(0, 0), max=(N, M)):
    return all(map(lambda m, t, M: m <= t < M, min, t, max))


def dijkstra(s, m):
    opened = pqueue()
    opened.put((0, (s, EAST), None))
    visited = {}
    parents = {(s, EAST): []}

    while not opened.empty():
        cost, vector, prev = opened.get()
        current, dir = vector

        if current == E:
            uniq = set()
            q = [prev]
            while len(q):
                node, d = q.pop()
                uniq.add(node)
                q.extend(parents[(node, d)])
            return cost, len(uniq) + 1

        if vector in visited:
            if cost <= visited[vector]:
                parents[vector].append(prev)
            continue

        visited[vector] = cost

        if prev is not None:
            parents[vector] = [prev]

        ni, nj = add(current, Steps2D[dir])
        if m[ni][nj] != '#':
            opened.put((cost + 1, ((ni, nj), dir), vector))

        for d in [-1, 1]:
            ndir = (dir + d) % len(Steps2D)
            opened.put((cost + 1000, (current, ndir), vector))

    return math.inf, ""


score, path = dijkstra(S, lines)
print("part1: ", score)
print("part2: ", path)
