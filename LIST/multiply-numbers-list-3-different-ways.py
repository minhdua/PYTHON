#from functools import reduce
import numpy as np
list1 = [int(x) for x in input().split()]

#mul = reduce(lambda x,y:x*y,list1)
mul = np.prod(list1)
print(mul)
