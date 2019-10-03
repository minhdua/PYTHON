list = input().split()
lowval,highval = input().split()

list = [int(x) for x in list]
lowval, highval = int(lowval), int(highval)

list1 = [x for x in list if x <lowval]
list2 = [x for x in list if lowval <= x <= highval]
list3 = [x for x in list if x > highval]

list = list1 + list2 + list3

print(list)
