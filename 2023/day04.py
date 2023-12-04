import re
from collections import Counter

# f = open('data/day04-sample.txt', 'r')
f = open('data/day04-final.txt', 'r')

def part1(lines):
    total = 0
    for card, winning, ticket in lines:
        current = 0
        for x in winning:
            if x in ticket:
                if current == 0:
                    current = 1
                else:
                    current *= 2
        total += current
    return total


def winners(card, winning, ticket):
    current = 0
    for x in winning:
        if x in ticket:
            current += 1
    return current

def part2(lines):
    counts = {card: 1 for card,_,_ in lines}

    for card, winning, ticket in lines:
        w = winners(card, winning, ticket)
        for i in range(card+1, card+1+w):
            counts[i] += counts[card]
        
    return sum(counts.values())


lines = [l for l in f]
def parse(lines):
    for l in lines:
        card, winning, ticket = re.match(r'Card\s*(\d+): (.*)\|(.*)', l).groups()
        yield (
            int(card), 
            list(map(lambda x: x.strip(), filter(lambda x: len(x) > 0, winning.strip().split(' ')))),
            list(map(lambda x: x.strip(), filter(lambda x: len(x) > 0, ticket.strip().split(' '))))
        )


# print("part1: ", part1(parse(lines)))
print("part2: ", part2([l for l in parse(lines)]))
