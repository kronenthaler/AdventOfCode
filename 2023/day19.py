import copy
import re

# f = open('data/day19-sample.txt', 'r')
f = open('data/day19-final.txt', 'r')


def part1(works, ps):
    valids = []
    for p in ps:
        w = works['in']
        resolved = False
        while not resolved:
            for cond, op, var, value, dest, rule in w:
                if not cond(p, op, var, value):
                    continue
                if dest == 'A':
                    valids.append(p)
                    resolved = True
                elif dest == 'R':
                    resolved = True
                else:
                    w = works[dest]
                break
    return sum([sum(v for v in vs.values()) for vs in valids])


class Node:
    def __init__(self, name, values, children):  # tuples (min, max)
        self.name = name
        self.values = copy.deepcopy(values)

        self.children = []  # [Node]
        previous_limits = {} # when evaluating a min/max of a condition, can update the limits for the next condition

        for _, op, var, value, dest, r in children:
            temp = copy.deepcopy(self.values)
            for k, (minv, maxv) in previous_limits.items():
                temp[k] = (max(temp[k][0], minv), min(temp[k][1], maxv))

            if var != 0:
                minv, maxv = temp[var]
                if op == '>':
                    temp[var] = [value + 1, maxv]
                    previous_limits[var] = (previous_limits.get(var, (1, 4000))[0], value)
                else:
                    temp[var] = [minv, value - 1]
                    previous_limits[var] = (value, previous_limits.get(var, (1, 4000))[1])

            self.children.append(Node(dest, temp, workflows[dest] if dest in workflows else []))

    def traverse(self, target):  # return counts
        if self.name == target:
            total = 1
            for _, (minv, maxv) in self.values.items():
                total *= maxv - minv + 1
            return total

        return sum(c.traverse(target) for c in self.children)


def part2(workflows):
    root = Node('in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}, workflows['in'])
    # there are overlaps, there are more accepted that actual possibilities!

    # 280577733351630 too high, 19211697726769 too low
    # 167409079868000 sample
    accepted = root.traverse('A')
    rejected = root.traverse('R')
    total = 4000*4000*4000*4000

    if accepted > total:
        print('overcounting!')

    print(accepted+rejected, total, accepted, rejected)
    return root.traverse('A'), root.traverse('R')



lines = [l.strip() for l in f]

workflows = []
parts = []
current = workflows
for l in lines:
    if len(l) == 0:
        current = parts
        continue
    current.append(l)

workflows = [tuple(re.match(r'(.*)\{(.*)\}', w).groups()) for w in workflows]
workflows = {name: rules.split(',') for name, rules in workflows}
ops = {
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y,
    '=': lambda x, y: x == y
}

for name, rules in workflows.items():
    lrules = []  # lambda that receives the whole dictionary with xmas values, and a destination if true
    for r in rules:
        if ':' not in r:
            lrules.append((lambda x, op, var, value: True, 0, 0, 0, r, r))
            continue
        cond, dest = tuple(r.split(':'))
        var, op, value = re.match(r'(.*)([<>])(.*)', cond).groups()
        lrules.append((lambda x, o, v, t: ops[o](x[v], t), op, var, int(value), dest, r))
    workflows[name] = lrules
# print(workflows)

parts = [p.replace('{', '').replace('}', '').split(',') for p in parts]
parts = [{s.split('=')[0]: int(s.split('=')[1]) for s in p} for p in parts]
# print(parts)


print("part1: ", part1(workflows, parts))
print("part2: ", part2(workflows))
