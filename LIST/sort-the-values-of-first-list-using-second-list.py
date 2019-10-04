list1 = input().split()
list2 = [int(x) for x in input().split()]
"""
for i in range(len(list2)-1):
	for j in range(i+1,len(list2)):
		if list2[i]>list2[j]:
			list2[i],list2[j] = list2[j],list2[i]
			list1[i],list1[j] = list1[j],list1[i]
print(list1)
"""
listzip = zip(list2,list1)

res = [x for _,x in sorted(listzip)]

print(res)
