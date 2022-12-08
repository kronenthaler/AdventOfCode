import re

# f = open('data/day8-sample.txt', 'r')
f = open('data/day8-final.txt', 'r')

def check(board, value, iv, jv):
    visible = (True, True, True, True)
    for i in range(0, iv):
        if board[i][jv] >= value:
            visible = (False, visible[1], visible[2], visible[3])

    for i in range(iv+1, len(board)):
        if board[i][jv] >= value:
            visible = (visible[0], False, visible[2], visible[3])

    for j in range(0, jv):
        if board[iv][j] >= value:
            visible = (visible[0], visible[1], False, visible[3])

    for j in range(jv+1, len(board)):
        if board[iv][j] >= value:
            visible = (visible[0], visible[1], visible[2], False)

    return visible[0] or visible[1] or visible[2] or visible[3]

def view(board, value, iv, jv):
    view = [0, 0, 0, 0]

    for i in range(iv-1, -1, -1):  # top
        if board[i][jv] >= value:
            view[0] = iv - i - (1 if board[i][jv] == 10 else 0)
            break

    for i in range(iv + 1, len(board)):  # bottom
        if board[i][jv] >= value:
            view[1] = i - iv - (1 if board[i][jv] == 10 else 0)
            break

    for j in range(jv - 1, -1, -1):  # left
        if board[iv][j] >= value:
            view[2] = jv - j - (1 if board[iv][j] == 10 else 0)
            break

    for j in range(jv + 1, len(board)):  # right
        if board[iv][j] >= value:
            view[3] = j - jv - (1 if board[iv][j] == 10 else 0)
            break

    result = view[0] * view[1] * view[2] * view[3]
    return result

def part1(board):
    count = 0
    for i in range(1, len(board)-1):
        for j in range(1, len(board)-1):
            count += 1 if check(board, board[i][j], i, j) else 0

    return count + 4 + 4*(len(board)-2)

def part2(board):
    # expand the board to ease the calculation
    n = len(board)
    board.insert(0, [10]*n)
    board.append([10]*n)
    for l in board:
        l.insert(0, 10)
        l.append(10)
    # [print(l) for l in board]

    count = 0
    for i in range(2, len(board) - 2):
        for j in range(2, len(board) - 2):
            count = max(count, view(board, board[i][j], i, j))

    return count

board = [list(map(int, list(l.strip()))) for l in f]

print("part1: ", part1(board.copy()))
print("part2: ", part2(board.copy()))