# f = open('data/day4-sample.txt', 'r')
f = open('data/day4-final.txt', 'r') # 13676 failed: too high


def part1(l):
    contained = 0
    for (l1, h1), (l2, h2) in l:
        r1 = set(range(l1, h1 + 1))
        r2 = set(range(l2, h2 + 1))
        overlap = r1 & r2
        if overlap == r1 or overlap == r2:
            contained += 1
    return contained


def part2(l):
    contained = 0
    for (l1, h1), (l2, h2) in l:
        r1 = set(range(l1, h1 + 1))
        r2 = set(range(l2, h2 + 1))
        if len(r1 & r2) != 0:
            contained += 1
    return contained


moves = [((map(int, l.strip().split(',')[0].split('-'))), (map(int, l.strip().split(',')[1].split('-')))) for l in f]

print("part1: ", part1(moves))
print("part2: ", part2(moves))
