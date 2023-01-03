import re

# f = open('data/day25-sample.txt', 'r')
f = open('data/day25-final.txt', 'r')


def to_dec(n):
    number = 0
    exp = 0
    for c in reversed(n):
        factor = -2
        if c in '012':
            factor = int(c)
        if c == '-':
            factor = -1
        number += factor * pow(5, exp)
        exp += 1
    return number


def dec_to_snafu(n):
    remap = {0: -2, 1: -1, 2: 0, 3: 1, 4: 2}
    chars = {-2: '=', -1: '-', 0: '0', 1: '1', 2: '2' }
    result = ''
    t0 = remap[(n - 3) % 5]
    result = chars[t0] + result
    n -= t0
    exp = 1
    while n // pow(5, exp) != 0:
        factor = remap[round((n / pow(5, exp)) - 3) % 5]
        result = chars[factor] + result
        n -= factor * pow(5, exp)
        exp += 1


    # for the units (5^0): (closest - 3) % 5 : 0=-2, 1=-1, 2=0, 3=1, 4=2
    # for tesn (5^1): (N - k(t-1)) % 5:
    # for the hundreds (5^2) (N - (k.5^1) - (k.5^0)) / 25
    # for thoudsands (5^3)
    return result


def part1(l):
    total = 0
    for n in l:
        total += to_dec(n)

    return dec_to_snafu(total)

def part2(l):
    pass


lines = [l.strip() for l in f]

print("part1: ", part1(lines))
print("part2: ", part2(lines))
