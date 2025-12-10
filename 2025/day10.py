import re

from utils import *
from scipy.optimize import linprog, milp, LinearConstraint, Bounds
from numpy import transpose


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


def part1(l):
    return sum(find_min(s, b) for s, b, _ in l)


# it's not a simple equation system because there might be more equations (buttons) than variables needed (lights)
# it's a linear system minimization
def part2(l):
    total = 0
    for s, btns, j in l:
        # convert to a vector form
        btns_vector = []
        for b in btns:
            new_b = [0] * len(s)
            for i in b:
                new_b[i] += 1
            btns_vector.append(new_b)

        coef = [1] * len(btns_vector) # minimize all coefficients
        constraints = LinearConstraint(transpose(btns_vector), lb=j, ub=j) # the solution must be exactly equal
        bounds = Bounds(lb=0, ub=np.inf) # restrict to non-negative values
        result = milp(coef, integrality=[1] * len(btns_vector), constraints=constraints, bounds=bounds)
        count = math.ceil(sum(result.x))
        total += count

    return total  #16361


print("part1: ", part1(parsed))
print("part2: ", part2(parsed))
