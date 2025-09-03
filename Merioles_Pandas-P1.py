#!/usr/bin/env python
# coding: utf-8

# ## Panda Data Analysis 

# #### Merioles, Irish Rianne T. 

# #### 2ECE-B

# In[2]:


import pandas as pd 


# In[3]:


cars = pd.read_csv('cars.csv')
cars


# In[8]:


print("First Five Rows:") 
cars.head() #First Five Rows


# In[9]:


print("Last Five Rows:")
cars.tail() #Last Five Rows


# In[ ]:




