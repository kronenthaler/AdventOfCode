# data = '389125467' #  sample
data = '215694783' #  final

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert(self, node):
        temp = self.next
        self.next = node
        node.next = temp


def simulate(data, moves):
    lookup = {}
    prev = None
    current = None
    n = len(data)
    for d in data:
        lookup[d] = Node(d)
        if prev is not None:
            prev.next = lookup[d]
        else:
            current = lookup[d]
        prev = lookup[d]
    # close loop
    prev.next = current

    for i in range(moves):
        # print('move: ', i)

        # pick the next 3 elements
        a = current.next
        b = a.next
        c = b.next

        # remove them from the line
        current.next = c.next

        # calculate destination
        dest = -1
        next_dest = (current.value - 1) % n
        picked = [a.value, b.value, c.value]
        while dest < 0:
            if next_dest not in picked:
                dest = next_dest
                break
            next_dest = (next_dest - 1) % n

        lookup[dest].insert(a)
        a.insert(b)
        b.insert(c)

        current = current.next

    return lookup[0]


def part1(data, moves):
    head = simulate(data, moves).next
    result = ''
    while head.value != 0:
        result += str(head.value + 1)
        head = head.next
    return result


def part2(data, moves):
    head = simulate(data, moves)
    return (head.next.value + 1) * (head.next.next.value + 1)


print('part1: ', part1([int(c)-1 for c in data], 100))
print('part2: ', part2([int(c)-1 for c in data] + [x for x in range(9, 1_000_000)], 10_000_000))