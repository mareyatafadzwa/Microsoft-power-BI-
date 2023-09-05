#!/usr/bin/env python
# coding: utf-8

# # loading data

# In[2]:


import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# In[5]:


df = pd.read_excel ('C:/Users/TafadzwaMareya/OneDrive - Adviceworx/Desktop/data/car_financing.xlsx')


# In[34]:


df[:].head()


# In[9]:


df.tail()


# In[16]:


df[['Month']].head()


# In[20]:


df[['Month', 'Repayment']][0:10]


# In[47]:


df['car_type'].value_counts()


# In[49]:


car_filter = df['car_type']=='Toyota Sienna'


# In[51]:


df.loc[car_filter, :]


# In[53]:


df = df.rename(columns={'Starting Balance': 'Starting_Balance'})


# In[54]:


df.head()


# In[56]:


df = df.drop(columns=['term'])


# In[57]:


df


# In[59]:


del df['Month']


# In[60]:


df


# In[61]:


df['Repayment'].sum()


# In[66]:


df.sum()


# In[67]:


df.info()


# In[70]:


df['Interest Paid'].isna().head()


# In[76]:


interest_missing = df['Interest Paid'].isna()


# In[83]:


df.loc[interest_missing,:]


# In[85]:


df.loc[-interest_missing,:].sum()


# In[91]:


df['Interest Paid'][0:40].fillna(0)


# In[92]:


df.to_excel(excel_writer = 'C:/Users/TafadzwaMareya/OneDrive - Adviceworx/Desktop/data/car_financing_Output.xlsx', index =  False)


# In[ ]:




