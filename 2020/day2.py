import re

f = open('day2-final.txt', 'r')
total = 0
positionalTotal = 0
while True:
    content = f.readline()
    if content is None:
        break

    tokens = re.match(r'([0-9]+)-([0-9]+) (.): (.*)$', content)
    if tokens is None or len(tokens.groups()) == 0:
        break

    contains = "({0})".format(tokens.group(3))
    count = len([m.start() for m in re.finditer(contains, tokens.group(4))])

    if int(tokens.group(1)) <= count <= int(tokens.group(2)):
        total += 1

    if (tokens.group(4)[int(tokens.group(1))-1] == tokens.group(3) and tokens.group(4)[int(tokens.group(2))-1] != tokens.group(3)) or \
       (tokens.group(4)[int(tokens.group(1))-1] != tokens.group(3) and tokens.group(4)[int(tokens.group(2))-1] == tokens.group(3)):
        positionalTotal += 1

print("first: {}".format(total))
print("second: {}".format(positionalTotal))