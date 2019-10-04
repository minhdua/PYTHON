from collections import Counter
arr = input().split()
list1 = []
for x in arr:
	list1.append(Counter(x))
for x in range(len(list1) -1 ):
	for y in range(x+1,len(list1)):
		if list1[x]==list1[y]:
			print(list[list1[y]])

