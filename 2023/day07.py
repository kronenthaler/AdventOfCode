import re
from collections import Counter
from functools import cmp_to_key

# f = open('data/day07-sample.txt', 'r')
f = open('data/day07-final.txt', 'r')


values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
          '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}


def hand_type(tally):
    freq = tally.values()
    if 5 in freq: return 6  # five of a kind
    if 4 in freq: return 5  # four of a kind
    if 3 in freq and 2 in freq: return 4  # full house
    if 3 in freq: return 3  # three of a kind
    if 2 == sum([1 for v in freq if v == 2]): return 2
    if 2 in freq: return 1  # one pair
    return 0  # high card


def hand_type2(hand):
    conversions = {
        0: {0: 0, 1: 1, 2: 3, 3: 5, 4: 6, 5: 6},
        1: {0: 1, 1: 3, 2: 5, 3: 6},
        2: {0: 2, 1: 4, },
        3: {0: 3, 1: 5, 2: 6},
        4: {0: 4},
        5: {0: 5, 1: 6},
    }

    tally = Counter(hand)
    jokers = tally.pop('J', 0)

    return conversions[hand_type(tally)][jokers]


def compare(h1, h2):
    if h1[2] != h2[2]: return h1[2] - h2[2]
    for i in range(5):
        if h1[0][i] != h2[0][i]:
            return values[h1[0][i]] - values[h2[0][i]]
    return 0


def part1(hands, hand_type=hand_type):
    game = [(hand, int(bid), hand_type(Counter(hand))) for hand, bid in hands]
    game.sort(key=cmp_to_key(compare), reverse=False)
    return sum([b * (index+1) for index, (hand, b, t) in enumerate(game)])


def part2(hands):
    values['J'] = 1
    return part1(hands, hand_type2)


lines = [tuple(l.strip().split(' ')) for l in f]

print("part1: ", part1(lines))
print("part2: ", part2(lines))
