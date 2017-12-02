
# coding: utf-8

# In[53]:

import numpy as np


# In[54]:

input = open('input.txt')


# In[55]:

checksum = 0
for line in input:
    nums = [int(num) for num in line.split()]
    for firstnum in nums:
        for secondnum in nums:
            if firstnum != secondnum and firstnum % secondnum==0:
                checksum += firstnum/secondnum           
checksum

