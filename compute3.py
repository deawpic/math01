a=[]
for x in range(1,201):
	if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
		a.append(x)

print a
print len(a)


