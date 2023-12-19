import re

# f = open('data/day19-sample.txt', 'r')
f = open('data/day19-final.txt', 'r')


def part1(workflows, parts):
    valids = []
    for p in parts:
        w = workflows['in']
        resolved = False
        while not resolved:
            for cond, op, var, value, dest, r in w:
                if not cond(p, op, var, value): continue
                if dest == 'A':
                    valids.append(p)
                    resolved = True
                    break
                if dest == 'R':
                    resolved = True
                    break
                w = workflows[dest]

    return sum([sum(v for v in vs.values()) for vs in valids])


def part2(l):
    # find how many combinations will be accepted.
    # xmas can be between 1 - 4000 [4000 * 4000 * 4000 * 4000 = 256,000,000,000,000]

    # find all paths to an A. -> those paths come with constraints.
    # try to do something with those constraints?
    pass


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
    lrules = []  #lambda that receives the whole dictionary with xmas values, and a destination if true
    for r in rules:
        if ':' not in r:
            lrules.append((lambda x, op, var, value: True, 0, 0, 0, r, r))
            continue
        cond, dest = tuple(r.split(':'))
        var, op, value = re.match(r'(.*)([<>])(.*)', cond).groups()
        lrules.append((lambda x, o, v, t: ops[o](x[v], t), op, var, int(value), dest, r))
    workflows[name] = lrules
print(workflows)

parts = [p.replace('{', '').replace('}', '').split(',') for p in parts]
parts = [{s.split('=')[0]: int(s.split('=')[1]) for s in p} for p in parts]
print(parts)


print("part1: ", part1(workflows, parts))
print("part2: ", part2(lines))
