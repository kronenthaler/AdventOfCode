# f = open('day12-sample.txt', 'r')
f = open('day12-final.txt', 'r')

content = [(l[0], int(l[1:])) for l in f]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # nesw
L = {90: 3, 180: 2, 270: 1}

def rotate(current, angle):
    if angle == 90:
        return current[1], -current[0]
    if angle == 180:
        return -current[0], -current[1]
    if angle == 270:
        return -current[1], current[0]
    return current

def part1(direction, steps):
    start = (0, 0)
    for s in steps:
        inc = dir[direction]
        if s[0] == 'F':
            start = (start[0] + inc[0] * s[1], start[1] + inc[1] * s[1])
        elif s[0] == 'N':
            start = (start[0], start[1] + s[1])
        elif s[0] == 'S':
            start = (start[0], start[1] - s[1])
        elif s[0] == 'E':
            start = (start[0] + s[1], start[1])
        elif s[0] == 'W':
            start = (start[0] - s[1], start[1])
        elif s[0] == 'R':
            direction = (direction + (s[1] // 90)) % 4
        elif s[0] == 'L':
            direction = (direction + L[s[1]]) % 4
    return abs(start[0]) + abs(start[1])


def part2(start_direction, waypoint,  steps):
    start = (0, 0)
    for s in steps:
        print(start, waypoint)
        if s[0] == 'F':
            start = (start[0] + waypoint[0] * s[1], start[1] + waypoint[1] * s[1])
        elif s[0] == 'N':
            waypoint = (waypoint[0], waypoint[1] + s[1])
        elif s[0] == 'S':
            waypoint = (waypoint[0], waypoint[1] - s[1])
        elif s[0] == 'E':
            waypoint = (waypoint[0] + s[1], waypoint[1])
        elif s[0] == 'W':
            waypoint = (waypoint[0] - s[1], waypoint[1])
        elif s[0] == 'R':
            waypoint = rotate(waypoint, s[1])
        elif s[0] == 'L':
            waypoint = rotate(waypoint, L[s[1]] * 90)

    return abs(start[0]) + abs(start[1])

print('part1: ', part1(1, content))
print('part2: ', part2(1, (10, 1), content))
