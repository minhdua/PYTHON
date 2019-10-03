list = input().split()
a,b = input().split()

list = [int(x) for x in list]
a,b = int(a),int(b)
"""
list = sorted(list)
x = list.index(a)
y = list.index(b) # wrong because it return first index

numbers = y - x + 1
"""
list = [x for x in list if a <= x <= b ]
print(list)
print(len(list))
