# Find prime number func.
pn=[2]

for i in range(3,201):
	#pn_l = len(pn)
	#for x in range(pn_l):
	c=0
	l=len(pn)
	for x in pn:
		c=c+1
		if i % x == 0:
			break
		else:
			if c == l:
				pn.append(i)
				

print pn;
print len(pn);
