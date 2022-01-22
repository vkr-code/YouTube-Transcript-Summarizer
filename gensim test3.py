#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

text = requests.get('http://rare-technologies.com/the_matrix_synopsis.txt').text
print(text)


# In[3]:


# Gensim Imports
from gensim.summarization.summarizer import summarize


# In[4]:


print(summarize(text, ratio=0.01))


# In[9]:


from gensim.summarization import keywords


# In[10]:


print(keywords(text, ratio=0.01))


# In[ ]:




