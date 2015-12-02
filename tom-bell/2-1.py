l = 0
with open("2-1.txt", 'r') as f:
	for line in f:
		d = [int(i) for i in line.split('x')]
		l += 2*d[0]*d[1] + 2*d[1]*d[2] + 2*d[2]*d[0]
		s = sorted(d)[:2]
		l += s[0]*s[1]
print(l)
