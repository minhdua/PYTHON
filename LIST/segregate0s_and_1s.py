arr = [int(x) for x in input().split()]

#res = sorted(arr)

res = [x for x in arr if x % 2 == 0] + [x for x in arr if x%2 ==1]

print(res)
