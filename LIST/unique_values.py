arr = [int(x) for x in input().split()]

import numpy as np
uni_arr = np.array(arr)
print(np.unique(uni_arr)) 

"""
uni_arr = set(arr)

print(uni_arr)

"""
