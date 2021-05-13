
# coding: utf-8

# ## Foundations of Artificial Intelligence and Machine Learning
# ### A Program by IIIT-H and TalentSprint

# The objective of this experiment is to perform Linear Regression using PyTorch

# In this experiment we will use synthetic data

# #### Total = 20 + 2(bonus) Marks

# #### Importing Required Packages

# In[1]:


import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import matplotlib.pyplot as plt
import random


# #### Intialising the data randomly around the line y = 2*x

# In[2]:



x_values = [i for i in range(11)]
x_train = np.array(x_values, dtype=np.float32)
x_train = x_train.reshape(-1, 1)

y_values = [2*i + 1 -2*random.random() for i in x_values]
y_train = np.array(y_values, dtype=np.float32)
y_train = y_train.reshape(-1, 1)


# In[2]:



# ### Plotting the data

# To get sense of the data. Let us plot the data

# In[3]:


plt.plot(x_train, y_train, 'r*')


# * Creating a model for linear regression

# In[4]:


class LinearRegressionModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)  
    
    def forward(self, x):
        out = self.linear(x)
        return out


# In[5]:


input_dim = 1
output_dim = 1

model = LinearRegressionModel(input_dim, output_dim)


# ### Exercise 1 ( 5 Marks):
# * Instantiate loss function in pytorch for linear regression model given above (5m)
# * Explore the different loss functions in the module torch.nn

criterion = nn.MSELoss()# Mean Squared Loss
l_rate = 0.01
optimiser = torch.optim.SGD(model.parameters(), lr = l_rate) #Stochastic Gradient Descent

# ### Exercise 2 (5 marks) :
# * choose a learning rate and instantiate optimizer (5m)
# * Explore different optimizers in the module torch.nn

# ### Exercise 3 (10 Marks) :
# * Train the model (5m)
# * plot the best fit line (5m)

# In[6]:


epochs = 100
for epoch in range(epochs):
    
    epochs += 1
    
    inputs = Variable(torch.from_numpy(x_train))
    labels = Variable(torch.from_numpy(y_train))
    
    optimiser.zero_grad()
    
    outputs = model.forward(inputs)
    loss = criterion(outputs, labels)
    loss.backward()
    optimiser.step()
    print('epoch {} , loss {} '.format(epoch, loss.data[0]))
    


predicted = model.forward(Variable(torch.from_numpy(x_train))).data.numpy()

plt.plot(x_train, y_train, 'go', label = 'from data', alpha = .5)
plt.plot(x_train, predicted, label = 'prediction', alpha = 0.5)
plt.legend()
plt.show()
print(model.state_dict())
    


# ### Exercise 4 (Bonus : 2 Marks) :
# * Deploy the model training on GPU using cuda (use colab)
