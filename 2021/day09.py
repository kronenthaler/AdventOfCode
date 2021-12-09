import math

# f = open('data/day09-sample.txt', 'r')
f = open('data/day09-final.txt', 'r')
steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def part1(l):
    locations = []
    count = 0
    n = len(l)
    m = len(l[0])
    for i in range(n):
        for j in range(m):
            ref = l[i][j]
            neighbours = list([(sx, sy) for sx, sy in steps if i+sx < n and j+sy < m])
            if sum([1 for sx, sy in neighbours if ref < l[i+sx][j+sy]]) == len(neighbours):
                count += ref + 1
                locations.append((i,j))
    return count, locations


def part2(board, locations):
    sizes = []
    for i, j in locations:
        sizes.append(bfs((i, j), board))
    return math.prod(sorted(sizes, reverse=True)[0:3])


def bfs(p, board):
    n = len(board)
    m = len(board[0])
    q = [p]
    count = 1
    visited = set(p)
    while len(q) != 0:
        i,j = q.pop()
        neighbours = list([(sx, sy) for sx, sy in steps if 0 <= i+sx < n and 0 <= j+sy < m and board[i+sx][j+sy] != 9 and (i+sx, j+sy) not in visited])
        valid = [(i+sx, j+sy) for sx, sy in neighbours if board[i+sx][j+sy] > board[i][j]]
        count += len(valid)
        visited.update(valid)
        q.extend(valid)
    return count


input = []
for l in f:
    input.append(list([int(x) for x in l.strip()]))

lows = part1(input.copy())
print('part1: ', lows[0])
print('part2: ', part2(input.copy(), lows[1]))