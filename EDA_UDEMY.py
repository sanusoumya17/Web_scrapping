#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np     #To perform numerical observations
import pandas as pd    #To work with dataframes

#For Data Visualisation
import matplotlib.pyplot as plt
import seaborn as sns

# To perform operations with date & time
import datetime as dt


# In[2]:


#Importing the data
udemy=pd.read_csv('udemy.csv')


# # Exploratory Data Analysis

# In[3]:


udemy.head()


# In[24]:


udemy.tail()


# In[4]:


udemy.info()


# There are 9 features and 10000 obervations.There are 4 quantitative features and 5 categorical feature.There are no missing values.
# 
# Since, Discount_Price ideally should be a numeric value, we need to change its datatype.

# In[6]:


print(udemy.columns)


# In[7]:


udemy = udemy.rename(columns = {' Url':'Url',' Created_on':'Created_on', ' Published':'Published', ' Subscribers':'Subscribers',' Reviews':'Reviews', ' Rating':'Rating', ' Price':'Price', ' Discounted_Price':'Discounted_Price'})


# In[8]:


discount_list=list(udemy.Discounted_Price.unique())
print(discount_list)


# We can see that the values are in str datatype, and due to presence of None we can't change its datatype directly.

# In[9]:


udemy['Discounted_Price'].replace('None', '0', inplace=True) #Replacing None with 0


# In[16]:


# Changing datatype from object to int64
udemy['Discounted_Price'] = np.dtype('int64').type(udemy['Discounted_Price'])


# In[18]:


udemy.info()


# In[19]:


udemy.describe()


# In[20]:


miss_val_per=udemy.isnull().mean()*100
print(miss_val_per)


# In[21]:


row, columns = udemy.shape
print("Data Row:", row)
print("Data Columns:", columns)


# In[22]:


udemy.describe(include='O')


# In[23]:


sns.heatmap(udemy.corr(),annot=True,square=True)


# We can interpret that Reviews and Subscribers are positively correlated.

# In[68]:


sns.kdeplot(data=udemy['Price'], label='Price', shade=True)


# In[30]:


top_subs = udemy[['Title','Subscribers']].sort_values(by='Subscribers', ascending=False).head(10)
print(top_subs)


# In[64]:


y=top_subs['Title'].values
x=top_subs['Subscribers'].values
plt.figure(figsize=(15,10))
sns.barplot(x,y,palette='Blues_d')
plt.xlabel('Subscribers')
plt.ylabel('Course')
plt.title('POPULAR COURSES ACCORDING TO SUBSCIPTION')


# In[31]:


top_reviews = udemy[['Title','Reviews']].sort_values(by='Reviews', ascending=False).head(10)
print(top_reviews)


# In[65]:


y=top_reviews['Title'].values
x=top_reviews['Reviews'].values
plt.figure(figsize=(15,10))
sns.barplot(x,y,palette='Reds_d')
plt.xlabel('Reviews')
plt.ylabel('Course')
plt.title('POPULAR COURSES ACCORDING TO REVIEWS')


# In[70]:


(udemy.groupby("Title")[["Subscribers", "Reviews"]].sum().sort_values("Reviews", ascending= False)).style.background_gradient()


# As the number one course is "2020 Complete Python Bootcamp: From Zero to Hero in Python" according to both "Subcribers" & "Reviews". Thus, number of reviews influences a prospective customer's decision to by the course.

# In[37]:


top_rating = udemy[['Title','Rating']].sort_values(by='Rating', ascending=False).head(20)
print(top_rating)


# In[36]:


top_price = udemy[['Title','Price']].sort_values(by='Price', ascending=False).head(20)
print(top_price)


# # Relationship between numerical columns

# In[39]:


udemy.plot(kind = 'scatter', x = 'Price', y = 'Subscribers', color = 'pink')
plt.xlabel('Price')
plt.ylabel('Subscribers')
plt.show()


# In[40]:


udemy.plot(kind = 'scatter', x = 'Reviews', y = 'Subscribers', color = 'red')
plt.xlabel('Reviews')
plt.ylabel('Subscribers')
plt.show()


# In[42]:


udemy.plot(kind = 'scatter', x = 'Rating', y = 'Subscribers', color = 'blue')
plt.xlabel('Rating')
plt.ylabel('Subscribers')
plt.show()


# In[45]:


udemy.plot(kind = 'scatter', x = 'Rating', y = 'Reviews', color = 'blue')
plt.xlabel('Rating')
plt.ylabel('Reviews')
plt.show()


# In[46]:


udemy0=udemy.copy()
udemy0['Published'] = pd.to_datetime(udemy['Published'])
udemy0['Published_date'] = udemy0['Published'].dt.date
udemy0['Published_year'] = pd.DatetimeIndex(udemy0['Published']).year


# In[49]:


udemy0[['Published_year','Title']].groupby(['Published_year']).count()


# In[50]:


plt.figure(figsize = (9,4))
sns.countplot(data = udemy0, x = 'Published_year')
plt.show()


# In[ ]:




