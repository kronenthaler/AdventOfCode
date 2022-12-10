import re

# f = open('data/day10-sample.txt', 'r')
f = open('data/day10-final.txt', 'r')


def part1(l):
    x = 1
    cycle = 1
    inst_ptr = 0
    first_tick = True
    total = 0
    display = ""
    while inst_ptr < len(l):
        ins = l[inst_ptr]
        if cycle in [20, 60, 100, 140, 180, 220]:
            total += x * cycle

        # draw pixel
        display += "▓" if (cycle-1) % 40 in [x-1, x, x+1] else " "

        if ins != 'noop':
            if first_tick:
                first_tick = False
                inst_ptr -= 1
            else:
                first_tick = True
                x += int(ins.split(' ')[1])

        inst_ptr += 1
        cycle += 1

    return total, display


def part2(l):
    _, display = part1(l)
    return "\n"+"\n".join([display[i: i+40] for i in range(0, len(display), 40)])


lines = [l.strip() for l in f]

print("part1: ", part1(lines)[0])
print("part2: ", part2(lines))
