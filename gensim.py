#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip show gensim


# In[2]:


from gensim.summarization import summarize


# In[3]:


from gensim.summarization import keywords


# In[6]:


text1 = "Hello, people from the future! Welcome to Normalized Nerd! I love to create educational videos on Machine Learning and Creative Coding. Machine learning and Data Science have changed our world dramatically and will continue to do so. But how they exactly work?...Find out with me. If you like my videos please subscribe to my channel."


# In[9]:


print(summarize(text1, ratio=0.5))


# In[8]:


print(summarize(text1, split=True, ratio=0.5))


# In[10]:


print(keywords(text1, words=5))


# In[ ]:




