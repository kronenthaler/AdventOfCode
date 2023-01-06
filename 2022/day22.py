import re

# f = open('data/day22-sample.txt', 'r'); N = 4
f = open('data/day22-final.txt', 'r'); N = 50

R=0;D=1;L=2;U=3
incs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # r, d, l, u (0 1 2 3)
dir_s = ['>', 'v', '<', '^']
jumps = [None, [(2, R), (4, D), (6, R), (9, R)], [(7, L), (4, L), (1, L), (9, U)],
         None, [(2, U), (7, D), (6, D), (1, U)], None,
         [(7, R), (9, D), (1, R), (4, R)], [(2, L), (9, L), (6, L), (4, U)], None,
         [(7, U), (2, D), (1, D), (6, U)]
]

wraps = [
    None,
    {
        2: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (min_i + rel_i, min_j), # ok
        4: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (min_i, min_j + rel_j), # ok
        6: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (max_i - rel_i, min_j), # ok
        9: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (min_i + rel_j, min_j), # ok
    },  # 1-X
    {
        1: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (min_i + rel_i, max_j), # ok
        7: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (max_i - rel_i, max_j), # ok
        4: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (min_i + rel_j, max_j), # ok
        9: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (max_i, min_j + rel_j), # ok
    },  # 2-X
    None,
    {
        2: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (max_i, min_j + rel_i), # ok
        1: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (max_i, min_j + rel_j), # ok
        7: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (min_i, min_j + rel_j), # ok
        6: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (min_i, min_j + rel_i), # ok
    },  # 3-X
    None,
    {
        1: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (max_i - rel_i, min_j), # ok
        4: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (min_i + rel_j, min_j), # ok
        7: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (min_i + rel_i, min_j), # ok
        9: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (min_i, min_j + rel_j), # ok
    },  # 4-X
    {
        2: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (max_i - rel_i, max_j), # ok
        4: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (max_i, min_j + rel_j), # ok
        6: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (min_i + rel_i, max_j), # ok
        9: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (min_i + rel_j, max_j), # ok
    },  # 5-X
    None,
    {
        1: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (min_i, min_j + rel_i), # ok
        2: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (min_i, min_j + rel_j), # ok
        6: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (max_i, min_j + rel_j), # ok
        7: lambda rel_i, rel_j, min_i, min_j, max_i, max_j: (max_i, min_j + rel_i), # ok
    },  # 6-X
]

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
    current_face_index = face_i * 3 + face_j
    new_face, new_dir = jumps[current_face_index][dir]
    new_face_i, new_face_j = new_face // 3, new_face % 3
    mi, mj = incs[new_dir]
    min_i, min_j = new_face_i * N, new_face_j * N
    max_i, max_j = min_i + N-1, min_j + N-1
    rel_i, rel_j = i - (face_i * N), j - (face_j * N)
    new_pos = wraps[current_face_index][new_face](rel_i, rel_j, min_i, min_j, max_i, max_j)

    if board[new_pos[0]][new_pos[1]] == '#':
        return None, None
    return new_pos, new_dir


def move(pos, dir, board, step, wrap):
    for t in range(step):
        i, j = pos
        mi, mj = incs[dir]
        if (0 > i+mi or i+mi >= len(board)) or (0 > j+mj or j+mj >= len(board[i])) or board[i+mi][j+mj] == ' ':  # wrap around
            new_pos, new_dir = wrap(i, j, dir)

            if not new_pos:
                return i, j

            dir = new_dir
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

print("part1: ", part1(board, moves, wrap1))
print("part2: ", part1(board, moves, wrap2))
