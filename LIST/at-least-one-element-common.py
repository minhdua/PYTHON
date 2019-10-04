arr1 =[int(x) for x in input().split()]
arr2 =[int(x) for x in input().split()]

check = any(x in arr1 for x in arr2)

if check : print("YES")
else : print("NO")
