# f = open('data/day2-sample.txt', 'r')
f = open('data/day2-final.txt', 'r') # 13676 failed: too high


def win(me, op):
    if (me == 0 and op == 2) or (me == 1 and op == 0) or (me == 2 and op == 1):
        return 6
    if me == op:
        return 3
    return 0


def part1(l):
    def score(a, b):
        op = ord(a) - ord('A')  # a=rock, b=paper, c=scissors
        me = ord(b) - ord('X')  # x=rock, y=paper, z=scissors
        return (me + 1) + win(me, op)

    return sum([score(*t) for t in l])


def part2(l):
    def score(a, b):
        op = ord(a) - ord('A')  # a=rock, b=paper, c=scissors
        me = ord(b) - ord('X')  # x=lose, y=tie, z=win

        return [(m + 1) + win(m, op) for m in range(0, 3) if win(m, op) / 3 == me][0]

    return sum([score(*t) for t in l])


moves = [tuple(l.strip().split(' ')) for l in f]

print("part1: ", part1(moves))
print("part2: ", part2(moves))
