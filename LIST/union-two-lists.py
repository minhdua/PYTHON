import numpy as np
list1 = [int(x) for x in input().split()]
list2 = [int(x) for x in input().split()]

list3 = list1 + list2

list3 = np.unique(list3)

print(list3)
