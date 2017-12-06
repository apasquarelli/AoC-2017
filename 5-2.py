
# coding: utf-8

# In[1]:

input = open("input.txt")
values = []
for line in input.readlines():
    values.append(int(line))
     
position = steps = 0
while position < len(values) and position>=0:
    if values[position] >= 3:
        values[position] -= 1
        position = position + (values[position] + 1)
    else: 
        values[position] += 1
        position = position + (values[position] - 1)
    steps +=1

steps
    

