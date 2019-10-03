arr = [int(x) for x in input().split()]
n = int(input())
"""
# cach 1
list1 = [x for x in arr if x > n]

if len(list1)== len(arr) : print("YES")
else : print("NO")

# cach 2
minx = min(arr)

if minx <= n : print("NO")
else: print("YES")
"""
#cach 3
check = all(x > n for x in arr)
if check : print("YES")
else: print("NO")
