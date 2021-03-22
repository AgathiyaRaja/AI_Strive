#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import the needed libraries
import numpy as np


# **34. How to get all the dates corresponding to the month of July 2016**

# In[3]:


print(np.arange('2016-07', '2016-08', dtype='datetime64[D]'))


# **42. Consider two random array A and B, check if they are equal**

# In[7]:


A = np.random.randint(2, 3, 4)
A


# In[8]:


B = np.random.randint(2, 3, 4)
B


# In[10]:


arr_eql = np.allclose(A, B)
arr_eql


# In[ ]:





# In[ ]:




