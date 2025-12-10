import re

from utils import *

# f = open('data/day10-sample.txt', 'r')
f = open('data/day10-final.txt', 'r')

lines = [l.strip() for l in f]
parsed = []
for l in lines:
    lights = re.findall(r'\[([.#]+)\]', l)[0]
    joltage = list(map(int, re.findall(r'\{(.+)\}', l)[0].split(',')))
    buttons = list(map(lambda x: list(map(int, x.strip().replace('(', '').replace(')','').split(','))), re.findall(r'(\(.*?\) ?)', l)))
    parsed.append((lights, buttons, joltage))


def find_min(state, buttons):
    start = "." * len(state)
    queue = [(start, 0)]
    visited = set(["".join(start)]) # avoid check same state twice

    while queue:
        current, count = queue.pop(0)
        if current == state:
            return count
        for b in buttons:
            new_state = list(current)
            for i in b:
                new_state[i] = '.' if current[i] == '#' else '#'
            new_state = "".join(new_state)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, count+1))
    return -1

# probably something to do with divisibility, order doesn't matter in this case.
def find_voltage(state, buttons):
    start = tuple([0] * len(state))
    queue = [(start, 0)]
    visited = set([start])  # avoid check same state twice

    while queue:
        current, count = queue.pop(0)
        for b in buttons:
            new_state = list(current)
            for i in b:
                new_state[i] = current[i] + 1
            new_state = tuple(new_state)
            ok = sum([1 if new_state[i] > state[i] else 0 for i in range(len(new_state))])
            if new_state not in visited and ok <= 0:
                if new_state == state:
                    print("solution found: ", new_state, state, count + 1)
                    return count + 1

                visited.add(new_state)
                queue.append((new_state, count + 1))
    return -1

def part1(l):
    return sum(find_min(s, b) for s, b, _ in l)


def part2(l):
    return sum(find_voltage(tuple(j), b) for _, b, j in l)


print("part1: ", part1(parsed))
print("part2: ", part2(parsed))
