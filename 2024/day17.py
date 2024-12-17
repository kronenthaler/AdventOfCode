from utils import *
import copy

# f = open('data/day17-sample.txt', 'r')
f = open('data/day17-final.txt', 'r')

A = int(re.findall(r'Register A: ([0-9]+)', f.readline())[0])
B = int(re.findall(r'Register B: ([0-9]+)', f.readline())[0])
C = int(re.findall(r'Register C: ([0-9]+)', f.readline())[0])
f.readline()
commands = list([int(x) for x in re.findall(r'Program: (.*)', f.readline())[0].split(',')])

operands = [
    lambda a,b,c: 0,
    lambda a,b,c: 1,
    lambda a,b,c: 2,
    lambda a,b,c: 3,
    lambda a,b,c: a,
    lambda a,b,c: b,
    lambda a,b,c: c
]

# A, B, C, out, pointer = operation(op)
operations = [
    lambda op, pointer, a, b, c: (a >> operands[op](a,b,c), b, c, [], pointer+2),         # 0 adv => A
    lambda op, pointer, a, b, c: (a, b ^ op, c, [], pointer+2),                           # 1 bxl => B
    lambda op, pointer, a, b, c: (a, operands[op](a, b, c) % 8, c, [], pointer+2),        # 2 bst => B
    lambda op, pointer, a, b, c: (a, b, c, [], op if a != 0 else pointer+2),              # 3 jump
    lambda op, pointer, a, b, c: (a, b ^ c, c, [], pointer+2),                            # 4 bxc => B
    lambda op, pointer, a, b, c: (a, b, c, [operands[op](a,b,c) % 8], pointer+2),         # 5 out => print
    lambda op, pointer, a, b, c: (a, a >> operands[op](a,b,c), c, [], pointer+2),         # 6 bdv => B
    lambda op, pointer, a, b, c: (a, b, a >> operands[op](a,b,c), [], pointer+2),         # 7 cdv => C
]


def run(a, b, c):
    pointer = 0
    console = []
    while pointer + 1 < len(commands):
        operation = commands[pointer]
        op = commands[pointer + 1]
        a, b, c, out, pointer = operations[operation](op, pointer, a, b, c)
        console += out
    return console


def part1(a, b, c):
    console = run(a, b, c)
    return ",".join([str(x) for x in console])


def part2():
    def find(a, index):
        if index < -len(commands): # comparing negative numbers, FML
            return a
        for i in range(8):
            out = run((a << 3) + i, 0, 0)
            if out[0] == commands[index]:  # first matches with last
                result = find((a << 3) + i, index-1)
                if result:
                    return result
        return 0
    return find(0, -1)


print("part1: ", part1(A, B, C))
print("part2: ", part2())
