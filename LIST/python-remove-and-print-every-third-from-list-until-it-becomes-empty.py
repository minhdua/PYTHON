list1 = [int(x) for x in input().split()]

list2 = []
i = 2
while list1:
	list2.append(list1[i])
	del list1[i]
	if list1:
		i = (i+2 )% len(list1)

print (list2)
