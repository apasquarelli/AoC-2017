
# coding: utf-8

# In[2]:

import numpy as np


# In[26]:

input = open('input.txt')
digits = input.read().strip()
digits = list(map(int, digits))


# In[27]:

sum = 0
length = int((len(digits))/2)
for idx,num  in enumerate(digits[:length]):
    if num == digits[length + idx]:
            sum +=num
            
print(sum *2)


# In[ ]:



