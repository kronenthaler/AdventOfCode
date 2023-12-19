import copy
import re
import math
import heapq

f = open('data/day17-sample.txt', 'r')
# f = open('data/day17-final.txt', 'r')


steps = [(1,0), (-1,0), (0,1), (0,-1)]

dsymbol = ['>', 'v', '<', '^']

RIGHT=(0, 1, 0)
DOWN=(1, 0, 1)
LEFT=(0, -1, 2)
UP=(-1, 0, 3)

R=0
D=1
L=2
U=3

directions = [  # (i,j, d-index)
    # straight, left,  right
    [RIGHT, UP, DOWN],  # 0: right >
    [DOWN, LEFT, RIGHT],  # 1: down v
    [LEFT, UP, DOWN],  # 2: left <
    [UP, LEFT, RIGHT]   # 3: up ^
]


def print_path(path, b, target):
    board = copy.deepcopy(b)
    current = target
    while current != (0, 0):
        i, j, d = path[current[0]][current[1]]
        board[i][j] = dsymbol[d]
        current = i, j

    [print("".join(str(x) for x in l)) for l in board]


def heuristic(src, target):
    return abs(src[0] - target[0]) + abs(src[1] - target[1])


def part1(board):
    target = len(board)-1, len(board[0])-1

    # A* approach
    # state: (cost, (i, j, d-index), path)
    # opened = PriorityQueue() # or heap
    opened = []
    heapq.heappush(opened, (heuristic((0, 0), target), ((0, 0), R, 0, "")))
    heapq.heappush(opened, (heuristic((0, 0), target), ((0, 0), D, 0, "")))
    closed = {}  # state -> cost
    opened_hash = {
        (0, 0): heuristic((0, 0), target),
    }

    while len(opened) > 0:
        h_cost, (pos, d, cost, path) = heapq.heappop(opened)
        i, j = pos

        print(pos, target, h_cost, cost, len(opened), len(closed))

        closed[pos] = h_cost
        if pos in opened_hash:
            del opened_hash[pos]

        if pos == target:
            [print(dsymbol[int(d)], end='') for d in path]  # path as a string is easier to append
            print()
            return cost  # 1007 too high

        # generate candidates
        candidates = []  # h_cost, ((i,j), d-index, cost, path)
        start_range = 1 if len(path) >= 3 and path[-1] == path[-2] == path[-3] == str(d) else 0
        for sx, sy, nd in directions[d][start_range:]:
            ni, nj = i + sx, j + sy
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                new_cost = cost + board[ni][nj]
                new_h_cost = heuristic((ni, nj), target) + new_cost
                new_state = (ni, nj), nd, new_cost, path + str(nd)
                candidates.append((new_h_cost, new_state))

        # end generation
        for new_h_cost, new_state in candidates:
            pos, _, _, _ = new_state
            if pos in closed:
                if closed[pos] < new_h_cost:
                    continue
                del closed[pos]

            if pos in opened_hash:
                if opened_hash[pos] < new_h_cost:
                    continue
                del opened_hash[pos]
                for i, (_, (open_pos, _, _, _)) in enumerate(opened):
                    if open_pos == pos:
                        del opened[i]
                        heapq.heapify(opened)
                        break

            heapq.heappush(opened, (new_h_cost, new_state))
            opened_hash[pos] = new_h_cost


    print(opened)


def part2(l):
    pass


lines = [list(map(int, list(l.strip()))) for l in f]
print(lines)

print("part1: ", part1(lines))
print("part2: ", part2(lines))
