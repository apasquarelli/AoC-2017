
# coding: utf-8

# In[10]:

import numpy as np
test


# In[20]:

input = open('input.txt')
digits = input.read().strip()
digits = list(map(int, digits))


# In[26]:

sum = 0
length = len(digits) -1 ;
for idx,num  in enumerate(digits):
    if idx == length:
        if num == digits[0]:
            sum +=num
    else:
        if num == digits[idx + 1]:
            sum +=num
print(sum)

