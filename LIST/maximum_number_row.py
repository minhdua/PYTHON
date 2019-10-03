arr2D = [[0,1,1,1],
	[0,0,1,1],
	[1,1,1,1],
	[0,0,0,0]]
"""
maximum = 0
for i in range(len(arr2D)):
	sum_max = sum(arr2D[i])
	if sum_max > maximum:
		index = i
		maximum = sum_max
"""
list = list(map(sum,arr2D))
maximum = max(list)
index = list.index(maximum)
print(index)

