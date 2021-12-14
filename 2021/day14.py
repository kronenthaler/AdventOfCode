import re
import copy
import collections
import math


# f = open('data/day14-sample.txt', 'r')
f = open('data/day14-final.txt', 'r')


def part2(patterns, seed, n):
    expansions = {k: [k[0] + v, v + k[1]] for k, v in patterns.items()}
    poly = dict(collections.Counter([seed[i:i+2] for i in range(len(seed)-1)]).most_common())

    for t in range(n):
        temp = {}
        for p, v in poly.items():
            new = expansions[p]
            temp[new[0]] = temp.setdefault(new[0], 0) + v
            temp[new[1]] = temp.setdefault(new[1], 0) + v
        poly = temp

    count = {}
    for k, v in poly.items():
        for k1, m in dict(collections.Counter(k).most_common()).items():
            count[k1] = count.setdefault(k1, 0) + (m * v)

    freq = collections.Counter({k: int(math.ceil(count[k]/2)) for k, v in count.items()}).most_common()
    return freq[0][1] - freq[-1][1]


seed = f.readline().strip()
f.readline()  # \n
patterns = {}
for l in f:
    groups = re.match('([A-Z]*) -> ([A-Z]*)', l.strip())
    patterns[groups[1]] = groups[2]


print('part1: ', part2(copy.deepcopy(patterns), seed, 10))
print('part1: ', part2(copy.deepcopy(patterns), seed, 40))
