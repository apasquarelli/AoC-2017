
# coding: utf-8

# In[10]:

input = open("input.txt")

phrases = []
valid = 0
for line in input.readlines():
    phrases.append(line.split())

for phrase in phrases:
    if not len(phrase) > len(set(phrase)):
        valid +=1

print(valid)

