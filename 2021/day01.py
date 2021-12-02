#f = open('data/day1-sample.txt', 'r')
f = open('data/day1-final.txt', 'r')


def part1(depths):
    count = 0
    last = depths[0]
    for i in range(1, depths.__len__()):
        if depths[i] - last > 0:
            count += 1
        last = depths[i]

    return count


def part2(d):
    w = (d[0], d[1], d[2])
    seq = [sum(w)]

    for i in range(3, depths.__len__()):
        w = (w[1], w[2], d[i])
        seq.append(sum(w))

    return part1(seq)



depths = [int(x.strip()) for x in f]

print("part1: ", part1(depths))
print("part2: ", part2(depths))