# To compute a sequence of numbers not divisible by 2 or 3 or 5 or 7

# Method-1  Brute force
def f(x): return x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0

# set range 1 to 200
ans = filter(f,range(1,201))

# print
print('answer=',ans)
print('count=',len(ans))

######
