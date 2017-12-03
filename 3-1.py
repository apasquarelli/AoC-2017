
# coding: utf-8

# In[3]:

import math


# In[122]:

input = 289326


# In[124]:

if int(math.sqrt(input)) %2 ==0:
       previousSquare = int(math.sqrt(input)) -1
else:
       previousSquare = int(math.sqrt(input))
        
position = input - previousSquare**2

if previousSquare %2 == 0:
    horizontalSteps = previousSquare//2
else:
    horizontalSteps = previousSquare//2 + 1

zeros = []
for i in range(4):
    if i == 0:
        zeros.append(previousSquare + (horizontalSteps +1))
    else:
        zeros.append(zeros[i-1] + (horizontalSteps) *2)
        
zeros[:] = [abs(x - position) for x in zeros]

verticalSteps = min(zeros)

print(horizontalSteps + verticalSteps)

