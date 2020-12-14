import re

#f = open('data/day14-sample.txt','r')
# f = open('data/day14-sampleB.txt','r')
f = open('data/day14-final.txt','r')

input = [l for l in f]

def part1(input):
    andMask = int('1'*36, 2)
    orMask = 0
    mem = {}
    for line in input:
        matches = re.match(r'(.*?) = (.*)', line)
        if matches.group(1) == 'mask':
            mask = matches.group(2)
            andMask = int(mask.replace('1', '0').replace('X', '1'), 2)
            orMask = int(mask.replace('X', '0'), 2)
        elif matches.group(1).startswith('mem'):
            index = re.match(r'mem\[(.*)\]', matches.group(1)).group(1)
            mem[index] = (int(matches.group(2)) & andMask) | orMask

    return sum([x for k, x in mem.items()])


def part2(input):
    def apply_mask(index, value):
        # permutate over mask and for each value, apply the mask and
        n = 2**mask.count('X')
        for comb in range(0, n):
            bit = 0
            newMask = mask
            floating = 0
            for i in [i for i in range(0, newMask.__len__()) if newMask[i] == 'X']:
                floating |= (((comb >> bit) & 1) << newMask.__len__() - 1 - i)
                bit += 1
            andMask = int(newMask.replace('X', '_').replace('1', '_').replace('0', '1').replace('_', '0'), 2)
            orMask = int(newMask.replace('X', '0'), 2) | floating
            newIndex = (int(index) & andMask) | orMask
            mem[newIndex] = value

    mem = {}
    mask = ''
    for line in input:
        matches = re.match(r'(.*?) = (.*)', line)
        if matches.group(1) == 'mask':
            mask = matches.group(2)
        elif matches.group(1).startswith('mem'):
            index = re.match(r'mem\[(.*)\]', matches.group(1)).group(1)
            apply_mask(index, int(matches.group(2)))

    return sum([x for k, x in mem.items()])


print('part1:', part1(input))
print('part2:', part2(input))
