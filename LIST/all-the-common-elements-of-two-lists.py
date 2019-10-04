arr1 = input().split()
arr2 = input().split()
"""
arr3 = [x for x in arr1 if x in arr2]
print(set(arr3))
"""

if set(arr1) & set(arr2):
	print(set(arr1)&set(arr2))
else: print ("No common elements")
