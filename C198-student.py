#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name : ")
print("Find the Correlation between the Natural Gas Consumption and Total Population from 2010-2014.")
print("Find the Correlation between the Coal Consumption and Coal Price  from 2010-2014.")


# # Activty 1- Find the Correlation between the Natural Gas Consumption and Total Population from 2010-2014.

# In[2]:


#image 
#predefine code for image
from IPython.display import Image
Image(filename='natural_gas.png') 
#predefine code end


# In[ ]:


#import libraries and csv
import pandas as pd
import matplotlib.pyplot as plt 

pd.set_option('display.max_columns', None)

df = pd.read_csv('Energy Census and Economic Data US 2010-2014.csv')
df



# In[ ]:


#Get the column number of POPESTIMATE2010 
POPESTIMATE2010 = df.columns.get_loc("POPESTIMATE2010")
POPESTIMATE2010


# In[ ]:


#Get the column number of POPESTIMATE2014
POPESTIMATE2014 = df.columns.get_loc("POPESTIMATE2014")
POPESTIMATE2014


# In[ ]:


#Create new dataframe only for Population colums and state column
population_dataframe = df[df.columns[POPESTIMATE2010:POPESTIMATE2014+1] ] 
population_dataframe['State'] = df['State']
population_dataframe



# In[ ]:


#from population_dataframe find the row for New Jersey and create a new dataframe
new_jersey_population= population_dataframe.loc[population_dataframe['State'] == 'New Jersey']
new_jersey_population
 


# In[ ]:


#Get the column number of NatGasC2010 
NatGasC2010 = df.columns.get_loc("NatGasC2010")
NatGasC2010


# In[ ]:


#Get the column number of NatGasC2014
NatGasC2014 = df.columns.get_loc("NatGasC2014")
NatGasC2014


# In[ ]:


#Create new dataframe only for Natural Gas colums
natural_gas_dataframe = df[df.columns[NatGasC2010:NatGasC2014 + 1] ] 
natural_gas_dataframe['State'] = df['State']
natural_gas_dataframe



# In[ ]:


#from natural_gas_dataframe find the row for New Jersey and create a new dataframe
new_jersey_gas= natural_gas_dataframe.loc[natural_gas_dataframe['State'] == 'New Jersey']
new_jersey_gas
 


# In[ ]:


#Multiply each natural gas year value with 10 for making it normalize
new_jersey_gas['NatGasC2010'] = new_jersey_gas['NatGasC2010']*10
new_jersey_gas['NatGasC2011'] = new_jersey_gas['NatGasC2011']*10
new_jersey_gas['NatGasC2012'] = new_jersey_gas['NatGasC2012']*10
new_jersey_gas['NatGasC2013'] = new_jersey_gas['NatGasC2013']*10
new_jersey_gas['NatGasC2014'] = new_jersey_gas['NatGasC2014']*10
new_jersey_gas


# In[ ]:


#Create a common dataframe for Population and NatGasConsumption
columns_gas = ['Year' , 'Population','NatGasConsumption']
index_gas  = [1,2,3,4,5]
data_gas =[
    [2010,new_jersey_population['POPESTIMATE2010'].values[0],new_jersey_gas['NatGasC2010'].values[0]],
    [2011,new_jersey_population['POPESTIMATE2011'].values[0],new_jersey_gas['NatGasC2011'].values[0]],
    [2012,new_jersey_population['POPESTIMATE2012'].values[0],new_jersey_gas['NatGasC2012'].values[0]],
    [2013,new_jersey_population['POPESTIMATE2013'].values[0],new_jersey_gas['NatGasC2013'].values[0]],
    [2014,new_jersey_population['POPESTIMATE2014'].values[0],new_jersey_gas['NatGasC2014'].values[0]],

]
final_gas = pd.DataFrame(data_gas, index=index_gas, columns=columns_gas)
final_gas



# In[ ]:


#plot a line graph for showing Natural Gas Consumption vs Population
fig = plt.subplots(figsize=(10,6))
label = final_gas['Year']
value = final_gas['NatGasConsumption']


plt.plot(label, value, label = "NatGasConsumption" , linewidth=3.0)

label = final_gas['Year']
value = final_gas['Population']
plt.plot(label, value, label = "Population" , linewidth=3.0)

plt.xlabel('Population')

plt.ylabel('NatGasConsumption')

plt.title('NatGasConsumption VS Population in New Jersey', fontsize=20)

plt.legend()

plt.show()


# Conslusion : The Natural Gas Consumption and Population growth was constant from 2010 till 2012 in New Jersey, after 2012 there was significant growth in Population which lead to significant growth Natural Gas Consumption

# # Activity 2 - Find the Correlation between the Coal Consumption and Coal Price  from 2010-2014.

# In[3]:


#image 
#predefine code for image
from IPython.display import Image
Image(filename='natural_gas.jpg') 
#predefine code end


# In[ ]:


#predefine code 
#import libraries and csv
import pandas as pd
import matplotlib.pyplot as plt 

pd.set_option('display.max_columns', None)

df = pd.read_csv('Energy Census and Economic Data US 2010-2014.csv')
df

#predefine code end


# In[4]:


#Get the column number of CoalC2010 
CoalC2010 = df.columns.get_loc("CoalC2010")
CoalC2010


# In[5]:


#Get the column number of CoalC2014 
CoalC2014 = df.columns.get_loc("CoalC2014")
CoalC2014


# In[6]:


#Create new dataframe only columns for Coal
Coal_dataframe = df[df.columns[CoalC2010:CoalC2014 + 1]]
Coal_dataframe['State'] = df['State']
Coal_dataframe


# In[7]:


#from Coal_dataframe find the row for New Mexico and create a new dataframe
new_mexico_coal = Coal_dataframe.loc[Coal_dataframe['State'] == 'New Mexico']
new_mexico_coal


# In[8]:


#Get the column number of CoalPrice2010
CoalPrice2010 = df.columns.get_loc("CoalPrice2010")
CoalPrice2010


# In[9]:


#Get the column number of CoalPrice2014
CoalPrice2014 = df.columns.get_loc("CoalPrice2014")
CoalPrice2014


# In[10]:


#Create new dataframe only  columns for Coal_price
Coal_price_dataframe = df[df.columns[CoalPrice2010:CoalPrice2014 + 1]]
Coal_price_dataframe['State'] = df['State']
Coal_price_dataframe


# In[11]:


#from Coal_price_dataframe find the row for New Mexico and create a new dataframe
new_mexico_coal_price = Coal_price_dataframe.loc[Coal_dataframe['State'] == 'New Mexico']
new_mexico_coal_price


# In[12]:


#Multiply each CoalPrice year wise column values with 100000 for making it normalize
new_mexico_coal_price['CoalPrice2010'] = new_mexico_coal_price['CoalPrice2010'] * 100000
new_mexico_coal_price['CoalPrice2011'] = new_mexico_coal_price['CoalPrice2011'] * 100000
new_mexico_coal_price['CoalPrice2012'] = new_mexico_coal_price['CoalPrice2012'] * 100000
new_mexico_coal_price['CoalPrice2013'] = new_mexico_coal_price['CoalPrice2013'] * 100000
new_mexico_coal_price['CoalPrice2014'] = new_mexico_coal_price['CoalPrice2014'] * 100000
new_mexico_coal_price


# In[13]:


#Create a common dataframe for coalConsumption and coalPrice
columns_gas = ['Year', 'Population', 'NatGasComsumption']
index_gas = [1, 2, 3, 4, 5]
data_gas = [
    [2010, new_jersey_population['POPESTIMATE2010'].values[0], new_jersey_gas['NatGasC2010'].values[0]],
    [2011, new_jersey_population['POPESTIMATE2011'].values[0], new_jersey_gas['NatGasC2011'].values[0]],
    [2012, new_jersey_population['POPESTIMATE2012'].values[0], new_jersey_gas['NatGasC2012'].values[0]],
    [2013, new_jersey_population['POPESTIMATE2013'].values[0], new_jersey_gas['NatGasC2013'].values[0]],
    [2014, new_jersey_population['POPESTIMATE2014'].values[0], new_jersey_gas['NatGasC2014'].values[0]],
]
final_coal = pd.DataFrame(data_gas, index = index_gas, columns = columns_gas)
final_coal


# In[17]:


#Plot a line graph showing the correlation between the Coal Consumption and Coal Price 

#plot the line for showing year wise coal consumption
plt.subplots(figsize=(19,8))

label = final_coal['Year']
value = final_coal['coalConsumption']
plt.plot(label, value, label = "coalConsumption" , linewidth=3.0)

#----------------------------------------------------------------------------------------
#Plot the line for showing the year wise coal price

label = final_coal['Year']
value = final_coal['coalPrice']
plt.plot(label, value, label = "coalPrice" , linewidth=3.0)

#----------------------------------------------------------------------------------------
plt.xlabel('Dates')
plt.ylabel('Coal Consumption VS Coal Price ')
plt.title('Coal Consumption VS Coal Price ', fontsize=20)
plt.legend()
plt.show()


# Conslusion : 

# In[ ]:





# In[ ]:





# In[ ]:




