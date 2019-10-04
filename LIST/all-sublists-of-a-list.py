arr = input().split()
print('[[]',end=' ')
for i in range(len(arr)):
	for j in range(i+1,len(arr)+1):
		print(arr[i:j],end=' ')
print(']')
