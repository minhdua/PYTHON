n,m = input().split()
n,m = int(n),int(m)
#l = [x*n for x in range(1,m+1)]
l = range(n,m*n+1,n)
print(*l)
