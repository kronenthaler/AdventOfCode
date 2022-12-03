# f = open('data/day3-sample.txt', 'r')
f = open('data/day3-final.txt', 'r') # 13676 failed: too high


def prio(common):
    if ord('a') <= ord(common) <= ord('z'):
        return ord(common) - ord('a') + 1
    return ord(common) - ord('A') + 27


def part1(l):
    return sum([prio(list(set(h1) & set(h2))[0]) for h1, h2 in [(p.strip()[0:len(p)/2], p.strip()[len(p)/2:]) for p in l]])


def part2(l):
    return sum([prio(list(set(l[i]) & set(l[i+1]) & set(l[i+2]))[0]) for i in range(0, len(l), 3)])


moves = [l.strip() for l in f]

print("part1: ", part1(moves))
print("part2: ", part2(moves))
