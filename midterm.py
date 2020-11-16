#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd

df = pd.read_csv(r"/Users/annahyunjin/Desktop/project/alcohol.csv")


# In[45]:


df.drop([5,192], axis=0).head(5)
df.drop(['continent'],axis = 1).head(5)


# In[61]:


av_column = df.mean(axis=0)
print(av_column)


# In[83]:


av_row = df.mean(axis=1)
print (av_row)


# In[94]:


import csv

f = open('/Users/annahyunjin/Desktop/project/alcohol.csv')
alcohol = list(csv.reader(f))

print(alcohol[:5])


# In[95]:


alcohol = alcohol[1:]

print(alcohol[:5])


# In[96]:


for al in alcohol:
    al[2] = int(al[2])
    al[3] = int(al[3])

print(alcohol[:5])


# In[99]:


first_row = alcohol[1]
print(first_row)


# In[100]:


second_row = alcohol[2]
print(second_row)


# In[101]:


albwine = first_row[3]
algwine = second_row[3]

if albwine > algwine:
    print("Albania comsumes more wine than Algeria.")
else:
    print("Algeria consumes more wine than Albania.")


# In[ ]:




