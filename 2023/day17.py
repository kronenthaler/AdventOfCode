import copy
import re
import math
import heapq

f = open('data/day17-sample.txt', 'r')
# f = open('data/day17-final.txt', 'r')


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
    # read up: https://cutonbuminband.github.io/AOC/qmd/2023.html#day-17-clumsy-crucible
    # dijsktra, however what matters are only the states where you turn, direction only need vertical/horizontal.

    target = len(board)-1, len(board[0])-1

    # A* approach
    # state: (cost, (i, j, d-index), path)
    # opened = PriorityQueue() # or heap
    opened = []
    heapq.heappush(opened, (heuristic((0, 0), target), ((0, 0, R), 0, "")))
    heapq.heappush(opened, (heuristic((0, 0), target), ((0, 0, D), 0, "")))
    closed = {}  # state -> cost
    opened_hash = {
        (0, 0, R): heuristic((0, 0), target),
        (0, 0, D): heuristic((0, 0), target),
    }

    while len(opened) > 0:
        h_cost, ((i, j, d), cost, path) = heapq.heappop(opened)

        print((i, j, d), target, h_cost, cost, path, len(opened), len(closed))

        closed[(i, j, d)] = h_cost
        if (i, j, d) in opened_hash:
            del opened_hash[(i, j, d)]

        if (i, j) == target:
            # [print(dsymbol[int(d)], end='') for d in path]  # path as a string is easier to append
            print(path)
            print(">>v>>>^>>>vv>>vv>vvv>vvv<vv>")
            return cost  # 1007 too high, 975 too high, 873 too low

        # generate candidates
        candidates = []  # h_cost, ((i,j), d-index, cost, path)
        start_range = 1 if len(path) >= 3 and path[-1] == path[-2] == path[-3] == dsymbol[d] else 0
        for sx, sy, nd in directions[d][start_range:]:
            ni, nj = i + sx, j + sy
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                new_cost = cost + board[ni][nj]
                new_h_cost = heuristic((ni, nj), target) + new_cost
                new_state = (ni, nj, nd), new_cost, path + dsymbol[nd]
                candidates.append((new_h_cost, new_state))

        # end generation
        for new_h_cost, new_state in candidates:
            new_pos, _, _ = new_state
            if new_pos in closed:
                if closed[new_pos] <= new_h_cost:
                    continue
                del closed[new_pos]

            # this part is cutting is pruning too much and missing the correct path
            # there is something with the definition of the state (pos + dir) could be too broad.
            # what else can be added?
            if new_pos in opened_hash:
                if opened_hash[new_pos] <= new_h_cost:
                    continue
                del opened_hash[new_pos]
                for i, (_, (open_pos, _, _)) in enumerate(opened):
                    if open_pos == new_pos:
                        del opened[i]
                        heapq.heapify(opened)
                        break

            heapq.heappush(opened, (new_h_cost, new_state))
            opened_hash[new_pos] = new_h_cost


    print(opened)


def part2(l):
    pass


lines = [list(map(int, list(l.strip()))) for l in f]
print(lines)

print("part1: ", part1(lines))
print("part2: ", part2(lines))
