import re
import copy

# f = open('data/day20-sample.txt', 'r')
f = open('data/day20-final.txt', 'r')


def print_b(img):
    minI = min([i for i, _ in img])-1
    maxI = max([i for i, _ in img])+1
    minJ = min([j for _, j in img])-1
    maxJ = max([j for _, j in img])+1
    for i in range(minI, maxI+1):
        for j in range(minJ, maxJ+1):
            print("#" if (i, j) in img and img[(i,j)] == '1' else ".", end="")
        print()
    print()


def part1(img, alg, rounds):
    steps = [(x,y) for x in range(-1, 2) for y in range(-1, 2)]
    toggle = alg[0] == '#' and alg[511] == '.'  # first and last make it alternate
    for t in range(rounds):
        default = str(t % 2) if toggle else "0"

        minI = min([i for i, _ in img])-1
        maxI = max([i for i, _ in img])+1
        minJ = min([j for _, j in img])-1
        maxJ = max([j for _, j in img])+1
        newI = {}
        for i in range(minI, maxI +1):
            for j in range(minJ, maxJ+1):
                window = "".join([img[(i+si, j+sj)] if (i+si, j+sj) in img else default for si, sj in steps])
                newI[(i, j)] = "1" if alg[int(window, 2)] == '#' else "0"
        img = newI  # swap

    return len([1 for k, v in img.items() if v == '1'])


alg = f.readline().strip()
f.readline()  # \n
matrix = [list(l.strip()) for l in f]
img = {(i,j): "1" for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == '#'}

print('part1: ', part1(copy.deepcopy(img), alg, 2))
print('part2: ', part1(copy.deepcopy(img), alg, 50))
