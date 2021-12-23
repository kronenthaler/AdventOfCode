import heapq
import re
import copy
import math
from functools import reduce
from queue import PriorityQueue as queue


# f = open('data/day23-sample.txt', 'r')
f = open('data/day23-final.txt', 'r')

def reachable(b, p, t):
    for i in range(min(p[1], t[1]), max(p[1], t[1])+1):
        if b[1][i] != '.':
            return None, 0
    return t, abs(min(p[1], t[1]) - max(p[1], t[1]))

def route_from_hall(b, l, p, t):  # board, letter, position ,targets
    b[p[0]][p[1]] = '.'
    try:
        for i in range(min(p[1], t[0][1]), max(p[1], t[0][1])+1):
            if b[1][i] != '.':
                return None, 0
        if b[t[0][0]][t[0][1]] == l and b[t[1][0]][t[1][1]] == '.':
            return t[1], abs(min(p[1], t[0][1]) - max(p[1], t[0][1])) + 1
        if b[t[0][0]][t[0][1]] == '.' and b[t[1][0]][t[1][1]] == '.':
            return t[0], abs(min(p[1], t[0][1]) - max(p[1], t[0][1])) + 2
        return None, 0
    finally:
        b[p[0]][p[1]] = l


def route_to_hall(b, l, p, t):
    if b[p[0]-1][p[1]] == '.':
        return (1, p[1]), abs(p[0] - 1)
    return None, 0

def direct_route(b, l, p, t):
    pth, cth = route_to_hall(b,l,p,t)
    pfh, cfh = route_from_hall(b,l,p,t)
    if pth and pfh:
        return pfh, cth + cfh
    return None, 0

def part1(board):
    targets = {
        'A': [(3, 3), (2, 3)],
        'B': [(3, 5), (2, 5)],
        'C': [(3, 7), (2, 7)],
        'D': [(3, 9), (2, 9)],
    }

    costs = {'A': 1, 'B': 10, 'C': 100, 'D':1000}

    # cannot stop in a gate
    gates = [(1,3), (1,5), (1,7), (1,9)]
    # places were is allowed to wait (if empty)
    waiting_positions = [(1, x) for x in range(1, 12) if x not in [3, 5, 7, 9]]

    # node: (letter, position, state) ; state: 0: waiting to leave, 1: in hall, -1: done
    positions = reduce(lambda a, x: a + x, [p for p in targets.values()], [])

    # print(route_from_hall(new_board, 'B', (1, 4), targets['B']))
    # print(route_to_hall(new_board, 'B', (3,5), targets["B"]))

    # new_board = inflate_board(flat_board(board))
    # print(reachable(new_board, (3,9), (1,10)))
    # print(route_from_hall(new_board, 'A', (1,10), targets['A']))
    # print(route_to_hall(new_board, 'A', (3,9), (1, 9)))
    # print(direct_route(new_board, 'A', (3,9), targets['A']))
    # if True: return 0
    nodes = []
    for p in positions:
        l = board[p[0]][p[1]]
        s = -1 if p == targets[l][0] or (p == targets[l][1] and board[targets[l][0][0]][targets[l][0][1]] == l) else 0
        nodes.append((l, p, s))

    nodes = sorted(nodes, key=lambda x: x[0], reverse=True)
    print(nodes)
    start = (tuple(nodes), flat_board(board))
    opened = []
    heapq.heappush(opened, (0, start))
    closed = {} # state, cost
    iteration = 0

    best = math.inf
    while len(opened):
        current = heapq.heappop(opened)
        cost, state = current
        nodes_t, board_str = state

        closed[board_str] = cost

        nodes = list(nodes_t)
        mutable_board = inflate_board(board_str)

        in_position = sum(1 for _,_,s in nodes if s == -1)

        iteration += 1
        # if cost in [8008, 8010]:
        if iteration % 10000 == 0:
            print(cost, iteration, in_position)
            # print(board_str)
            # print(nodes_t)
            # print()

        if in_position == 8:  # it's a solution
            return cost, nodes, board

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
                    candidates.append(generate_state(mutable_board, i, new_p, cost, new_cost*costs[l], -1, nodes))
                else:
                    # state 2: no direct route, but can wait in the halls
                    new_p, new_cost = route_to_hall(mutable_board, l, p, targets[l])
                    if new_p:
                        for wp in waiting_positions:
                            if mutable_board[wp[0]][wp[1]] != '.': continue
                            target_p, target_c = reachable(board, new_p, wp)
                            if target_p:
                                candidates.append(generate_state(mutable_board, i, target_p, cost, (new_cost+target_c)*costs[l], 1, nodes))
            if s == 1:  # in the hall
                new_p, new_cost = route_from_hall(mutable_board, l, p, targets[l])
                if new_p:
                    candidates.append(generate_state(mutable_board, i, new_p, cost, new_cost*costs[l], -1, nodes))

        for new_cost, new_state in candidates:
            if new_state[1] in closed:
                if closed[new_state[1]] < new_cost:
                    continue
                del closed[new_state[1]]

            heapq.heappush(opened, (new_cost, new_state))
    return best


def generate_state(board, i, new_p, cost, new_cost, new_s, nodes):
    l, p, s = nodes[i]
    new_board = copy.deepcopy(board)
    new_board[p[0]][p[1]] = '.'
    new_board[new_p[0]][new_p[1]] = l
    new_nodes = copy.deepcopy(nodes)
    new_nodes[i] = (l, new_p, new_s)

    #TODO: add the heuristic cost!!!
    return (cost + new_cost, (tuple(new_nodes), flat_board(new_board)))


def flat_board(b):
    return "\n".join(["".join(l) for l in b])


def inflate_board(b):
    return [list(l) for l in b.split('\n')]


def part2(input):
    pass


board = [l[0:-1].replace(' ', '#') + '#' * (13 - (len(l) - 1)) for l in f]
[print(l) for l in board]

print('part1: ', part1(copy.deepcopy(board)))
print('part2: ', part2(copy.deepcopy(board)))
