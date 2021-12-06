# f = open('data/day06-sample.txt', 'r')
f = open('data/day06-final.txt', 'r')

def part1(seq, rounds):
    # increments for the base population
    incs = [0] * 7
    for i in range(0, 7):
        ext = sum([1 for x in seq if x == 0])
        seq = [(x-1) % 7 if x - 1 != 7 else x - 1 for x in seq]
        incs[(i+1) % 7] = ext

    nums = incs * int(rounds / 6)

    total = seq.__len__()
    for i in range(0, rounds + 1):
        if nums[i] == 0: continue
        if i + 9 >= nums.__len__(): continue

        to_add = nums[i]
        nums[i + 9] += to_add
        for j in range(i + 9 + 7, nums.__len__(), 7):
            if j < nums.__len__():
                nums[j] += to_add
        total += to_add

    return total


input = [int(x) for x in f.readline().split(',')]


print("part1: {}".format(part1(input.copy(), 80)))
print("partt2: {}".format(part1(input.copy(), 256)))
