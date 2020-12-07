import re

#f = open('day7-sample.txt', 'r')
f = open('day7-final.txt', 'r')

invG = {}
G = {}
for line in f:
    matches = re.match(r'(.*) (bags contain) ((no other bags)|(.*))\.', line)
    target = matches.group(1)
    if target not in G:
        G[target] = []

    if matches.group(3) != "no other bags":
        for origin in re.finditer('([0-9]+) (.*?) bags?', matches.group(3)):
            # create tuple (target, origin.group(2))
            if origin.group(2) not in invG:
                invG[origin.group(2)] = []
            invG[origin.group(2)].append(target)
            G[target].append((int(origin.group(1)), origin.group(2)))
    else:
        G[target].append((0, ""))

def part1():
    queue = ['shiny gold']
    visited = set()
    while queue.__len__() != 0:
        current = queue.pop(0)
        if current in invG:
            for e in invG[current]:
                if e not in visited:
                    queue.append(e)
                    visited.add(e)

    return visited.__len__()

def part2(current):
    count = 0
    if current in G:
        for n, node in G[current]:
            count += n + n*part2(node)
    return count

print("part1:", part1())
print("part2: ", part2("shiny gold"))