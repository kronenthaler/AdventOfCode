import re

#f = open('day9-sample.txt', 'r')
f = open('day9-final.txt', 'r')

content = f.readlines()
digits = list([int(x) for x in content])


def part1(digits, preamble):
    for i in range(preamble+1, digits.__len__()):
        target = digits[i]
        found = False
        for j in range(i-preamble, i):
            for k in range(i-preamble, i):
                if j == k: continue
                found |= digits[j] + digits[k] == target
        if not found:
            return (target, i)
    return -1

def part2(digits, target):
    dp = []
    for i in range(0, digits.__len__()):
        dp.append([0] * digits.__len__())

    value = target[0]
    index = target[1]
    n = digits.__len__()
    t = 1
    for k in range(0, n-1):
        for i in range(0, n-1):
            j = i + k
            if j >= n: break
            dp[i][j] = digits[j] if i == j else digits[j] + dp[i][j - 1]
            if dp[i][j] == value and i != j:
                return max(digits[i:j]) + min(digits[i:j])

# change preamble to 25!!
# print("part1: ", part1(digits, 25))
print("part2: ", part2(digits, part1(digits, 25)))
