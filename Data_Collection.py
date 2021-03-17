#!/usr/bin/env python
# coding: utf-8

# In[166]:


#Import the data and save as data
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

#path = !pwd
#print(path)

'''if !pwd != '/Users/jackroubin/Desktop/Springboard/First_Capstone/data'
    path = !pwd
    #print(path)
    path = path[0] + "/data"
    #print(path)
    os.chdir(path)'''

data = pd.read_csv('aug_train.csv')
#data


# In[167]:


#Drop columns that do not add any useful information, rename the rest and save as data_drop
data.columns
data_rename_cols = data.rename(columns={'city_development_index':'City Development Index','gender':'Gender','relevent_experience':'Relevant Experience','enrolled_university':'Enrollment Status', 'education_level':'Education Level','major_discipline':'Major','experience':'Experience','last_new_job':'Last Job','training_hours':'Training Hours','target':'Target'})
data_rename_cols
data_drop = data_rename_cols.drop(['enrollee_id','city'], axis = 1)
#data_drop is all the revelant data to our target 


# In[169]:


#Find out which columns have a high percentage of na values
na_array = np.array(data_drop.isna().sum())
na_array_ratio = na_array/data_drop.shape[0]
na_array_ratio

missing = pd.concat([data_drop.isna().sum(),data_drop.isna().mean()], axis =1)
missing.columns = ['count', '%']
missing = missing.sort_values(by = ['count','%'])
missing


# In[171]:


#Make a new df with columns that have less than 10% Na's
data_drop2 = data_drop.drop(['Gender','Major','company_size','company_type'], axis =1)
data_drop
data_drop2


# In[172]:


#Find na percentages again
missing = pd.concat([data_drop2.isnull().sum(),data_drop2.isnull().mean()], axis =1)
missing.columns = ['count', '%']
missing = missing.sort_values(by = ['count','%'])
missing


# In[173]:


#Make a third df with no na's whatsoever(drop all rows that have any Na's)
data_drop2.shape
data_drop3 = data_drop2.dropna()
data_drop3.shape


# In[174]:


#Check how many of each Education Level there is
values = data_drop3[['Education Level']].value_counts()
values


# In[198]:


#Make 5 data frames, one for each eduction level
graduate = data_drop3[data_drop3['Education Level']=='Graduate'][['Education Level','Target']]
graduate = graduate.set_index(['Education Level'])
masters = data_drop3[data_drop3['Education Level']=='Masters'][['Education Level','Target']]
masters = masters.set_index(['Education Level'])
high_school = data_drop3[data_drop3['Education Level']=='High School'][['Education Level','Target']]
high_school = high_school.set_index(['Education Level'])
primary_school = data_drop3[data_drop3['Education Level']=='Primary School'][['Education Level','Target']]
primary_school = primary_school.set_index(['Education Level'])
phd = data_drop3[data_drop3['Education Level']=='Phd'][['Education Level','Target']]
phd = phd.set_index(['Education Level'])


# In[222]:


print(str(round(primary_school.value_counts()[1]/primary_school.value_counts().sum()*100)) + '% of primary school graduates get a job in data science.')
print(str(round(high_school.value_counts()[1]/high_school.value_counts().sum()*100)) + '% of high school graduates get a job in data science.')
print(str(round(graduate.value_counts()[1]/graduate.value_counts().sum()*100)) + '% of graduate graduates get a job in data science.')
print(str(round(masters.value_counts()[1]/masters.value_counts().sum()*100)) + '% of masters graduates get a job in data science.')
print(str(round(phd.value_counts()[1]/phd.value_counts().sum()*100)) + '% of Phd graduates get a job in data science.')


# In[ ]:




