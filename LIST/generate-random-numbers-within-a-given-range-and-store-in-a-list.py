import random

num,start,end = input().split()
num,start,end = int(num),int(start),int(end)
list1 = []
for i in range(num):
	list1.append(random.randint(start,end))

print(list1)
