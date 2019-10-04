import pprint
def Convert(a,b,c):
	a = a.strip()
	b = b.strip()
	c = c.strip()
	a,b,c = int(a),int(b),int(c)
	return a,b,c

a,b,c = input().split('x')

a,b,c = Convert(a,b,c)

l = [[['#' for col in range(a)] for col in range(b)] for col in range(c)]
pprint.pprint(l)
