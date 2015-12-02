from functools import reduce
l = 0
with open("2.txt", 'r') as f:
	for line in f:
		d = [int(i) for i in line.split('x')]
		l += sum([i*2 for i in sorted(d)[:2]]) + reduce(lambda x, y: x*y, d)
print(l)