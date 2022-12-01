# f = open('data/day1-sample.txt', 'r')
f = open('data/day1-final.txt', 'r')

lists = []
current = None
for l in f:
    l = l.strip()
    if current is None:
        current = []
    if l == '':
        lists.append(current)
        current = None
    else:
        current.append(int(l.strip()))
lists.append(current)
lists = sorted([sum(l) for l in lists], reverse=True)

print("part1: ", lists[0])
print("part2: ", sum(lists[0:3]))