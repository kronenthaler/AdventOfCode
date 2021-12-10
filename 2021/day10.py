# f = open('data/day10-sample.txt', 'r')
f = open('data/day10-final.txt', 'r')

score_invalid = {')': 3, ']': 57, '}': 1197, '>': 25137}
score_incomplete = {')': 1, ']': 2, '}': 3, '>': 4}
compl = { '(': ')', '[': ']', '{': '}', '<': '>' }

def isValid(l):
    stack = []
    for c in l:
        if c in compl.keys():
            stack = [compl[c]] + stack
        elif stack[0] != c:
            return False, c, stack
        else:
            stack.pop(0)
    return True, '', stack


def part1(input):
    total = 0
    for l in input:
        r, c, _ = isValid(l)
        if not r:
            total += score_invalid[c]
    return total


def part2(input):
    scores = []
    for l in input:
        r, _, s = isValid(l)
        if r:
            score = 0
            for x in s:
                score = (score*5) + score_incomplete[x]
            scores.append(score)
    scores = sorted(scores)
    return scores[int(len(scores)/2)]


input = [l.strip() for l in f]

print('part1: ', part1(input.copy()))
print('part2: ', part2(input.copy()))