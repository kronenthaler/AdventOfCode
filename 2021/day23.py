import heapq
import re
import copy
import math
from functools import reduce
from queue import PriorityQueue as queue


# f = open('data/day23-sample.txt', 'r')
f = open('data/day23-final.txt', 'r')


def reachable(b, p, t):
    p_x = p[1]
    t_x = t[1]
    for i in range(min(p_x, t_x), max(p_x, t_x)+1):
        if b[1][i] != '.':
            return None, 0
    return t, abs(min(p_x, t_x) - max(p_x, t_x))


def route_from_hall(b, l, p, t):  # board, letter, position ,targets
    b[p[0]][p[1]] = '.'
    try:
        possible, v = reachable(b, p, t[0])
        if not possible:
            return None, 0

        empty = 0
        same = 0
        other = 0
        for x in t:  # row, column
            if b[x[0]][x[1]] == l:
                same += 1
            elif b[x[0]][x[1]] == '.':
                empty += 1
            else:
                other += 1

        if other != 0:
            return None, 0

        return (t[0][0] - same, t[0][1]), abs(min(p[1], t[0][1]) - max(p[1], t[0][1])) + empty
    finally:
        b[p[0]][p[1]] = l


def route_to_hall(b, l, p, t):
    for i in range(1, p[0]):
        if b[i][p[1]] != '.':
            return None, 0
    return (1, p[1]), abs(p[0] - 1)


def direct_route(b, l, p, t):
    pth, cth = route_to_hall(b, l, p, t)
    pfh, cfh = route_from_hall(b, l, p, t)
    if pth and pfh:
        return pfh, cth + cfh
    return None, 0


# cost per letter
costs = {'A': 1, 'B': 10, 'C': 100, 'D':1000}

# cannot stop at gates
gates = [(1, 3), (1, 5), (1, 7), (1, 9)]

# places were is allowed to wait (if empty)
waiting_positions = [(1, x) for x in range(1, 12) if x not in [3, 5, 7, 9]]


def part1(board):
    targets = {
        'A': [(3, 3), (2, 3)],
        'B': [(3, 5), (2, 5)],
        'C': [(3, 7), (2, 7)],
        'D': [(3, 9), (2, 9)],
    }

    return astar(board, targets)


def astar(board, targets):
    # node: (letter, position, state) ; state: 0: waiting to leave, 1: in hall, -1: done
    positions = reduce(lambda a, x: a + x, [p for p in targets.values()], [])
    N = len(positions)

    nodes = []
    for p in positions:
        l = board[p[0]][p[1]]
        s = -1 if p == targets[l][0] or (p == targets[l][1] and board[targets[l][0][0]][targets[l][0][1]] == l) else 0
        nodes.append((l, p, s))

    nodes = sorted(nodes, key=lambda x: x[0], reverse=True)
    start = (tuple(nodes), flat_board(board), 0)
    opened = []
    heapq.heappush(opened, (heuristic(nodes, targets), start))
    closed = {}  # state, cost
    opened_hash = { start[1]: heuristic(nodes, targets) }  # state, cost
    iteration = 0
    paths = {}  # state, previous board

    best = math.inf
    while len(opened):
        current = heapq.heappop(opened)
        h_cost, state = current
        nodes_t, board_str, cost = state

        closed[board_str] = h_cost
        if board_str in opened_hash:
            del opened_hash[board_str]

        nodes = list(nodes_t)
        mutable_board = inflate_board(board_str)

        in_position = sum(1 for _,_,s in nodes if s == -1)
        if in_position == N:  # it's a solution
            traverse_path(flat_board(mutable_board), paths)
            return cost

        # generate candidates
        candidates = []
        # nodes should be positional to avoid problems
        for i in range(len(nodes)):
            l,p,s = nodes[i]
            if s == -1: continue
            if s == 0:  # waiting
                # state 1: if there is direct route
                new_p, new_cost = direct_route(mutable_board, l, p, targets[l])
                if new_p:
                    candidates.append(generate_state(mutable_board, i, new_p, cost, new_cost*costs[l], -1, nodes, targets))
                else:
                    # state 2: no direct route, but can wait in the halls
                    new_p, new_cost = route_to_hall(mutable_board, l, p, targets[l])
                    if new_p:
                        for wp in waiting_positions:
                            if mutable_board[wp[0]][wp[1]] != '.': continue
                            target_p, target_c = reachable(mutable_board, new_p, wp)
                            if target_p:
                                candidates.append(generate_state(mutable_board, i, target_p, cost, (new_cost+target_c) * costs[l], 1, nodes, targets))
            if s == 1:  # in the hall
                new_p, new_cost = route_from_hall(mutable_board, l, p, targets[l])
                if new_p:
                    candidates.append(generate_state(mutable_board, i, new_p, cost, new_cost*costs[l], -1, nodes, targets))

        for new_cost, new_state in candidates:
            if new_state[1] in closed:
                if closed[new_state[1]] < new_cost:
                    continue
                del closed[new_state[1]]

            if new_state[1] in opened_hash:
                if opened_hash[new_state[1]] < new_cost:
                    continue
                del opened_hash[new_state[1]]
                for i, (_, b, _) in enumerate(opened):
                    if b == new_state[1]:
                        del opened[i]
                        heapq.heapify(opened)
                        break

            paths[new_state[1]] = board_str  # store the path for reconstruction
            heapq.heappush(opened, (new_cost, new_state))
            opened_hash[new_state] = new_cost

    return best


def generate_state(board, i, new_p, cost, new_cost, new_s, nodes, targets):
    l, p, s = nodes[i]
    new_board = copy.deepcopy(board)
    new_board[p[0]][p[1]] = '.'
    new_board[new_p[0]][new_p[1]] = l
    new_nodes = copy.deepcopy(nodes)
    new_nodes[i] = (l, new_p, new_s)
    return cost + new_cost + heuristic(new_nodes, targets), (tuple(new_nodes), flat_board(new_board), cost + new_cost)


def heuristic(nodes, targets):
    return sum([(len(targets[l]) + abs(p[0] - 1) + abs(p[1] - targets[l][0][1]) + 1) * costs[l] for l, p in [(l1, p) for l1, p, s in nodes if s != -1]])


def flat_board(b):
    return "\n".join(["".join(l) for l in b])


def inflate_board(b):
    return [list(l) for l in b.split('\n')]


def traverse_path(board, paths):
    if board in paths:
        parent = paths[board]
        traverse_path(parent, paths)
        print(board)
        print()
    else:
        print("*"*100, "\n", "start path:")
        print(board)
        print()


def part2(board):
    targets = {
        'A': [(5, 3), (4, 3), (3, 3), (2, 3)],
        'B': [(5, 5), (4, 5), (3, 5), (2, 5)],
        'C': [(5, 7), (4, 7), (3, 7), (2, 7)],
        'D': [(5, 9), (4, 9), (3, 9), (2, 9)],
    }

    extras = [list("###D#C#B#A###"), list("###D#B#A#C###")]
    return astar(board[0:3] + extras + board[3:], targets)


board = [l[0:-1].replace(' ', '#') + '#' * (13 - (len(l) - 1)) for l in f]
[print(l) for l in board]

print('part1: ', part1(copy.deepcopy(board)))
print('part2: ', part2(copy.deepcopy(board)))
