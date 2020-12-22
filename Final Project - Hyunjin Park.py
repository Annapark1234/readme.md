#!/usr/bin/env python
# coding: utf-8

# In[283]:


# Topic: Visualize unemployment rate(%) differences between Oct. 2019 and Oct. 2020 in the United States.
# Then, compare each state's status with an average rate to check how many states have low and high rate since Covid-19 started.


# In[44]:


# Convert html file to csv file by using BeautifulSoup and Pandas.


# In[7]:


import pandas as pd


# In[8]:


import os


# In[9]:


import sys


# In[10]:


from bs4 import BeautifulSoup


# In[11]:


path = 'unemployment rate.html'


# In[12]:


data = []


# In[48]:


# Getting the header from HTML file


# In[13]:


list_header = [] 
soup = BeautifulSoup(open(path),'html.parser') 
header = soup.find_all("table")[0].find("tr") 


# In[14]:


for items in header: 
    try: 
        list_header.append(items.get_text()) 
    except: 
        continue


# In[49]:


# Getting the data


# In[15]:


HTML_data = soup.find_all("table")[0].find_all("tr")[1:]


# In[16]:


for element in HTML_data: 
    sub_data = [] 
    for sub_element in element: 
        try: 
            sub_data.append(sub_element.get_text()) 
        except: 
            continue
    data.append(sub_data)


# In[50]:


# Storing data into Pandas


# In[17]:


dataFrame = pd.DataFrame(data = data, columns = list_header)


# In[51]:


# Converting Pandas DataFrame into csv file


# In[20]:


dataFrame.to_csv('unemploymentrate.csv.') 


# In[87]:


import pandas as pd

df = pd.read_csv(r"/Users/annahyunjin/Desktop/final/unemploymentrate.csv",index_col=0)


# In[109]:


df


# In[114]:


# Removing unnecessary rows


# In[110]:


df.drop(200,0,inplace=True)

df


# In[111]:


df.drop(214,0,inplace=True)
df


# In[115]:


# Remove '/n' in 'Month' column


# In[113]:


df['Month'].replace(r'\s+|\\n', ' ', regex=True, inplace=True) 
df


# In[165]:


# Convert data types into numeric


# In[214]:


df.apply(pd.to_numeric, errors='ignore')


# In[217]:


# Making the bar graph by using matplotlib


# In[221]:


import matplotlib.pyplot as plt

df.plot(x ='Month', y='Unemployment Rate', kind = 'bar')
plt.show()


# In[224]:


# Bring the csv file with the unemployment rate by state for Nov 2020


# In[232]:


import pandas as pd

df2 = pd.read_csv(r"/Users/annahyunjin/Desktop/final/states.csv")


# In[233]:


df2


# In[235]:


# Drop unnecessary column


# In[234]:


df2.drop('Rank', axis=1, inplace=True)

df2


# In[258]:


import csv

f = open("/Users/annahyunjin/Desktop/final/states.csv")
comparison = list(csv.reader(f))

print(comparison)


# In[266]:


# Remove unnecessary row


# In[259]:


comparison = comparison[1:]

print(comparison)


# In[282]:


# Convert string to number for unemployment rate


# In[263]:


for cp in comparison:
    cp[1] = float(cp[1])

print(comparison)


# In[264]:


rate = []

for cp in comparison:
    rate.append(cp[1])
    
print(rate)


# In[237]:


# Getting the average of the Unemployment Rate


# In[265]:


rate_avg = sum(rate)/len(rate)

print("Average unemployment rate is: ", rate_avg)


# In[273]:


# Compare average rate and rate for each state to determine the number of states with low rate and high rate.


# In[281]:


low_rate = 0.0
high_rate = 0.0

for cp in comparison:
    rate = cp[1]
    if rate <= rate_avg:
        low_rate = low_rate + 1.0
        
    elif rate > rate_avg:
        high_rate = high_rate + 1.0
        

print("The number of states with LOW unemployment rate: ", low_rate)
print("The number of states with HIGH unemployment rate: ", high_rate)


# In[ ]:




