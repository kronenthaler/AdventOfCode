import re
from functools import cmp_to_key

# f = open('data/day18-sample.txt', 'r'); n=10
f = open('data/day18-final.txt', 'r'); n=25

def sort_p(a, b):
    ax, ay, az = a
    bx, by, bz = b
    if ax != bx: return ax - bx
    if ay != by: return ay - by
    return az - bz

face_inc = [
    [(0, 0, 0), (1, 0, 0), (1, -1, 0), (0, -1, 0)],  # f1
    [(0, 0, 0), (0, 0, 1), (1, 0, 1), (1, 0, 0)],    # f2
    [(1, 0, 0), (1, 0, 1), (1, -1, 1), (1, -1, 0)],  # f3
    [(0, -1, 0), (0, -1, 1), (1, -1, 1), (1, -1, 0)],# f4
    [(0, 0, 0), (0, 0, 1), (0, -1, 1), (0, -1, 0)],  # f5
    [(0, 0, 1), (1, 0, 1), (1, -1, 1), (0, -1, 1)]   # f6
]
incs = [(0, 0, -1), (0, 1, 0), (1, 0, 0), (0, -1, 0), (-1, 0, 0), (0, 0, 1)]


def make_face(vx, vy, vz, t):
    face = set()
    for x, y, z in face_inc[t]:
        face.add((vx + x, vy + y, vz + z))
    s_faces = list(face)
    sorted(s_faces, key=cmp_to_key(sort_p))
    return s_faces


def faces(vx, vy, vz):
    result = []
    for i in range(0, len(face_inc)):
        result.append(make_face(vx, vy, vz, i))
    return result


def part1(l):
    cubes = set()
    collisions = set()
    for v in l:
        fs = list(map(str, faces(*v)))
        collisions.update(set([f for f in fs if f in cubes]))
        cubes.update(set(fs))
    return len(cubes) - len(collisions), cubes, collisions


# flood from the outside
def part2(l):
    open_faces, cubes, collisions = part1(l)

    queue = [(-1,-1,-1)]
    visited = set()
    external = set()
    while len(queue) != 0:
        vx, vy, vz = queue.pop(0)

        for i in range(0, len(incs)):
            x,y,z = incs[i]

            f = make_face(vx, vy, vz, i).__str__()
            if f in cubes:
                external.add(f)

            new_voxel = vx+x, vy+y, vz+z
            if new_voxel not in visited and new_voxel not in l and -1 <= vx < n and -1 <= vy < n and -1 <= vz < n:
                visited.add(new_voxel)
                queue.append(new_voxel)

    return len(external)


lines = [tuple(list(map(int, l.strip().split(',')))) for l in f]

# print(part1([(1,1,1), (2, 1, 1)]))
print("part1: ", part1(lines)[0])
print("part2: ", part2(lines))
