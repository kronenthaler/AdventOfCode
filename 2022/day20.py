import re
from collections import deque

# f = open('data/day20-sample.txt', 'r')
f = open('data/day20-final.txt', 'r')


def part1(l, base, iterations):
    N = len(l)
    indices = deque([i for i in range(0, N)])
    values = deque([v*base for v in l])

    for t in range(iterations):
        for i in range(N):
            position = indices.index(i)
            # apply the same transformation to both queues
            values.rotate(-position)  # bring to the left
            current_value = values.popleft()
            values.rotate(-current_value)
            values.appendleft(current_value)

            indices.rotate(-position)
            index = indices.popleft()
            indices.rotate(-current_value)
            indices.appendleft(index)

    zero = values.index(0)
    return sum([values[(zero + 1000*i) % N] for i in range(1, 4)])


lines = [int(l.strip()) for l in f]

print("part1: ", part1(lines, 1, 1))
print("part2: ", part1(lines, 811589153, 10))
