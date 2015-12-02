i = open("1.txt").read()
(p, k) = 0, 1
for c in i:
	p += 1 if c == '(' else -1
	if p == -1:
		break
	k += 1
print(k)