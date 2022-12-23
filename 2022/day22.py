import re

# f = open('data/day22-sample.txt', 'r'); N = 4
f = open('data/day22-final.txt', 'r'); N = 50

incs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # r, d, l, u (0 1 2 3)
dir_s = ['>', 'v', '<', '^']
jumps = [None, [(2, 0), (4, 1), (6, 0), (9, 0)], [(7, 2), (4, 2), (1, 2), (9, 3)],
         None, [(2, 3), (7, 1), (6, 1), (1, 3)], None,
         [(7, 0), (9, 1), (1, 0), (4, 0)], [(2, 2), (9, 2), (6, 2), (4, 3)], None,
         [(7, 3), (2, 1), (1, 1), (6, 3)]
]

# lambda i, j, rel_i, rel_j, min_i, min_j, max_i, max_j
# 1-2: min(i) + rel_c(i), min(j)
# 1-3: min(i), min(j) + rel_c(j)
# 1-4: max(i) - rel_c(i), min(j)
# 1-6: min(i), min(j) + rel_c(j)

# 2-1: min(i) + rel_c(i), max(j)
# 2-5: max(i) - rel_c(j), max(j)
# 2-3: min(i) + rel_c(j), max(j)
# 2-6: max(i), rel_c(j)

# 3-2: max(i), min(j) + rel_c(i)
# 3-1: max(i), min(j) + rel_c(j)
# 3-5: min(i), min(j) + rel_c(j)
# 3-4: min(i), min(j) + rel_c(i)

# 4-1: max(i) - rel_c(i), min(j)
# 4-3: min(i) + rel_c(j), min(j)
# 4-5: min(i) + rel_c(i), min(j)
# 4-6: min(i), min(j) + rel_c(j)

# 5-2: max(i) - rel_c(j), max(j)
# 5-3: max(i), min(j) + rel_c(j)
# 5-4: min(i) + rel_c(i), max(j)
# 5-6: min(i) + rel_c(j), max(j)

# 6-1:
# 6-2:
# 6-4: max(i), min(j) + rel_c(j)
# 6-5: max(i), min(j) + rel_c(i)



def print_b(board, pos, dir):
    for i in range(len(board)):
        line = ''
        for j in range(len(board[i])):
            if (i,j) == pos:
                line += dir_s[dir]
            else:
                line += board[i][j]
        print(line)
    print()


def wrap1(i, j, dir):
    mi, mj = incs[dir]
    mod = len(board[i]) if dir % 2 == 0 else len(board)
    for w in range(mod):
        i = (i + mi) % mod if dir % 2 != 0 else i
        j = (j + mj) % mod if dir % 2 == 0 else j

        if board[i][j] == '#':
            return None, None

        if board[i][j] != ' ':
            return (i, j), dir


def wrap2(i, j, dir):
    face_i, face_j = i // N, j // N
    new_face, new_dir = jumps[face_i * 3 + face_j][dir]
    # calculate transpotion of coordinates for new pos
    new_pos = i,j
    if board[new_pos[0]][new_pos[1]] == '#':
        return None, None
    return new_pos, new_dir


def move(pos, dir, board, step, wrap):
    for t in range(step):
        i, j = pos
        mi, mj = incs[dir]
        if (0 > i+mi or i+mi >= len(board)) or (0 > j+mj or j+mj >= len(board[i])) or board[i+mi][j+mj] == ' ':  # wrap around
            mod = len(board[i]) if dir % 2 == 0 else len(board)
            x, y = i, j
            new_pos, new_dir = wrap(i, j, dir)
            dir = new_dir

            if not new_pos:
                return x, y
            pos = new_pos

        else:
            if board[i+mi][j+mj] == '#':
                return i, j
            pos = i+mi, j+mj
    return pos

def part1(board, moves, wrap):
    pos = (0, 0)
    dir = 0
    for x in range(len(board[0])):
        if board[0][x] == '.':
            pos = (0, x)
            break

    for step, r in moves:
        if r != '':
            dir = (dir + (1 if r == 'R' else -1)) % 4
            continue
        pos = move(pos, dir, board, int(step), wrap)

    return ((pos[0]+1)*1000) + ((pos[1]+1)*4) + dir

def part2(board, moves):
    pass

board = []
max_l = 0
while True:
    l = f.readline()[0:-1]
    if l == '':
        break
    board.append(l)
    max_l = max(max_l, len(l))

inst = f.readline().strip()
moves = re.findall(r'([0-9]+)|([RL])', inst)

for i in range(len(board)):
    l = board[i]
    if max_l != len(l):
        board[i] = l.ljust(max_l)
print(len(moves))
print("part1: ", part1(board, moves, wrap1))
print("part2: ", part2(board, moves))
