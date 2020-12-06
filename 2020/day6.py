f = open('day4-final.txt','r')
#f = open('day4-sample.txt','r')

all = []
exc = []
counts = []
union = set()
intersection = set()
fos = True
for line in f:
#	print(line.strip())
	if line == '\n':
		all.append(union)
		exc.append(intersection)
		union = set()
		intersection = set()
		fos = True
		continue

	union.update(line.strip())
	if fos:
		fos = False
		intersection.update(line.strip())
	else:
		intersection.intersection_update(line.strip())
		

all.append(union)
exc.append(intersection)

print('part1', sum([x.__len__() for x in all]))
print('part2', sum([x.__len__() for x in exc]))

