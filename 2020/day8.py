import re

#f = open('day8-sample.txt', 'r')
f = open('day8-final.txt', 'r')

contents = f.readlines()

def sim(current, contents):
    visited = [0] * contents.__len__()
    counter = 0
    while current < contents.__len__() and visited[current] != 1:
        visited[current] += 1
        tokens = contents[current].split(' ')
        op = tokens[0]
        arg = tokens[1]

        if op == 'nop':
            current += 1
        if op == 'acc':
            current += 1
            counter += int(arg)
        if op == 'jmp':
            current += int(arg)

    return counter, current == contents.__len__()

def part2(contents):
    for index in range(0, contents.__len__()):
        line = contents[index]

        op = line.split(' ')[0]
        arg = line.split(' ')[1]
        if op == 'nop':
            contents[index] = 'jmp {0}'.format(arg)
        elif op == 'jmp':
            contents[index] = 'nop {0}'.format(arg)
        else:
            continue

        result = sim(0, contents)
        contents[index] = line

        if result[1]:
            return result

print('part1: ', sim(0, contents))
print('part2: ', part2(contents))

