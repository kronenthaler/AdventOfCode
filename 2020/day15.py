#f = open('data/day15-sample.txt', 'r')
f = open('data/day15-final.txt', 'r')

input = [int(x) for x in [l.split(',') for l in f][0]]

def part1(input, target):
    mem = {}
    current = -1

    for i in range(0, input.__len__()):
        mem[input[i]] = i + 1
        current = input[i]

    for i in range(input.__len__(), target):
        # if i % 1000 == 0:
        #     print(i)
        diff = i - mem.get(current, i)
        mem[current] = i
        current = diff

    return current

print('part1: ', part1(input, 2020))
print('part2: ', part1(input, 30000000))