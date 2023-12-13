import re

# f = open('data/day13-sample.txt', 'r')
f = open('data/day13-final.txt', 'r')


def check_horizontal(map, max_error=0, reflection_line=-1):
    pivot = 0
    for i in range(1, len(map[0])):
        if i == reflection_line:
            continue

        pivot = i
        f, b = pivot, pivot - 1 # forward, backward indexes

        valid_pivot = True
        errors_allowed = max_error
        error = None
        while f < len(map[0]) and b >= 0:
            for j in range(0, len(map)):
                if map[j][f] != map[j][b]:
                    errors_allowed -= 1
                    error = (j, f, b)
                    if errors_allowed < 0:
                        valid_pivot = False
                        break

            if valid_pivot:
                f += 1
                b -= 1
            else:
                break

        if valid_pivot and errors_allowed == 0:
            # print('pivot', pivot, error)
            return pivot

    return 0


def part1(maps):
    total_left = 0
    total_top = 0

    for m in maps:
        l = check_horizontal(m)
        t = check_horizontal(list(map(list, zip(*m))))
        total_left += l
        total_top += t

    return total_left + (100 * total_top)


def part2(maps):
    total_left = 0
    total_top = 0

    for m in maps:
        # only the solutions with exactly 1 error are valid
        total_left += check_horizontal(m, 1, -1)
        total_top += check_horizontal(list(map(list, zip(*m))), 1, -1)

    return total_left + (100 * total_top)


def print_map(m):
    for l in m:
        print(l)
    print()


lines = [l.strip() for l in f]
maps = []
current_map = []
for l in lines:
    if l == '':
        maps.append(current_map)
        current_map = []
    else:
        current_map.append(l)
maps.append(current_map)

# [print_map(m) for m in maps]

print("part1: ", part1(maps))
print("part2: ", part2(maps))
