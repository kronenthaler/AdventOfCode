import re

f = open('data/day01-sample.txt', 'r')
# f = open('data/day01-final.txt', 'r')


def part1(l):
    total = 0
    for line in l:
        digits = [c for c in line.strip() if c.isdigit()]
        if len(digits) > 0:
            total += int(f"{digits[0]}{digits[-1]}")

    return total


def part2(l):
    numbers1 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    total = 0
    for line in l:
        digits = []
        line = line.strip()
        for index, c in enumerate(line):
            if c.isdigit():
                digits.append(int(c))
            else:
                for pos, number in enumerate(numbers1):
                    if line[index:index+len(number)] == number:
                        digits.append(pos)
        total += int(f"{digits[0]}{digits[-1]}")
    return total


lines = [l for l in f]

print("part1: ", part1(lines))
print("part2: ", part2(lines))
