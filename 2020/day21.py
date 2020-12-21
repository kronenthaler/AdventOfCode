f = open('data/day21-sample.txt', 'r')
# f = open('data/day21-final.txt', 'r')

data = [l.strip() for l in f]
all = set()
comb = {}
all_ingredients = []
for d in data:
    parts = d.split('(contains ')
    ingredients = parts[0].strip().split(' ')
    allergens = parts[1].strip(')').split(', ')
    for a in allergens:
        poss, count = comb.get(a, ([], 0))
        poss.extend(ingredients)
        comb[a] = (poss, count + 1)
    all.update(allergens)
    all_ingredients.extend(ingredients)

m = {}
changed = True
while changed:
    changed = False
    for k in sorted(comb, key=lambda x: comb[x][1], reverse=True):
        l = sorted(comb[k][0])
        for x, y in {i: l.count(i) for i in l}.items():
            if y >= comb[k][1] and x not in m.values():
                changed = True
                m[k] = x
                break

print('part1:', len([i for i in all_ingredients if i not in m.values()]))
print('part2:', ','.join([x[1] for x in sorted(m.items(), key=lambda t: t[0])]))