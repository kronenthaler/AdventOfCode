import re
from copy import deepcopy

# f = open('data/day11-sample.txt', 'r')
f = open('data/day11-final.txt', 'r')

class Monkey:
    def __init__(self, index, items, op, test, dst_true, dst_false):
        self.index = index
        self.items = items.copy()
        self.seen_items = 0
        self.div_test = test
        self.operation = op.replace('old', '{old}')
        self.dst_true = dst_true
        self.dst_false = dst_false

    def check(self, old):
        return eval(self.operation.format(old=old))

    def __repr__(self):
        return f'[{self.index}/{self.seen_items}]: {self.items} / new = ({self.operation} / {self.div_test}) ? {self.dst_true} : {self.dst_false}'


def part1(monkeys, rounds, relief):
    for i in range(rounds):
        for m in monkeys:
            if len(m.items) == 0:
                continue

            for item in m.items.copy():
                m.items.pop(0)
                m.seen_items += 1
                new = relief(m.check(item))
                monkeys[m.dst_true if new % m.div_test == 0 else m.dst_false].items.append(new)

    monkeys.sort(key=lambda x: x.seen_items, reverse=True)
    return monkeys[0].seen_items * monkeys[1].seen_items


monkeys_part1 = []
monkeys_part2 = []
while True:
    l = f.readline().strip()
    if not l:
        break

    index = int(re.findall(r'Monkey (.*):', l)[0].strip()); l = f.readline().strip()
    items = list([int(x.strip()) for x in l.split(':')[1].split(',')]); l = f.readline().strip()
    op = l.split('=')[1].strip(); l = f.readline().strip()
    test = int(re.findall(r'Test: divisible by (.*)', l)[0].strip()); l = f.readline().strip()
    dst_true = int(re.findall(r'If true: throw to monkey (.*)', l)[0].strip()); l = f.readline().strip()
    dst_false = int(re.findall(r'If false: throw to monkey (.*)', l)[0].strip()); l = f.readline().strip()

    monkeys_part1.append(Monkey(index, items, op, test, dst_true, dst_false))
    monkeys_part2.append(Monkey(index, items, op, test, dst_true, dst_false))

mod_all = 1
for monkey in monkeys_part2:
    mod_all *= monkey.div_test

print("part1: ", part1(monkeys_part1, 20, lambda x: x // 3))
print("part2: ", part1(monkeys_part2, 10000, lambda x: x % mod_all))



