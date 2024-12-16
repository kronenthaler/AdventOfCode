from utils import *

# f = open('data/day16-sample.txt', 'r')
f = open('data/day16-final.txt', 'r')

lines = [list(l.strip()) for l in f]
N = len(lines)
M = len(lines[0])
S = tuple([(i, j) for i in range(N) for j in range(M) if lines[i][j] == 'S'][0])
E = tuple([(i, j) for i in range(N) for j in range(M) if lines[i][j] == 'E'][0])


def valid(t, min=(0, 0), max=(N, M)):
    return all(map(lambda m, t, M: m <= t < M, min, t, max))


def path(vector, parents):
    uniq = set()
    start = [vector]
    checked = set()
    while len(start) != 0:
        next = start.pop()
        uniq.add(next[0])
        if next not in checked:
            start.extend(parents[next])
        checked.add(next)
    return uniq


def dijkstra(s, m):
    opened = PriorityQueue()
    opened.put((0, (s, EAST)))
    visited = {}
    parents = {(s, EAST): set()}

    while not opened.empty():
        cost, vector = opened.get()
        current, dir = vector

        if current == E:
            return cost, len(path(vector, parents))

        def adjs():
            for d in [-1, 1]:
                ndir = (dir + d) % len(Steps2D)
                yield 1000, (current, ndir)
            ni, nj = add(current, Steps2D[dir])
            if m[ni][nj] != '#':
                yield 1, ((ni, nj), dir)

        for ncost, nvector in adjs():
            cur_cost = visited.get(nvector, math.inf)
            if cost + ncost <= cur_cost:
                opened.put((cost + ncost, nvector))
                visited[nvector] = cost + ncost

                if cost + ncost < cur_cost:
                    parents[nvector] = {vector}
                else:
                    parents[nvector].add(vector)

    return math.inf, ""


score, path = dijkstra(S, lines)
print("part1: ", score)
print("part2: ", path)
