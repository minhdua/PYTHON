listt = [int(x) for x in input().split()]

list1 = listt[::2]
list2 = listt[1::2]
list1 = sorted(list1)
list2 = sorted(list2,reverse = True)
listt = list1 + list2

print(listt)
