import re

# f = open('data/day05-sample.txt', 'r')
f = open('data/day05-final.txt', 'r')


def translate(src_range, offset, dest_range):
    return range(dest_range.start+offset, dest_range.start+offset+len(src_range))


def part2(seeds, transitions):
    q = [('seed', seed) for seed in seeds]
    solutions = []
    while len(q) > 0:
        state, r = q.pop(0)

        if state == 'location':
            solutions.append(r.start)
            continue

        src, dest, ranges = [(s, d, r) for s, d, r in transitions if s == state][0]

        for src_range, dest_range in ranges:
            if r.start in src_range and r.stop in src_range:
                q.append((dest, translate(r, r.start - src_range.start, dest_range)))
                r = range(0, 0)
                break
            elif r.start in src_range and r.stop not in src_range:
                q.append((dest, translate(range(r.start, src_range.stop), r.start - src_range.start, dest_range)))
                r = range(src_range.stop, r.stop)
            elif r.start not in src_range and r.stop in src_range:
                q.append((dest, translate(range(src_range.start, r.stop), 0, dest_range)))
                r = range(r.start, src_range.start)

        if len(r) != 0:
            q.append((dest, r))

    return min(solutions)


lines = [l.strip() for l in f]
seeds = [int(x) for x in re.findall(r'(\d+)', lines[0])]
transitions = []
i = 1
while i < len(lines):
    l = lines[i]
    i += 1

    if len(l) == 0: continue

    src, dest = re.match(r'(.*)-to-(.*) map:', l).groups()
    
    ranges = []
    while i < len(lines) and len(lines[i]) != 0:
        l = lines[i]
        dest_start, src_start, length = tuple([int(x) for x in re.findall(r'(\d+)', l)])
        ranges.append((range(src_start, src_start+length), range(dest_start, dest_start+length)))
        i += 1
    transitions.append((src, dest, ranges))


print("part1: ", part2([range(seeds[i], seeds[i]+1) for i in range(0, len(seeds))], transitions))
print("part2: ", part2([range(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)], transitions))
