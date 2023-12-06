import re
from functools import reduce

# f = open('data/day06-sample.txt', 'r')
f = open('data/day06-final.txt', 'r')


def part1(times, distances):
    ways = []
    for t, d in list(zip(times, distances)):
        count = 0
        for i in range(0, t):
            speed = i
            remaining = t - i

            if remaining * speed > d:
                count += 1

        ways.append(count)

    return reduce((lambda x, y: x * y), ways)


def lower_bound(time, distances):
    left = 0 
    right = time

    while left < right:
        mid = (left + right) // 2
        if mid * (time - mid) >= distances:
            right = mid
        else:
            left = mid + 1
    return left

def upper_bound(time, distances):
    left = 0
    right = time

    while left < right:
        mid = (left + right) // 2
        if mid * (time - mid) <= distances:
            right = mid
        else:
            left = mid + 1
    return left


def part2(times, distances):
    time = int("".join([str(t) for t in times]))
    distance = int("".join([str(d) for d in distances]))
    return upper_bound(time, distance) - lower_bound(time, distance)


lines = [l.strip() for l in f]

times = [int(t) for t in re.findall(r'(\d+)', lines[0])]
distances = [int(d) for d in re.findall(r'(\d+)', lines[1])]

print("part1: ", part1(times, distances))
print("part2: ", part2(times, distances))
