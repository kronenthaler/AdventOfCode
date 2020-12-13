import math

#f = open('data/day13-sample.txt', 'r')
f = open('data/day13-final.txt', 'r')

ts = int(f.readline().strip())
buses = [l for l in f.readline().strip().split(',')]


def part1(ts, buses):
    bus = -1
    current = ts
    while bus == -1:
        #print(current)
        for b in buses:
            if current % b == 0:
                bus = b
                break
        current += 1

    return (current - ts - 1) * bus


def part2(ts, buses):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = egcd(b % a, a)
            return g, x - (b // a) * y, y

    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    product = 1
    for b in [x for x in buses if x != 0]:
        product *= b

    sm = 0
    for i in range(0, buses.__len__()):
        if buses[i] == 0:
            continue
        p = product // buses[i]
        sm += (buses[i] - i) * modinv(p, buses[i]) * p
    return sm % product


print('part1: ', part1(ts, [int(b) for b in buses if b != 'x']))
print('part2: ', part2(ts, list([int(b) if b != 'x' else 0 for b in buses])))