import math
import re
import copy

# f = open('data/day22-sample.txt', 'r')
f = open('data/day22-final.txt', 'r')


def part1(inst, bound):
    grid = {}

    for v, (minx, maxx, miny, maxy, minz, maxz) in inst:
        if -bound > minx or minx > bound or \
           -bound > miny or miny > bound or \
           -bound > minz or minz > bound or \
           -bound > maxx or maxx > bound or \
           -bound > maxy or maxy > bound or \
           -bound > maxz or maxz > bound:
            continue

        for x in range(minx, maxx):
            for y in range(miny, maxy):
                for z in range(minz, maxz):
                    if v and (x,y,z) not in grid:
                        grid[(x,y,z)] = 1
                    elif not v and (x,y,z) in grid:
                        del grid[(x,y,z)]

    return len(grid)


def area(c):
    return abs(c[0]-c[1]) * abs(c[2]-c[3]) * abs(c[4]-c[5])


def overlaps(a, b):
    a_x_from, a_x_to, a_y_from, a_y_to, a_z_from, a_z_to = a
    b_x_from, b_x_to, b_y_from, b_y_to, b_z_from, b_z_to = b
    return not (
        b_x_to <= a_x_from or a_x_to <= b_x_from or \
        b_y_to <= a_y_from or a_y_to <= b_y_from or \
        b_z_to <= a_z_from or a_z_to <= b_z_from
    )


def split_overlapping_cube(overlapping_cube, cube_to_split):
    # print(f'<{overlapping_cube}>, <{cube_to_split}>')
    a_x_from, a_x_to, a_y_from, a_y_to, a_z_from, a_z_to = overlapping_cube
    b_x_from, b_x_to, b_y_from, b_y_to, b_z_from, b_z_to = cube_to_split

    intersect_start_x, intersect_end_x = max(a_x_from, b_x_from), min(a_x_to, b_x_to)
    intersect_start_y, intersect_end_y = max(a_y_from, b_y_from), min(a_y_to, b_y_to)
    intersect_start_z, intersect_end_z = max(a_z_from, b_z_from), min(a_z_to, b_z_to)

    min_x, max_x = min(a_x_from, b_x_from), max(a_x_to, b_x_to)
    min_y, max_y = min(a_y_from, b_y_from), max(a_y_to, b_y_to)
    min_z, max_z = min(a_z_from, b_z_from), max(a_z_to, b_z_to)

    extends_left_x, extends_right_x = b_x_from < intersect_start_x, b_x_to > intersect_end_x
    extends_left_y, extends_right_y = b_y_from < intersect_start_y, b_y_to > intersect_end_y
    extends_left_z, extends_right_z = b_z_from < intersect_start_z, b_z_to > intersect_end_z

    overlapping = intersect_start_x, intersect_end_x, intersect_start_y, intersect_end_y, intersect_start_z, intersect_end_z
    non_overlapping = []

    # 1:
    if extends_left_x:
        non_overlapping.append((min_x, intersect_start_x, intersect_start_y, intersect_end_y, intersect_start_z, intersect_end_z))
    if extends_left_y:
        non_overlapping.append((intersect_start_x, intersect_end_x, min_y, intersect_start_y, intersect_start_z, intersect_end_z))
    if extends_left_z:
        non_overlapping.append((intersect_start_x, intersect_end_x, intersect_start_y, intersect_end_y, min_z, intersect_start_z))
    if extends_right_x:
        non_overlapping.append((intersect_end_x, max_x, intersect_start_y, intersect_end_y, intersect_start_z, intersect_end_z))
    if extends_right_y:
        non_overlapping.append((intersect_start_x, intersect_end_x, intersect_end_y, max_y, intersect_start_z, intersect_end_z))
    if extends_right_z:
        non_overlapping.append((intersect_start_x, intersect_end_x, intersect_start_y, intersect_end_y, intersect_end_z, max_z))

    # 2:
    if extends_left_x:
        if extends_left_y:
            non_overlapping.append((min_x, intersect_start_x, min_y, intersect_start_y, intersect_start_z, intersect_end_z))
        if extends_right_y:
            non_overlapping.append((min_x, intersect_start_x, intersect_end_y, max_y, intersect_start_z, intersect_end_z))
        if extends_left_z:
            non_overlapping.append((min_x, intersect_start_x, intersect_start_y, intersect_end_y, min_z, intersect_start_z))
        if extends_right_z:
            non_overlapping.append((min_x, intersect_start_x, intersect_start_y, intersect_end_y, intersect_end_z, max_z))
    if extends_right_x:
        if extends_left_y:
            non_overlapping.append((intersect_end_x, max_x, min_y, intersect_start_y, intersect_start_z, intersect_end_z))
        if extends_right_y:
            non_overlapping.append((intersect_end_x, max_x, intersect_end_y, max_y, intersect_start_z, intersect_end_z))
        if extends_left_z:
            non_overlapping.append((intersect_end_x, max_x, intersect_start_y, intersect_end_y, min_z, intersect_start_z))
        if extends_right_z:
            non_overlapping.append((intersect_end_x, max_x, intersect_start_y, intersect_end_y, intersect_end_z, max_z))
    if extends_left_y:
        if extends_left_z:
            non_overlapping.append((intersect_start_x, intersect_end_x, min_y, intersect_start_y, min_z, intersect_start_z))
        if extends_right_z:
            non_overlapping.append((intersect_start_x, intersect_end_x, min_y, intersect_start_y, intersect_end_z, max_z))
    if extends_right_y:
        if extends_left_z:
            non_overlapping.append((intersect_start_x, intersect_end_x, intersect_end_y, max_y, min_z, intersect_start_z))
        if extends_right_z:
            non_overlapping.append((intersect_start_x, intersect_end_x, intersect_end_y, max_y, intersect_end_z, max_z))

    # 3:
    if extends_left_x and extends_left_y and extends_left_z:
        non_overlapping.append((min_x, intersect_start_x, min_y, intersect_start_y, min_z, intersect_start_z))
    if extends_left_x and extends_left_y and extends_right_z:
        non_overlapping.append((min_x, intersect_start_x, min_y, intersect_start_y, intersect_end_z, max_z))
    if extends_left_x and extends_right_y and extends_left_z:
        non_overlapping.append((min_x, intersect_start_x, intersect_end_y, max_y, min_z, intersect_start_z))
    if extends_left_x and extends_right_y and extends_right_z:
        non_overlapping.append((min_x, intersect_start_x, intersect_end_y, max_y, intersect_end_z, max_z))
    if extends_right_x and extends_left_y and extends_left_z:
        non_overlapping.append((intersect_end_x, max_x, min_y, intersect_start_y, min_z, intersect_start_z))
    if extends_right_x and extends_left_y and extends_right_z:
        non_overlapping.append((intersect_end_x, max_x, min_y, intersect_start_y, intersect_end_z, max_z))
    if extends_right_x and extends_right_y and extends_left_z:
        non_overlapping.append((intersect_end_x, max_x, intersect_end_y, max_y, min_z, intersect_start_z))
    if extends_right_x and extends_right_y and extends_right_z:
        non_overlapping.append((intersect_end_x, max_x, intersect_end_y, max_y, intersect_end_z, max_z))
    return overlapping, non_overlapping


def process_cube(is_on, current_cube, cubes):
    if area(current_cube) == 0:
        return cubes
    existing_overlapping = None
    new_cubes = cubes[:]
    for cube in new_cubes:
        if overlaps(current_cube, cube):
            existing_overlapping = cube
            break
    if not existing_overlapping:
        return new_cubes + [current_cube] if is_on else new_cubes
    new_cubes.remove(existing_overlapping)
    # Slices that are in the existing cube and not in this one
    # No cubes in cubes_on should ever already overlap, so we can safely add them back to the list
    _, non_overlap = split_overlapping_cube(current_cube, existing_overlapping)
    new_cubes.extend(non_overlap)

    # Slices that are in this cube and not in the existing one
    # Need to be reprocessed in case they overlap with more cubes
    overlap, non_overlap = split_overlapping_cube(existing_overlapping, current_cube)
    if is_on:
        new_cubes.append(overlap)
    for cube_slice in non_overlap:
        new_cubes = process_cube(is_on, cube_slice, new_cubes)
    return new_cubes


def part2(inst, bound):
    # inst = [(s, c) for s, c in inst if -bound <= c[0] <= bound and -bound <= c[1] <= bound and \
    #                                     -bound <= c[2] <= bound and -bound <= c[3] <= bound and \
    #                                     -bound <= c[4] <= bound and -bound <= c[5] <= bound]

    cubes_on = []
    for i, (s, cube) in enumerate(inst):
        print(i, '/', len(inst), len(cubes_on))
        cubes_on = process_cube(s, cube, cubes_on)

    return sum([area(c) for c in cubes_on])


regex = r'(on|off) x=([-]?[0-9]*)..([-]?[0-9]*),y=([-]?[0-9]*)..([-]?[0-9]*),z=([-]?[0-9]*)..([-]?[0-9]*)'
inst = []
for l in f:
    groups = re.match(regex, l)
    inst.append((groups[1] == 'on', (int(groups[2]),int(groups[3])+1,int(groups[4]),int(groups[5])+1,int(groups[6]),int(groups[7])+1)))

print('part1: ', part1(copy.deepcopy(inst), 50))
print('part2: ', part2(copy.deepcopy(inst), 50))
