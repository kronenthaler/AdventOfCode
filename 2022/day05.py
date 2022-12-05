import re

# f = open('data/day5-sample.txt', 'r')
f = open('data/day5-final.txt', 'r')


def part1(stacks, moves):
    for amount, src, dst in moves:
        stacks[dst] = stacks[src][0:amount][::-1] + stacks[dst]
        stacks[src] = stacks[src][amount:]

    return "".join([s[0] for s in stacks])

def part2(stacks, moves):
    for amount, src, dst in moves:
        stacks[dst] = stacks[src][0:amount] + stacks[dst]
        stacks[src] = stacks[src][amount:]

    return "".join([s[0] for s in stacks])

stacks = []
for l in f:
    if l.strip() == '':
        break
    stacks.append(l.strip())

moves = []
for l in f:
    matches = re.match(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)', l.strip())
    moves.append((int(matches[1]), int(matches[2])-1, int(matches[3])-1))

print("part1: ", part1(stacks.copy(), moves))
print("part2: ", part2(stacks.copy(), moves))
