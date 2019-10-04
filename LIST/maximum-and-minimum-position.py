arr = [int(x) for x in input().split()]

print('The maximum is at position',arr.index(max(arr))+1)
print('The minimum is at position',arr.index(min(arr))+1)
