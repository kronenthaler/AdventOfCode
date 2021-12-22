import math
import re
import copy

# f = open('data/day22-sample.txt', 'r')
f = open('data/day22-final.txt', 'r')


def part1(inst, bound):
    grid = {}

    for v, (minx, maxx), (miny, maxy), (minz, maxz) in inst:
        if -bound > minx or minx > bound or \
           -bound > miny or miny > bound or \
           -bound > minz or minz > bound or \
           -bound > maxx or maxx > bound or \
           -bound > maxy or maxy > bound or \
           -bound > maxz or maxz > bound:
            continue

        for x in range(minx, maxx+1):
            for y in range(miny, maxy+1):
                for z in range(minz, maxz+1):
                    if v and (x,y,z) not in grid:
                        grid[(x,y,z)] = 1
                    elif not v and (x,y,z) in grid:
                        del grid[(x,y,z)]

    return len(grid)


class Cube:
    def __init__(self, on, x, y, z):
        self.min_x, self.max_x = min(x), max(x)
        self.min_y, self.max_y = min(y), max(y)
        self.min_z, self.max_z = min(z), max(z)
        self.on = on

        self.volume = (self.max_x - self.min_x + 1) * (self.max_y - self.min_y + 1) * (self.max_z - self.min_z + 1)

    def intersect(self, other):
        if self.max_x < other.min_x or self.min_x > other.max_x or \
           self.max_y < other.min_y or self.min_y > other.max_y or \
           self.max_z < other.min_z or self.min_z > other.max_z:
            return None

        return Cube(other.on if self.on != other.on else not other.on,
            (min(self.max_x, other.max_x), max(self.min_x, other.min_x)),
            (min(self.max_y, other.max_y), max(self.min_y, other.min_y)),
            (min(self.max_z, other.max_z), max(self.min_z, other.min_z)))


def part2(inst):
    regions = [Cube(v, x, y, z) for v, x,y,z in inst]
    processed = []

    for i, region in enumerate(regions):
        next_processed = []

        for previous in processed:
            next_processed.append(previous)
            if overlap := previous.intersect(region):
                next_processed.append(overlap)

        if region.on:
            next_processed.append(region)

        processed = next_processed

    return sum(region.volume if region.on else -region.volume for region in processed)

regex = r'(on|off) x=([-]?[0-9]*)..([-]?[0-9]*),y=([-]?[0-9]*)..([-]?[0-9]*),z=([-]?[0-9]*)..([-]?[0-9]*)'
inst = []
for l in f:
    groups = re.match(regex, l)
    s, minx, maxx, miny, maxy, minz, maxz = groups.groups()
    inst.append((groups[1] == 'on', (int(minx), int(maxx)), (int(miny), int(maxy)), (int(minz), int(maxz))))

print('part1: ', part1(copy.deepcopy(inst), 50))
print('part2: ', part2(copy.deepcopy(inst)))
