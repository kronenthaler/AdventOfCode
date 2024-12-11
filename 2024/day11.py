import functools

# f = open('data/day11-sample.txt', 'r')
f = open('data/day11-final.txt', 'r')


@functools.cache
def transform(stone, times):
    if times == 0:
        return 1
    if stone == '0':
        return transform('1', times - 1)
    if len(stone) % 2 == 0:
        a = stone[0:len(stone) // 2]
        b = str(int(stone[len(stone) // 2:]))
        return transform(a, times - 1) + transform(b, times - 1)
    return transform(str(int(stone) * 2024), times - 1)


def dp(l, times):
    return sum([transform(x, times) for x in l])


lines = [l.strip().split(' ') for l in f][0]

print("part1: ", dp(lines, 25))
print("part2: ", dp(lines, 75))
