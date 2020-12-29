import re

f = open("data/day3-final.txt", 'r')
# f = open("day3-sample.txt", 'r')
content = f.readlines()

def isValid(line):
    required = {
        'byr': [lambda x: 1920 <= int(x) <= 2002],
        'iyr': [lambda x: 2010 <= int(x) <= 2020],
        'eyr': [lambda x: 2020 <= int(x) <= 2030],
        'hgt': [lambda x: re.match('([0-9]*)(cm|in)', x), lambda y: (y.group(2) == 'cm' and 150 <= int(y.group(1)) <= 193) or (y.group(2) == 'in' and 59 <= int(y.group(1)) <= 76)],
        'hcl': [lambda x: re.match('#[0-9a-f]{6}$', x) is not None],
        'ecl': [lambda x: re.match('(amb|blu|brn|gry|grn|hzl|oth)$', x) is not None],
        'pid': [lambda x: re.match('[0-9]{9}$', x) is not None]
    }
    pairs = line.split(" ")
    count = 0
    strictCount = 0
    for pair in pairs:
        tokens = pair.split(":")
        if tokens[0] in required:
            count += 1
            prev = tokens[1]
            try:
                for f in required[tokens[0]]:
                    prev = f(prev)
                if prev:
                    strictCount += 1
            except:
                print(line)
                continue

    return (count == required.__len__(), strictCount == required.__len__())

aggregated = 0
strictAggregated = 0
for line in content:
    relaxed, strict = isValid(line)
    if relaxed:
        aggregated += 1
    if strict:
        strictAggregated += 1

print("part1: ", aggregated)
print("part2: ", strictAggregated)
