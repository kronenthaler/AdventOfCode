# f = open('data/day03-sample.txt', 'r')
f = open('data/day03-final.txt', 'r')


def part1(input, size):
    ones = [0] * size
    for x in input:
        for i in range(0, size):
            if x[i] == '1':
                ones[i] += 1

    gamma = [0]*size
    epsilon = [0]*size
    for i in range(0, size):
        gamma[i] = '1' if ones[i] >= input.__len__() - ones[i] else '0'
        epsilon[i] = '0' if gamma[i] == '1' else '1'

    return int("".join(str(x) for x in gamma), 2) * int("".join(str(x) for x in epsilon), 2), gamma, epsilon


def part2(input, size):
    oxy = input
    co2 = input

    current = 0
    while oxy.__len__() > 1:
        filter = part1(oxy, size)[1]
        oxy = [x for x in oxy if x[current] == filter[current]]
        current += 1

    current = 0
    while co2.__len__() > 1:
        filter = part1(co2, size)[2]
        co2 = [x for x in co2 if x[current] == filter[current]]
        current += 1
    print(oxy, co2)

    # wrong answer: 4406844
    return int("".join(str(x) for x in oxy), 2) * int("".join(str(x) for x in co2), 2)

input = [x.strip() for x in f.readlines()]

print("part1: {}".format(part1(input, input[0].__len__())))
print("part2: {}".format(part2(input, input[0].__len__())))