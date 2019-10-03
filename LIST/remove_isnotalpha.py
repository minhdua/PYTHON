import re

str1 = input()
"""
# Cach 1
patt = '[a-z,A-z]'
match = re.findall(patt,str1)
res = ''.join(match)
# cach 2
res = ''
for i in str1:
	if i.isalpha():
		res += i
"""
# cach 3
list = [i for i in str1 if i.isalpha()]
res = ''.join(list)
print(res)


