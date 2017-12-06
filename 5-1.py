
# coding: utf-8

# In[2]:

input = open("input.txt")
values = []
for line in input.readlines():
    values.append(int(line))
     
position = 0
steps = 0

while position < len(values):
    values[position] += 1
    position = position + (values[position] -1)
    steps +=1

steps
    


# In[ ]:



