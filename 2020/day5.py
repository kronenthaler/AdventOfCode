import re

#f = open('day4-sample.txt', 'r')
f = open('day4-final.txt', 'r')

def bin(seq):
    lo = 0
    hi = 127
    row = -1
    seat = -1
    mode = True
    mid = (hi + lo) // 2
    for c in seq:
        mid = (hi + lo) // 2
        if mode:
            if c == 'F':
                hi = mid
            elif c == 'B':
                lo = mid + 1
            else:
                row = mid
                lo = 0
                hi = 7
                mid = (hi + lo) // 2
                mode = False

                if c == 'L':
                    hi = mid
                else:
                    lo = mid + 1
        else:
            if c == 'L':
                hi = mid
            else:
                lo = mid + 1

    seat = mid
    return (row * 8) + seat


content = f.readlines()
value = 0
seats = []
for line in content:
    seats.append(bin(line))
print("part1: ", value)

seats.sort()
for x in range(98, 987):
    if x not in seats:
        print("part2", x)
        break



