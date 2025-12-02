from utils import *

# f = open('data/day02-sample.txt', 'r')
f = open('data/day02-final.txt', 'r')

lines = [l.strip() for l in f]
lines = lines[0].split(',')
lines = [tuple(l.split('-')) for l in lines]
lines = [(int(x), int(y)) for x, y in lines]

def part1(l):
    return sum(i for s, e in l for i in range(s, e + 1) if (x:=str(i)) and x[0:len(x)//2] == x[len(x)//2:])


def part2(l):
    total = 0
    for s, e in l:
        for i in range(s, e+1):
            x = str(i)
            for j in range(1, len(x)):
                step = 10 ** j
                current = i
                target = current % step
                ok = True
                while current != 0:
                    if current % step != target or len(str(current % step)) != j:
                        ok = False
                        break
                    current = current // step

                if ok:
                    total += i
                    break
    return total

print("part1: ", part1(lines))
print("part2: ", part2(lines))
