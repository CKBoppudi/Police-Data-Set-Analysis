#!/usr/bin/env python
# coding: utf-8

# # Police Data set Analysis 

# In[ ]:


# Firstly importing Pandas as pd


# In[2]:


import pandas as pd


# In[3]:


police = pd.read_csv(r"C:\Users\DELL\Desktop\Projects datasets\3. Police Data.csv")


# In[4]:


police


# In[ ]:


# To get the number of column and rows of the data set .shape command is used 


# In[5]:


police.shape 


# # Instruction (For data cleaning)
# # Remove the column that only contains missing values 

# In[6]:


police.head()


# In[ ]:


# To find the column that is having no values .isnull().sum() command is used 


# In[7]:


police.isnull().sum()


# In[ ]:


# From the above information the column country_name have no values entered
# So in the below cell executing the code to remove the countr_name column


# In[12]:


police.drop(columns = "country_name" , inplace = True)


# In[13]:


police


# In[14]:


# From the data above the required column have been removed 


# # Question - based on filtering and value_counts 
# # For speeding, who were stopped more often - Men or women

# In[15]:


police.head()


# In[21]:


police[police.violation == "Speeding"].driver_gender.value_counts()


# In[ ]:


# So, clearly from the above the number of men are stopped more often for speeding violation.


# # Does gender affects who gets searched during a stop?

# In[22]:


police.head()


# In[23]:


police.groupby("driver_gender").search_conducted.sum()


# In[27]:


police.search_conducted.value_counts()


# # What is the mean for stop_duration 

# In[28]:


police.head()


# In[31]:


police["stop_duration"].mean()


# In[ ]:


# There is an error in the above while executing the code because the format of column is string while it has to be integer.
#so we have to use the map function for changing string to integer.


# In[38]:


police.head()


# In[39]:


police["stop_duration"].value_counts()


# In[40]:


police.stop_duration.value_counts()


# In[47]:


police["stop_duration"] = police["stop_duration"].map({"0-15 Min" : 7.5 , "16-30 Min" : 24 , "30+ Min " : 45})


# In[48]:


police.stop_duration.mean()


# In[49]:


police["stop_duration"].mean()


# # Question ( groupby, describe() )
# # Compare the age distributions of each violation.

# In[50]:


police.head()


# In[52]:


police.groupby("violation").driver_age.describe()


# In[53]:


police.shape


# In[57]:


police.describe()


# In[ ]:




