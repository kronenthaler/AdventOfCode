import re

# f = open('data/day19-sample.txt', 'r')
# f = open('data/day19-sampleB.txt', 'r')
f = open('data/day19-final.txt', 'r')

rules = {}
for l in f:
    matches = re.match(r'([0-9]*): (.*)', l)
    if matches is None: break
    parts = matches.group(2).split('|')
    rules[matches.group(1)] = list([p.replace('"', '').strip().split(' ') for p in parts])

print(rules)
queries = [l for l in f]

def convert(rule):
    replacement = []
    for p in rule:
        replacement.append(','.join(p))
    if replacement.__len__() == 1:
        return replacement[0]
    return '({})'.format('|'.join(replacement))


def expand(rule0):
    max = 100
    changed = True
    while changed and max != 0:
        max -= 1
        changed = False
        temp = ''
        for m in re.finditer(r'([0-9]*)([()|,ab^$]*)', rule0):
            if m.group(1) != '':
                changed = True
                temp += convert(rules[m.group(1)])
            if m.group(2) != '':
                temp += m.group(2)

        rule0 = temp

    changed = True
    rule0 = rule0.replace('8', '')
    while changed:
        changed = False
        t = rule0.replace('||', '|')
        if t != rule0:
            rule0 = t
            changed = True

    return rule0.replace(',', '').replace('(a)', 'a').replace('(b)', 'b')


def expand2(rule0, rule42, rule31):
    changed = True
    while changed:
        changed = False
        temp = ''
        for m in re.finditer(r'([0-9]*)([()|,ab^$*?+]*)', rule0):
            if m.group(1) != '':
                changed = True
                if m.group(1) == '8':
                    temp += '(' + rule42 + ')'
                elif m.group(1) == '11':
                    temp += '(' + rule42 + rule31 + ')'
                else:
                    temp += convert(rules[m.group(1)])
            if m.group(2) != '':
                temp += m.group(2)

        rule0 = temp

    return rule0.replace(',', '')


def part1(rules, queries):
    # process the rules.
    rule0 = expand('^'+(','.join(rules['0'][0]))+'$')
    count = 0
    for q in queries:
        if re.match(rule0, q) is not None:
            count += 1
    return count

def part2(rules, queries):
    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]
    rule0 = expand('^' + (','.join(rules['0'][0])) + '$')
    count = 0
    for q in queries:
        if re.match(rule0, q) is not None:
            count += 1
    return count

print('part1: ', part1(rules, queries))
print('part2: ', part2(rules, queries))