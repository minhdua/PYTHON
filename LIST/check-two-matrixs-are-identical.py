n = int(input())
matrix1 = [[]]

for i in range(n):
	arr1 = [int(x) for x in input().split()]
	matrix1.append(arr1)
matrix2 = [[]]
for i in range(n):
	arr2 = [int(x) for x in input().split()]
	matrix2.append(arr2)

if matrix1 == matrix2 : print('YES')
else: print('NO')
