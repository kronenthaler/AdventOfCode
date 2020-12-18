
# f = open('data/day18-sample.txt', 'r')
f = open('data/day18-final.txt', 'r')

input = [l.strip() for l in f]

class T:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def eval(self):
        if self.left is None and self.right is None:
            return int(self.root)

        lv = self.left.eval()
        rv = self.right.eval()
        if self.root == '+':
            return lv + rv
        elif self.root == '*':
            return lv * rv

    def pp(self):
        if self.left is None and self.right is None:
            return '{}'.format(self.root)

        s = '('
        s += self.left.pp() if self.left is not None else ''
        s += ' {} '.format(self.root)
        s += self.right.pp() if self.right is not None else ''
        return s + ')'


def factor(tokens, prio):
    if tokens[0] == '(':
        tokens.pop(0) # (
        t = exp(tokens, prio)
        tokens.pop(0) # )
    else:
        t = T(tokens.pop(0))
    return t


def term(tokens, prio):
    t = factor(tokens, prio)
    while tokens.__len__() != 0 and tokens[0] in prio[1]:
        op = tokens.pop(0)
        r = factor(tokens, prio)
        t = T(op, t, r)
    return t


def exp(tokens, prio):
    t = term(tokens, prio)
    while tokens.__len__() != 0 and tokens[0] in prio[0]:
        op = tokens.pop(0)
        r = term(tokens, prio)
        t = T(op, t, r)
    return t


def part1(input, parse, prio):
    total = 0
    for line in input:
        t = parse(list([c for c in line.replace(' ', '')]), prio)
        print(t.pp(), t.eval())
        total += t.eval()
    return total


print('part1: ', part1(input, exp, [['+', '*'], []]))
print('part2: ', part1(input, exp, [['*'], ['+']]))
