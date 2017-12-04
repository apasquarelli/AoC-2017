
# coding: utf-8

# In[6]:

input = open("input.txt")

phrases = []
sortedPhrases = []
valid = 0
for line in input.readlines():
    phrases.append([''.join(sorted(x)) for x in line.split()])

    
for phrase in phrases:    
    if not len(phrase) > len(set(phrase)):
        valid +=1

print(valid)

