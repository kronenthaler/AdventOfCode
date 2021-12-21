import re
import copy
import collections

# f = open('data/day21-sample.txt', 'r')
f = open('data/day21-final.txt', 'r')


def part1(p1, p2):
    die = 1
    count = 0
    scores = [0, 0]
    p = [p1, p2]
    current = 0
    while True:
        total = 0
        for _ in range(3):
            total += die
            die = (die % 100) + 1

        p[current] = ((p[current]+total-1) % 10) + 1
        scores[current] += p[current]
        count += 3
        if scores[current] >= 1000:
            break
        current = 1 - current

    return count * scores[1 - current]


def part2(p1, p2):
    draws = collections.Counter([sum(x) for x in [(a, b, c) for a in range(1,4) for b in range(1,4) for c in range(1,4)]]).most_common()

    def dfs(p, scores, current):
        wins = [0, 0]
        for total, factor in draws:
            newP = [p[0], p[1]]
            newS = [scores[0], scores[1]]

            newP[current] = ((p[current] + total - 1) % 10) + 1
            newS[current] = scores[current] + newP[current]

            if newS[current] >= 21:
                wins[current] += factor
            else:
                wins = [a + (b * factor) for a, b in zip(wins, dfs(newP, newS, 1 - current))]

        return wins
    return max(dfs([p1, p2], [0, 0], 0))


p1 = int(re.match(r'Player . starting position: ([0-9]*)', f.readline()).group(1))
p2 = int(re.match(r'Player . starting position: ([0-9]*)', f.readline()).group(1))

print('part1: ', part1(p1, p2))
print('part2: ', part2(p1, p2))
