list1 = input().split()
list2 = input().split()

list1u = [x for x in list1 if x not in list2]
list2u = [x for x in list2 if x not in list1]
print(list1u + list2u)
