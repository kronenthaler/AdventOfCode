import re
import time


# f = open('data/day12-sample.txt', 'r')
f = open('data/day12-final.txt', 'r')


def is_valid(l, s):
    for j in range(len(l)):
        if not ((s[j] == '1' and (l[j] == '#' or l[j] == '?')) or
                (s[j] == '0' and (l[j] == '.' or l[j] == '?'))):
            return False
    return True


def part1(lines):
    # brute force: generate all possible combinations for 2^20 => 22 seconds
    # for each combination, if the combination matches the mask, generate a list of section matches
    # create an inverted list of matches, with a set
    # look up the match in the list, return the lenght of the set
    start = time.time()
    total = 0
    for l, sections in lines:
        possibilities = {}
        sections = tuple(sections)

        for i in range((2**len(l))+1):
            s = "{0:b}".format(i).zfill(len(l))
            key = tuple([len(l) for l in s.split('0') if len(l) != 0])
            if is_valid(l, s) and key == sections:
                if key not in possibilities:
                    possibilities[key] = 0
                possibilities[key] += 1

        total += possibilities[sections]
    end = time.time()
    print(end - start)
    return total

def part2(l):
    # combinatorics?
    pass


lines = [l.strip() for l in f]
lines = [(l.split()[0], [int(x) for x in l.split()[1].split(',')]) for l in lines]

print("part1: ", part1(lines))
print("part2: ", part2(lines))
