#!/usr/bin/env python
# coding: utf-8

# In[1]:


from __future__ import division
from itertools import permutations, combinations
import copy as cp
import numpy as np


# In[2]:


import random
N = 8 
x = range(0, N )


master_list = []
for item in permutations(range(0, N)):
    y = item
    new_list = []
    for x_value, y_value in zip(x, y):
        new_list.append((x_value, y_value))
    master_list.append(new_list)


def IsDiagonal(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    gradient = (y2 - y1) / (x2 - x1)
    if gradient == -1 or gradient == 1:
        return(True)
    else:
        return(False)


solutions = []
for possible_solution in master_list:
    diagonal_clash_list = []
    for piece1, piece2 in combinations(possible_solution, 2):
        diagonal_clash_list.append(IsDiagonal(piece1, piece2))

    if True not in diagonal_clash_list:
        solutions.append(possible_solution)

def Convert(lst): 
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst),2)} 
    return res_dct 
          

tmp_list=[]

for row in range(len(solutions)):
    for column in range(len(solutions[row])):
         tmp_list.append(solutions[row][column][1])


sol_array= np.asarray(tmp_list)
solution=sol_array.reshape(92,8)

random=random.randint(0,91)
Position=solution[random]
Position


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




