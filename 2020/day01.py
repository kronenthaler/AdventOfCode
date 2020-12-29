
f = open('data/day1-sample.txt', 'r')
# f = open('day1-final.txt', 'r')

content = f.readlines()
for i in range(0, content.__len__()):
    x = int(content[i])
    for j in range(i+1, content.__len__()):
        y = int(content[j])
        if x + y == 2020:
            print('part1: ', x * y)

        for k in range(j+1, content.__len__()):
            z = int(content[k])
            if x + y + z == 2020:
                print('part2: ', x* y * z)

