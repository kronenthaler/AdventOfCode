import re
import copy


# f = open('data/day12-sample.txt', 'r')
f = open('data/day12-final.txt', 'r')


def part2(input, allow_repeat=None):
    q = [('start', [], set(['start']), allow_repeat)]  # <node, path, visited, repeated item>
    paths = set()
    while len(q) != 0:
        current = q.pop(0)
        if current[0] == 'end':
            paths.add(tuple(current[1] + ['end']))
            continue

        for e in input[current[0]]:
            if (e.islower() and e not in current[2] and e != 'start') or (not e.islower()):
                q.insert(0, (e, current[1] + [current[0]], current[2] | set([e]), current[3]))
                if current[3] is None:
                    q.insert(0, (e, current[1] + [current[0]], current[2], e))
    # [print(p) for p in paths]
    return len(paths)


links = [tuple(l.strip().split('-')) for l in f]
input = dict()
for a, b in links:
    input.setdefault(a, []).append(b)
    input.setdefault(b, []).append(a)


print('part1: ', part2(copy.deepcopy(input), allow_repeat=False))
print('part2: ', part2(copy.deepcopy(input)))
