# f = open('data/day07-sample.txt', 'r')
f = open('data/day07-final.txt', 'r')

def part1(l):
    n = max(l)
    result = (n * l.__len__())*(n * l.__len__())
    for i in range(n):
        subtotal = 0
        for x in l:
            subtotal += abs(x-i)
        result = min(subtotal, result)
    return result


def part2(l):
    n = max(l)
    result = (n * l.__len__())*(n * l.__len__())
    for i in range(n):
        subtotal = 0
        for x in l:
            m = abs(x-i)
            subtotal += int(m * (m+1)/2)
        result = min(subtotal, result)
    return result


input = [int(x.strip()) for x in f.readline().split(',')]

print('part1: ', part1(input.copy()))
print('part2: ', part2(input.copy()))