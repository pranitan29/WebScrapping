#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import numpy as np
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')


# In[2]:


from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException


# In[3]:


url='https://archive.ics.uci.edu/'
#open web driver
driver=webdriver.Chrome(r"C:\Users\vgoda\chromedriver.exe")
driver.get(url)


# In[4]:


data_sets=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/span/b/a')
try:
    data_sets.click()
except ElementNotInteractableException:#handling element not clickable exception
    driver.get(data_sets.get_attribute('href'))


# In[5]:


name=[]
try:
    names=driver.find_elements_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td[2]/p/b/a')
    for x in names:
        name.append(x.text)
except NoSuchElementException:
    name.append('-')
except StaleElementReferenceException:
    name.append('-')
print(len(name),name)


# In[6]:


data=[]
try:
    datas=driver.find_elements_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[2]/p')
    for x in datas:
        data.append(x.text)
except NoSuchElementException:
    data.append('-')
except StaleElementReferenceException:
    data.append('-')
data=data[1:]#first row is title of table 'Data Types'
print(len(data),data)


# In[7]:


task=[]
try:
    tasks=driver.find_elements_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[3]/p')
    for x in tasks:
        task.append(x.text)
except NoSuchElementException:
    task.append('-')
except StaleElementReferenceException:
    task.append('-')
task=task[1:]#first row is title of table 'Defult Task'
print(len(task),task)


# In[8]:


attribute_type=[]
try:
    types=driver.find_elements_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[4]/p')
    for x in types:
        attribute_type.append(x.text)
except NoSuchElementException:
    attribute_type.append('-')
except StaleElementReferenceException:
    attribute_type.append('-')
attribute_type=attribute_type[1:]#first row is title of table 'Attribute Types'
print(len(attribute_type),attribute_type)


# In[9]:


instance=[]
try:
    instances=driver.find_elements_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[5]/p')
    for x in instances:
        instance.append(x.text)
except NoSuchElementException:
    instance.append('-')
except StaleElementReferenceException:
    instance.append('-')
instance=instance[1:]#first row is title of table 'No of Instances'
print(len(instance),instance)


# In[10]:


attribute=[]
try:
    attributes=driver.find_elements_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[6]/p')
    for x in attributes:
        attribute.append(x.text)
except NoSuchElementException:
    attribute.append('-')
except StaleElementReferenceException:
    attribute.append('-')
attribute=attribute[1:]#first row is title of table 'No of Attribute'
print(len(attribute),attribute)


# In[11]:


year=[]
try:
    years=driver.find_elements_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[7]/p')
    for x in years:
        year.append(x.text)
except NoSuchElementException:
    year.append('-')
except StaleElementReferenceException:
    year.append('-')
year=year[1:]#first row is title of table 'No of Instances'
print(len(year),year)


# In[12]:


df=pd.DataFrame()
df['Dataset name']=name
df['Data type']=data
df['Task']=task
df['Attribute type']=attribute_type
df['No of instances']=instance
df['No of attribute']=attribute
df['Year']=year
df


# In[13]:


driver.close()


# In[ ]:




