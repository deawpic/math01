# Find prime number func.
def g(x):
	for i in range(2,x):
		if x % i == 0:
			break
		else:
			if i+1 == x:
				return x

# prime number between 9-200.
ans = filter(g,range(9,201))


temp = [1]

len_ans = len(ans)

# Find  multiplication of two prime numbers that not exceed 200.
for i in range(0,len_ans):
	z = ans[i]*ans[i]
	if  z < 201:
		temp.append(z)
		for j in range(i,len_ans):
			y = ans[i]*ans[j+1]
			if y < 201:
				temp.append(y)
			else: break
	else: break

###

print(temp)

ans = ans + temp
ans.sort()
	
print(ans)
print(len_ans)