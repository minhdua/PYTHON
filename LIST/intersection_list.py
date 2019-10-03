list1 = input().split()
list2 = input().split()
intersections = list(filter(lambda x : x in list1,list2))

print(intersections)
