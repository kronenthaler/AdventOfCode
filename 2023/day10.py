import re

# f = open('data/day10-sample.txt', 'r')
f = open('data/day10-final.txt', 'r')

neighbours = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'F': [(1, 0), (0, 1)],
    '7': [(0, -1), (1, 0)],
    'J': [(-1, 0), (0, -1)],
    'L': [(0, 1), (-1, 0)],
}


def print_board(l, inside_pos):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if (i, j) in inside_pos:
                print('I', end='')
            else:
                print(l[i][j], end='')
        print()


def part1(l, s):
    # determine the neighbours of the starting point
    neighbours['S'] = []
    for dx, dy, symbol in [(-1, 0, ['|', 'F', '7']), (0, 1, ['-', '7', 'J']), (1, 0, ['|', 'J', 'L']),
                           (0, -1, ['-', 'F', 'L'])]:
        if 0 <= s[0] + dx < len(l) and 0 <= s[1] + dy < len(l[0]) and l[s[0] + dx][s[1] + dy] in symbol:
            neighbours['S'].append((dx, dy))

    # replace the starting point with the correct symbol
    replacement = ''
    for key, neighs in neighbours.items():
        if key == 'S': continue
        if set(neighs) == set(neighbours['S']):
            replacement = key
            break
    l[s[0]] = l[s[0]][:s[1]] + replacement + l[s[0]][s[1] + 1:]

    # start flooding (BFS)
    start = (s[0], s[1], 0)
    queue = [start]
    visited = set([start])
    max_d = 0
    while queue:
        x, y, d = queue.pop(0)
        visited.add((x, y))

        for dx, dy in neighbours[l[x][y]]:
            if (x + dx, y + dy) not in visited and 0 <= x + dx < len(l) and 0 <= y + dy < len(l[0]):
                max_d = max(max_d, d + 1)
                queue.append((x + dx, y + dy, d + 1))
    return max_d, visited


def part2(l, s):
    # clean up the main loop
    _, main_loop = part1(l, s)
    for i in range(len(l)):
        for j in range(len(l[i])):
            if (i, j) not in main_loop:
                l[i] = l[i][:j] + '.' + l[i][j + 1:]

    # do a rastering scan, everything that goes up, changes direction of loop.
    # if we were going from the bottom to the top, the ones pointing down will change the loop direction
    northen = ['|', 'L', 'J']
    inside = False
    inside_pos = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] in northen:
                inside = not inside
            elif l[i][j] == '.' and inside:
                inside_pos.append((i, j))

    # print_board(l, inside_pos)
    return len(inside_pos)


lines = [l.strip() for l in f]
start = [(i, j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == 'S'][0]

print("part1: ", part1(lines, start)[0])
print("part2: ", part2(lines, start))
