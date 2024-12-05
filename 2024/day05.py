import re
from functools import cmp_to_key

# f = open('data/day05-sample.txt', 'r')
f = open('data/day05-final.txt', 'r')


def part1(r):
    return sum([q[len(q) // 2] for q in r])


def compare(a, b):
    if a not in graph:
        return 1
    if b not in graph:
        return -1
    if a in graph[b]:
        return 1
    if b in graph[a]:
        return -1
    return 0


graph = {}
queries = []
for l in f:
    if (l := l.strip()) == '':
        break
    s, d = map(int, tuple(l.split('|')))
    graph[s] = graph.get(s, []) + [d]

queries = [list([int(x) for x in l.strip().split(',')]) for l in f]

results = [(q, sorted(q, key=cmp_to_key(compare))) for q in queries]
print("part1: ", part1([q for (q, v) in results if q == v]))
print("part2: ", part1([v for (q, v) in results if q != v]))
