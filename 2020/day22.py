import re

# f = open('data/day22-sample.txt', 'r')
f = open('data/day22-final.txt', 'r')

players = {}
active = ''
for l in f:
    l = l.strip()
    if l.__len__() == 0: continue
    p = re.match('Player (.*):', l)
    if p is not None:
        active = p.group(1)
        continue
    deck = players.get(active, [])
    deck.append(int(l))
    players[active] = deck

def score(l):
    return sum([(l.__len__() - i + 1) * l[i - 1] for i in range(l.__len__(), 0, -1)])

def part1(p1, p2):
    while len(p1) != 0 and len(p2) != 0:
        t1, t2 = p1.pop(0), p2.pop(0)
        p1.extend([t1, t2]) if t1 > t2 else p2.extend([t2, t1])

    return p1 if len(p1) != 0 else p2


def game(p1, p2):
    rounds = set()  # tuple(player, deck.copy())
    while len(p1) != 0 and len(p2) != 0:
        # infinite loop stopper
        d1, d2 = (1, tuple(p1)), (2, tuple(p2))
        if d1 in rounds or d2 in rounds:
            return 1, p1

        rounds.update([d1, d2])

        t1, t2 = p1.pop(0), p2.pop(0)
        if len(p1) >= t1 and len(p2) >= t2:
            winner = game(p1[:t1], p2[:t2])
        else:
            winner = (1, p1) if t1 > t2 else (2, p2)

        p1.extend([t1, t2]) if winner[0] == 1 else p2.extend([t2, t1])

    return (1, p1) if len(p1) != 0 else (2, p2)


print('part1:', score(part1(players['1'].copy(), players['2'].copy())))
print('part2:', score(game(players['1'].copy(), players['2'].copy())[1]))