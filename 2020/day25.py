# data = (5764801, 17807724)
data = (1965712, 19072108)

def loop_sizes(subject_number, loop):
    memo = {}
    value = 1
    for i in range(loop):
        value = (value * subject_number) % 20201227
        memo[value] = i + 1

    return memo, value

def part1(data):
    card_size = sizes[data[0]]  # 7779516 for final input
    door_size = sizes[data[1]]  # 7177897 for final input

    # handshake algorithm
    _, key = loop_sizes(data[0], door_size)
    print(card_size, door_size)

    return key

sizes, _ = loop_sizes(7, 10000000)

print('part1: ', part1(data))
#print('part2: ', part2(data))