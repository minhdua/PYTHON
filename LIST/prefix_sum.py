arr = [int(x) for x in input().split()]
"""
res = arr
for i in range(1,len(res)):
	res[i] = res[i]+res[i-1]
print(res)
"""
from itertools import accumulate
res  = list(accumulate(arr))
print(res)	

