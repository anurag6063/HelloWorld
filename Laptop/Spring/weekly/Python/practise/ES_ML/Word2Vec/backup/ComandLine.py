
# coding: utf-8

# In[8]:


import argparse


# In[2]:


parser = ArgumentParser()


# In[20]:


parser =argparse.ArgumentParser(description='This is a sample parser')

parser.add_argument("echo")


# In[21]:


args = parser.parse_args()


# In[22]:


print(args)

