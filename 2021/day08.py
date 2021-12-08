# f = open('data/day08-sample.txt', 'r')
f = open('data/day08-final.txt', 'r')

def part1(l):
    return sum([1 for _, (a,b,c,d) in l for x in [a,b,c,d] if len(x) in [2,3,4,7]])


def part2(l):
    # remap the values of abcdefg per line and add the decoded value.
    # 1, 7, 4, 8, (9, 6, 0), (2, 3, 5)
    # aaa
    #b   c
    #b   c
    # ddd
    #e   f
    #e   f
    # ggg
    table = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9',
    }
    total = 0
    for d, o in l:
        display = sorted(list(d), key=lambda x: len(x))
        a = b = c = d = e = f = g = ''
        # determine the replacement patterns
        # 1-7 share 2 values => 3rd value of 7 is known
        a = [x for x in display[1] if x not in display[0]][0]

        for x in [set(x) for x in display if len(x) == 6]:
            if len(set(display[0]).intersection(x)) == 1:
                f = list(set(display[0]).intersection(x))[0]
                c = list(set(display[0]).difference(set(f)))[0]
                break

        dg = set(display[-1])
        for x in [set(x) for x in display if len(x) == 5]:
            dg = dg.intersection(x)

        dg.remove(a)
        d = list(set(display[2]).intersection(dg))[0]
        g = list(dg - set(d))[0]
        b = list(set(set(display[2]).difference(set([c,d,f]))))[0]
        e = list(set(set(display[-1]).difference(set([a,b,c,d,f,g]))))[0]

        trans = {a: 'a', b: 'b', c: 'c', d:'d', e:'e', f:'f', g:'g'}
        total += int("".join([table["".join(sorted([trans[j] for j in x]))] for x in o]))

    return total


input = []
for l in f:
    toks = l.strip().split(' ')
    input.append((tuple(toks[0:10]), tuple(toks[11:])))

print('part1: ', part1(input.copy()))
print('part2: ', part2(input.copy()))