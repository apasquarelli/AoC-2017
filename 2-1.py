
# coding: utf-8

# In[1]:

import numpy as np


# In[5]:

input = open('input.txt')


# In[6]:

checksum = 0
for line in input:
    nums = [int(num) for num in line.split()]
    checksum += max(nums)-min(nums)
checksum


# In[ ]:



