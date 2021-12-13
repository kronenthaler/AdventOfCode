from functools import reduce

# f = open('data/day10-sample.txt', 'r')
f = open('data/day10-final.txt', 'r')

score_invalid = {')': 3, ']': 57, '}': 1197, '>': 25137}
score_incomplete = {')': 1, ']': 2, '}': 3, '>': 4}
compl = { '(': ')', '[': ']', '{': '}', '<': '>' }

def isValid(l):
    stack = []
    for c in l:
        if c in compl.keys():
            stack.insert(0, compl[c])
        elif (x := stack.pop(0)) != c:
            return False, c, stack
    return True, '', stack


def part1(input):
    total = 0
    for l in input:
        valid, c, _ = isValid(l)
        if not valid:
            total += score_invalid[c]
    return total


def part2(input):
    scores = []
    for l in input:
        valid, _, s = isValid(l)
        if valid:
            scores.append(reduce(lambda score, x: score*5 + score_incomplete[x], s, 0))
    scores = sorted(scores)
    return scores[int(len(scores)/2)]


input = [l.strip() for l in f]

print('part1: ', part1(input.copy()))  # 315693
print('part2: ', part2(input.copy()))  # 1870887234
