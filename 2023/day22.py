import re

# f = open('data/day22-sample.txt', 'r')
f = open('data/day22-final.txt', 'r')


def articulation_points(graph, start):
    unsafe = set()
    total = 0
    for node in graph.keys():
        if node == start:
            continue

        visited = set([node, start])
        q = [start]
        while len(q) > 0:
            current = q.pop(0)
            candidates = [e for e in graph[current] if e not in visited]
            q.extend(candidates)
            visited.update(candidates)

        if len(visited) != len(graph):
            unsafe.add(node)
            total += len(graph) - len(visited)
    return unsafe, total


def max_at_range(zindex, x0, x1, y0, y1):
    maxz = max([zindex[y][x][0] for x in range(x0, x1+1) for y in range(y0, y1+1)])

    # collect matching contact points (index)
    contact_points = [zindex[y][x][1] for x in range(x0, x1+1) for y in range(y0, y1+1) if zindex[y][x][0] == maxz]

    return maxz, contact_points


def create_graph(blocks):
    # build the graph on the go?
    graph = {}

    # find min, max for x & y -> area of action
    minx, miny = 0, 0
    maxx, maxy = 0, 0
    for name, ((x0, y0, _), (x1, y1, _)) in blocks:
        minx = min(minx, x0, x1)
        miny = min(miny, y0, y1)
        maxx = max(maxx, x0, x1)
        maxy = max(maxy, y0, y1)
        graph[name] = set()

    # need to have a max depth at each x,y, position available
    zindex = [[(0, -1) for i in range(minx, maxx+2)] for j in range(miny, maxy+2)]  # depth, name

    # sort the list by z: name, ((x,y,z), (x,y,z))
    # name: 0, rect: 1
    # p0: 0, p1: 1
    # x: 0, y: 1, z: 2
    blocks.sort(key=lambda x: x[1][0][2])

    # need to be able to get the max depth on an area over x,y
    for name, ((x0, y0, z0), (x1, y1, z1)) in blocks:
        maxz, contact_points = max_at_range(zindex, x0, x1, y0, y1)

        # update the graph (with supporting blocks!)
        for index in contact_points:
            if index not in graph:
                graph[index] = set()
            graph[index].add(name)

        # update zindex with this block new depth
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                zindex[y][x] = (maxz + (z1 - z0 + 1), name)

    # find the articulation points
    points, total = articulation_points(graph, -1)
    return len(graph) - 1 - len(points), total


lines = [tuple([x.strip() for x in l.split('~')]) for l in f]
lines = [(tuple(map(int, start.split(','))), tuple(map(int, end.split(',')))) for start, end in lines]
lines = list(zip(range(len(lines)), lines))

points, total = create_graph(lines)

print("part1: ", points)
print("part2: ", total)
