import copy

# f = open('data/day04-sample.txt', 'r')
f = open('data/day04-final.txt', 'r')

seq = [int(x) for x in f.readline().split(',')]
boards = []
while f.readline():
    board = ([], [[], [], [], [], []])  # array<rows>, array<cols>
    for i in range(0, 5):
        board[0].append([int(i) for i in f.readline().split()])
        for j in range(0, 5):
            x = board[0][-1][j]
            board[1][j].append(x)
    boards.append(board)


def print_b(board):
    for r in board[0]:
        print(r)
    print("")


def part1(seq, boards):
    for s in seq:
        for r, c in boards:
            for i in range(0, 5):
                if s in r[i]:
                    r[i].remove(s)
                if s in c[i]:
                    c[i].remove(s)

                if len(r[i]) == 0:
                    return sum([x for rs in r for x in rs]) * s
                if len(c[i]) == 0:
                    return sum([x for rs in c for x in rs]) * s


def part2(seq, boards):
    for s in seq:
        to_remove = set()
        for j in range(0, len(boards)):
            r, c = boards[j]
            for i in range(0, 5):
                if s in r[i]:
                    r[i].remove(s)
                if s in c[i]:
                    c[i].remove(s)

                if len(r[i]) == 0 and len(boards) == 1:
                    return sum([x for rs in r for x in rs]) * s
                if len(c[i]) == 0 and len(boards) == 1:
                    return sum([x for rs in c for x in rs]) * s
                if len(r[i]) == 0 or len(c[i]) == 0:
                    to_remove.add(j)

        for x in sorted(list(to_remove), reverse=True):
            del boards[x]

print("part1: {}".format(part1(seq, copy.deepcopy(boards))))
print("part2: {}".format(part2(seq, copy.deepcopy(boards))))