
# f = open('day10-sample.txt', 'r')
f = open('data/day10-final.txt', 'r')

jolts = sorted([int(x) for x in f])

def part1(jolts):
    prev = 0
    diff1 = 0
    diff3 = 0
    for j in jolts:
        diff = j - prev
        if diff == 1: diff1 += 1
        if diff == 3: diff3 += 1
        prev = j
    return diff1 * (diff3 + 1)


memo = [0] * (max(jolts) + 3)
valid = set(jolts)
valid.add(0)


def part2(jolts, current):
    if current == 0:
        return 1

    if memo[current] != 0:
        return memo[current]

    total = 0
    for i in range(1, 4):
        if (current - i) in valid:
            total += part2(jolts, current - i)
    memo[current] = total
    return total


print("part1: ", part1(jolts))
print("part2: ", part2(jolts, jolts[-1]))
