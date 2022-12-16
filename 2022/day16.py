import re

# f = open('data/day16-sample.txt', 'r')
f = open('data/day16-final.txt', 'r')


def dfs(current, G, W, t, pressure, opened, max_pressure, path):
    if len(opened) == len(G):
         return pressure

    edges = [e for e, w in W[current].items() if w != 0]
    for e in edges:
        r, _ = G[e]
        w = W[current][e]
        if e not in opened:
            max_pressure = max(max_pressure, dfs(e, G, W, t-w-1, pressure + ((t-w-1) * r), set(list(opened) + [e]), max_pressure, path + '->' + e) if t - w - 1 >= 0 else pressure)

    return max_pressure


# way too slow... but it finishes
# hints: https://github.com/davearussell/advent2022/blob/master/day16/solve.py
def dfs2(current, G, W, t, pressure, opened, max_pressure):
    if len(opened) == len(G):
        return pressure

    actor = 0 if t[0] > t[1] else 1  # actor with the most time to go
    s = current[actor]

    # current and tt are tuples
    edges = [e for e, w in W[s].items() if w != 0]
    for e in edges:
        r, _ = G[e]
        w = W[s][e]
        if e not in opened:
            new_time = t[actor]-w-1
            max_pressure = max(max_pressure, dfs2((e, current[1-actor]), G, W, (new_time, t[1-actor]), pressure + (new_time * r), set(list(opened) + [e]), max_pressure) if new_time >= 0 else pressure)

    return max_pressure


def fw(G):
    # need to create the floyd warshall version of the graph
    W = {}
    for s, _ in G.items():
        W[s] = {}
        for d, _ in G.items():
            W[s][d] = 99999 if s != d else 0

    for s, (w, edges) in G.items():
        for e in edges:
            W[s][e] = 1

    for k in W.keys():
        for j in W.keys():
            for i in W.keys():
                if (i not in W or j not in W[i]) or W[i][j] > W[i][k] + W[k][j]:
                    W[i][j] = W[i][k] + W[k][j]
    return W


def part1(G, W, t):
    opened = set([s for s, (r, _) in graph.items() if r == 0])
    return dfs('AA', G, W, t, 0, opened, 0, "AA")


def part2(G, W, tt):
    opened = set([s for s, (r, _) in graph.items() if r == 0])
    return dfs2(('AA', 'AA'), G, W, tt, 0, opened, 0)


graph = {}
for l in f:
    matches = re.findall(r'([A-Z]{2}|[0-9]+)', l)
    src = matches[0]
    rate = int(matches[1])
    dst = matches[2:]
    graph[src] = (rate, dst)

W = fw(graph)

print("part1: ", part1(graph, W, 30))
print("part2: ", part2(graph, W, (26, 26)))
