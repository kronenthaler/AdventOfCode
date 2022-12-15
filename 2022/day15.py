import re
import time

# f = open('data/day15-sample.txt', 'r'); sample = 10; n=20
f = open('data/day15-final.txt', 'r'); sample = 2_000_000; n=4_000_000

def part1(sensors, target):
    matches = set()
    beacons = set()
    for s, dx, dy, b in sensors:
        # the ratio crosses the target line
        if s[1] + dx + dy < target or s[1] - (dx + dy) > target:
            continue

        # distance from the sensor to the target line
        h = abs(target - s[1])
        w = dx + dy - h
        for i in range(-w, w+1):
            matches.add((s[0]+i, target))

        if b[1] == target:
            beacons.add(b)

    return len(matches-beacons)


def part2(sensors, n):
    for sensor, dx, dy, _ in sensors:
        distance = dx + dy
        sx, sy = sensor
        for x in range(max(0, sx - distance - 1), min(n, sx + distance + 2)):
            for y in [sy + (distance + 1 - abs(x - sx)), sy - (distance + 1 - abs(x - sx))]:
                if y in range(n + 1):
                    for s, dx, dy, _ in sensors:
                        # check if the new point is inside any other range
                        if abs(x-s[0])+abs(y-s[1]) <= dx + dy:
                            break
                    else:
                        # stop as soon as the number is not contained
                        return x * n + y


sensors = []
for l in [l.strip() for l in f]:
    matches = re.match(r'Sensor at x=(-?[-0-9]*), y=(-?[0-9]*): closest beacon is at x=(-?[0-9]*), y=(-?[0-9]*)', l)
    s = int(matches[1]), int(matches[2])
    b = int(matches[3]), int(matches[4])
    sensors.append((s, abs(s[0] - b[0]), abs(s[1] - b[1]), b))

print("part1: ", part1(sensors, sample))
print("part2: ", part2(sensors, n))
