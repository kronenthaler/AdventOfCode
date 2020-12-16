import re
import functools


# f = open('data/day16-sample.txt', 'r')
# f = open('data/day16-sampleB.txt', 'r')
f = open('data/day16-final.txt', 'r')

rules = {}
mine = ""
others = []

for l in f:
    if l.strip().__len__() == 0: break
    tokens = re.match(r'(.*): ([0-9]*)-([0-9]*) or ([0-9]*)-([0-9]*)', l)
    rules[tokens.group(1)] = [(int(tokens.group(2)), int(tokens.group(3))), (int(tokens.group(4)), int(tokens.group(5)))]

f.readline()  # your ticket:
mine = list([int(x) for x in f.readline().strip().split(',')])

f.readline()  # empty
f.readline()  # empty

for l in f:
    others.append(list([int(x) for x in l.strip().split(',')]))


def is_valid(t, rules):
    fails = {}
    for i in range(0, t.__len__()):
        f = t[i]
        match = False
        for k, v in rules.items():
            if v[0][0] <= f <= v[0][1] or v[1][0] <= f <= v[1][1]:
                match = True
            else:
                fails[k] = fails.get(k, set()) | set([i])
        if not match:
            return False, f, {}
    return True, 0, fails


def part1(rules, tickets):
    total = 0
    for t in tickets:
        total += is_valid(t, rules)[1]
    return total


def part2(rules, mine, tickets):
    merged = {}
    for t in tickets:
        for k, v in is_valid(t, rules)[2].items():
            merged[k] = merged.get(k, set()) | v

    assigned = {}  # key -> index
    indexes = list(range(0, mine.__len__()))
    while indexes.__len__() > 1:
        # loop and remove options
        for k, v in merged.items():
            if v.__len__() != indexes.__len__() - 1: continue

            # find index that is missing here and has not been assigned yet
            i = [x for x in indexes if x not in v][0]
            assigned[k] = i
            indexes.remove(i)
            del merged[k]
            break

    # last index must be the only rule not assigned
    assigned[[k for k, v in rules.items() if k not in assigned][0]] = indexes[0]

    return functools.reduce(lambda x, y: x * y, [mine[assigned[k]] for k, v in rules.items() if k.startswith('departure')], 1)


print('part1: ', part1(rules, others))
print('part2: ', part2(rules, mine, others))