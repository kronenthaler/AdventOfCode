import re
from copy import deepcopy

# f = open('data/day14-sample.txt', 'r')
f = open('data/day14-final.txt', 'r')


def fall(x, y, board):
    for i in range(0, len(board)):
        if x+1 >= len(board):
            return True

        if board[x+1][y] == '.':
            x += 1
            continue

        if (board[x+1][y] == 'o' or board[x+1][y] == '#') and \
            (board[x+1][y+1] == 'o' or board[x+1][y+1] == '#') and \
            (board[x+1][y-1] == 'o' or board[x+1][y-1] == '#'):
            board[x][y] = 'o'
            return x == 0 and y == 500

        if board[x+1][y-1] != 'o' and board[x+1][y-1] != '#':
            y -= 1
            x += 1
            continue

        if board[x+1][y+1] != 'o' and board[x+1][y+1] != '#':
            y += 1
            x += 1
            continue

    return False


def part1(board):
    while True:
        if fall(0, 500, board):
            break

    # [print("".join(l)) for l in board]
    return sum([1 for i in range(0, len(board)) for j in range(0, len(board[0])) if board[i][j] == 'o'])


lines = []
minx = 1000000
miny = 1000000
maxx = 0
maxy = 0
walls = []
for l in f:
    matches = re.findall(r'(([0-9]+),([0-9]+)( ->)*)+', l.strip())
    path = []
    for i in range(0, len(matches)):
        point = (int(matches[i][2]), int(matches[i][1]))
        minx = min(minx, point[0])
        maxx = max(maxx, point[0])
        miny = min(miny, point[1])
        maxy = max(maxy, point[1])
        path.append(point)
    walls.append(path)

board = [['.'] * ((2*maxy) + 1) for i in range(0, maxx + 1)]
for path in walls:
    for p in range(0, len(path)-1):
        p1 = path[p]
        p2 = path[p+1]
        n = abs(p1[0] - p2[0]) + abs(p1[1] - p2[0])
        if p1[0] != p2[0]:
            inc = (1, 0) if p1[0] < p2[0] else (-1, 0)
        else:
            inc = (0, 1) if p1[1] < p2[1] else (0, -1)

        current = p1
        board[p1[0]][p1[1]] = '#'
        board[p2[0]][p2[1]] = '#'
        while current != p2:
            board[current[0]+inc[0]][current[1]+inc[1]] = '#'
            current = current[0] + inc[0], current[1] + inc[1]


print("part1: ", part1(deepcopy(board)))
board.append(['.']*len(board[0]))
board.append(['#']*len(board[0]))
print("part2: ", part1(deepcopy(board)))
