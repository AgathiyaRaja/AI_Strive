#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Import the needed libraries
import numpy as np


# **13. Create a 10x10 array with random values and find the minimum and maximum values**

# In[8]:


arr = np.random.randint(50,size=(10,10))
arr


# In[10]:


print(np.min(arr))
print(np.max(arr))


# **15. Create a 2d array with 1 on the border and 0 inside**

# In[13]:


arr = np.ones((5,5))
arr[1:-1,1:-1] = 0
arr


# In[ ]:




