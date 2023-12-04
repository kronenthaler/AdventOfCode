import re
from functools import reduce

# f = open('data/day02-sample.txt', 'r')
f = open('data/day02-final.txt', 'r')


def part1(l, thresholds):
    valids = []
    for id, game in l.items():
        total = 0
        for pull in game:
            for color, count in pull.items():
                if count > thresholds[color]:
                    break
            else:
                total += 1

            if total == len(game):
                valids.append(id)

    return sum(valids)


def part2(l):
    valids = []
    for id, game in l.items():
        maxs = {}
        for pull in game:
            for color, count in pull.items():
                maxs[color] = max(maxs.get(color, 0), count)

        valids.append(reduce((lambda x, y: x * y), maxs.values()))

    return sum(valids)


lines = [l for l in f]


def parse(lines):
    games = {}
    for l in lines:
        id, game = re.match(r'Game (\d+): (.*)', l).groups()
        turns = game.split(';')
        games[int(id)] = []
        
        for turn in turns:
            steps = turn.split(', ')
            pull = {}
            for step in steps:
                count, color = re.match(r'(\d+) (red|green|blue)', step.strip()).groups()
                pull[color] = int(count)
            games[int(id)].append(pull)
    return games
games = parse(lines)

print("part1: ", part1(games.copy(), {'red': 12, 'green': 13, 'blue': 14}))
print("part2: ", part2(games.copy()))
