import re

# f = open('data/day12-sample.txt', 'r')
f = open('data/day12-final.txt', 'r')

steps = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def part1(board, start, end):
    queue = [(start, 0)]
    visited = set([start])
    n = len(board)
    m = len(board[0])
    while len(queue) != 0:
        current, d = queue.pop(0)
        i, j = current
        if current == end:
            return d

        for sx, sy in steps:
            nx, ny = i + sx, j + sy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and ord(board[nx][ny]) - ord(board[i][j]) <= 1:
                queue.append(((nx, ny), d + 1))
                visited.add((nx, ny))
    return n * m  # no solution


def part2(board, end):
    return min([part1(board, (i, j), end)
                for i in range(0, len(board))
                for j in range(0, len(board[0]))
                if board[i][j] == 'a'])


board = [list(l.strip()) for l in f]
start = (0, 0)
end = (0, 0)
for i in range(0, len(board)):
    for j in range(0, len(board[0])):
        if board[i][j] == 'S':
            start = i, j
            board[i][j] = 'a'
        if board[i][j] == 'E':
            end = i, j
            board[i][j] = 'z'

print("part1: ", part1(board, start, end))
print("part2: ", part2(board, end))
