
# coding: utf-8

# In[2]:


from flask import Flask


# In[3]:


from flask_restful import Api, Resource, reqparse


# In[4]:


app = Flask(__name__)


# In[5]:


api = Api(app)


# In[6]:


users= [{
    "name": "anurag"
}]


# In[7]:


users


# In[18]:


class User(Resource):
    def get(self, name):
        print(name)


# In[19]:


api.add_resource(User, "/user/<string:name>")

