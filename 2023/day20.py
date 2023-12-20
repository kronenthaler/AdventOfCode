import re

# f = open('data/day20-sample.txt', 'r')
f = open('data/day20-final.txt', 'r')

class Node:
    def __init__(self, name, inputs, outputs):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs

    def activate(self, pulse, origin):
        pass


class Broadcaster(Node):
    def __init__(self, name, inputs, outputs):
        super().__init__(name, inputs, outputs)

    def activate(self, pulse, origin):  # return a list of activations
        return list([(o, pulse, self.name) for o in self.outputs])


class FlipFlop(Node):
    def __init__(self, name, inputs, outputs):
        super().__init__(name, inputs, outputs)
        self.state = 0

    def activate(self, pulse, origin):
        if pulse == 1: return []
        self.state = 1 - self.state
        return list([(o, self.state, self.name) for o in self.outputs])


class Conjunction(Node):
    def __init__(self, name, inputs, outputs):
        super().__init__(name, inputs, outputs)
        self.last_values = {k: 0 for k in inputs}

    def activate(self, pulse, origin):
        self.last_values[origin] = pulse
        is_all_high = sum(self.last_values.values()) == len(self.last_values)
        return list([(o, 0 if is_all_high else 1, self.name) for o in self.outputs])


def part1(nodes):
    pulses = [0, 0]
    for t in range(1000):
        q = [('broadcaster', 0, 'button')]
        while len(q) > 0:
            node, pulse, origin = q.pop(0)
            pulses[pulse] += 1  # record pulses

            if node not in nodes:
                continue

            node = nodes[node]
            results = node.activate(pulse, origin)
            q.extend(results)
    return pulses[0] * pulses[1]


def part2(nodes):
    # not simulation (2000000000 too low!) -> need to create the path to rx node

    return -1


lines = [re.match(r'(.*) -> (.*)', l.strip()).groups() for l in f]
lines = [(name if name[0] not in ['%','&'] else name[1:],
          name[0] if name[0] in ['%', '&'] else '',
          list(l.strip() for l in dests.split(','))) for name, dests in lines]
outputs = {k: v for k, _, v in lines}
inputs = {'broadcaster': ['button']}
for k, _, v in lines:
    for t in v:
        if t not in inputs:
            inputs[t] = []
        inputs[t].append(k)


def create_nodes(lines):
    nodes = {}
    # create Nodes out of inputs, outputs, nodes
    for name, type in ({k: t for k, t, _ in lines}).items():
        if type == '':
            nodes[name] = Broadcaster(name, inputs[name], outputs[name])
        if type == '%':
            nodes[name] = FlipFlop(name, inputs[name], outputs[name])
        if type == '&':
            nodes[name] = Conjunction(name, inputs[name], outputs[name])
    return nodes


print("part1: ", part1(create_nodes(lines)))
print("part2: ", part2(create_nodes(lines)))
