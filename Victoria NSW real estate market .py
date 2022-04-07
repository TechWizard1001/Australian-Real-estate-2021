#!/usr/bin/env python
# coding: utf-8

# Let's dig deeper in the Australian real estate market where we have a dataset of sales consisting of properties from major cities in Australia. 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df_estate = pd.read_csv("C:/Users/Ronfo/Desktop/realestate.csv")


# In[3]:


df_estate[30:]


# let's create a subset daraframe that consist of date_sold, price, city_name,state,bedrooms,property_type

# In[4]:


new_estate= df_estate[['date_sold','price','city_name','state','bedrooms','property_type']]
new_estate


# Let's visualize the prices for victoria
# 

# In[5]:


vic_estate= new_estate[new_estate['state'] == 'VIC']
vic_estate


# In[6]:


vic_estate_low = vic_estate[vic_estate['price'] < 500000]
vic_estate_low


# In[7]:


fig = plt.figure(figsize=(10,10))
plt.scatter(vic_estate_low.property_type, vic_estate_low.price)
plt.xlabel('property type')
plt.ylabel('price')
plt.title("Houses sold in Victoria under half a million $")
plt.show()


# As we can see that in 2021 Victoria sold most number of units under 500 k and price ranged from less tha 100k to 500k, and only one house was sold under 100k and average house price started from 300k and townhouse price were above 300k.

# In[8]:


vic_estate_high = vic_estate[vic_estate['price'] > 500000]
vic_estate_high
                             


# In[9]:


fig = plt.figure(figsize=(20,100))
plt.scatter(vic_estate_high.property_type, vic_estate_high.price)
plt.xlabel('property type')
plt.ylabel('price')
plt.title("Houses sold in Victoria more than half a million")
plt.show()


# Houses were most sold when price went above 500k after that unit and townhouse. 

# In[10]:


vic_estate_low.describe()


# Average property sold in victoria was 411k during 2021
# 
# 

# In[11]:


nsw_estate= new_estate[new_estate['state'] == 'NSW']
nsw_estate


# In[12]:


nsw_estate_low = nsw_estate[nsw_estate['price'] < 500000]
nsw_estate_low


# In[13]:


fig = plt.figure(figsize=(10,10))
plt.scatter(nsw_estate_low.property_type, nsw_estate_low.price)
plt.xlabel('property type')
plt.ylabel('price')
plt.title("Houses sold in NSW under half a million $")
plt.show()


# Most property in NSW under 500k comprised of units followed by house and townhouse where one house under 100k was sold and average sale was 415k

# In[14]:


nsw_estate_low.describe()


# In[15]:


nsw_estate_high = nsw_estate[nsw_estate['price'] > 500000]
nsw_estate_high
                     


# In[16]:


fig = plt.figure(figsize=(20,50))
plt.scatter(nsw_estate_high.property_type, nsw_estate_high.price)
plt.xlabel('property type')
plt.ylabel('price')
plt.title("Houses sold in NSW more than half a million")
plt.show()


# NSW sales for more than 500k went to the houses followed by unit and townhouse
# 
# It can be identified that when people are spending over 500k both in NSW and VIC they prefer to buy a house but sales are under 500k most units are sold with townhouses ranged in middle
# 
# Surprisingly property bought under 500k both in Vic and NSW have average price of 415k irrespective of the hype in terms of cost of living in NSW

# In[ ]:





# In[ ]:




