import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from IPython import display
import seaborn as sn
import functions as f


print(f.df.head())
print(f.df.shape)

print(f.USAPop.head())
print(f.GDPandPop.head())

no_null = set(f.df.columns[f.df.isnull().mean()==0])

print("Columns that has no nulls \n", no_null)

most_missing_cols = set(f.df.columns[f.df.isnull().mean()>.50])

print("Columns that has 75% nulls \n", most_missing_cols)

count_city = f.df.City.value_counts()

most_city = count_city[:30]

print(most_city)

dict_city = dict(most_city)

list_city = list(dict_city.keys())

print(list_city)

count_country = f.df.Country.value_counts()


print("City with the most number of respondents: \n", most_city)

#print("List of the cities: \n", most_count[0])

(most_city/f.df.shape[0]).plot(kind="bar");
plt.title("Most Number of Data per City");
plt.show()
 
set_average = []
# initialize list of lists 
data = [] 
  
# Create the pandas DataFrame 
the_table = pd.DataFrame() 
for i in list_city:
    print("The average number of mins to park in", i, "is ",f.getAvgTimetoPark(i))
    state = (f.df.loc[f.df['City'] == i]['State']).to_string(index=False)
    state = state.split('\n')[0]
    state = state.strip()
    set_average.append([i, state])
    #set_average.append([i, f.getAvgTimetoPark(i)])

print(f.df.loc[f.df['City'].isin(list_city)]['State'])

state = f.df.loc[f.df['City'].isin(list_city)]['State']
print("state boi", state)

set_average=list(set_average)

set_average = pd.DataFrame(set_average)

set_average.columns = ['City', 'State']

#set_average.loc[[1], 'State'] = f.df.loc[f.df['City'].isin(list_city)]['State']

print(list(f.df.loc[f.df['City'].isin(list_city)]['State'])[1])
set_average.set_index('City', inplace=True)


print(pd.DataFrame(set_average))

for i in list_city:
    set_average.loc[i, 'Average time to park'] =  f.getAvgTimetoPark(i)
    print("The percentage of small car in ", i, "is ", f.getAvgPercentCar(i))
    set_average.loc[i, 'Percent of small cars']= f.getAvgPercentCar(i)
    print("The percentage of Multi-purpose Vehicles in ", i, "is ", f.getAvgBigCar(i))
    set_average.loc[i, 'Percent of Multi-purpose Vehicles']= f.getAvgBigCar(i)
    print("The percentage of Light Duty Trucks in ", i, "is ", f.getAvgLDTruck(i))
    set_average.loc[i, 'Percent of Light Duty Trucks']= f.getAvgLDTruck(i)
    print("The percentage of Medium Duty Trucks in ", i, "is ",f.getAvgMDTruck(i))
    set_average.loc[i, 'Percent of Medium Duty Trucks']= f.getAvgMDTruck(i)
    print("The percentage of Heavy Duty Trucks ", i, "is ", f.getAvgHDTruck(i))
    set_average.loc[i, 'Percent of Heavy Duty Trucks']= f.getAvgHDTruck(i)
    print("The percentage of unknown vehicles in ", i, "is ", f.getAvgOtherV(i))
    set_average.loc[i, 'Percent of unknown vehicles']= f.getAvgOtherV(i)
    print((f.GDPandPop.loc[f.GDPandPop['City'] == i]['Population']))
    set_average.loc[i, 'Population of the city']= (f.GDPandPop.loc[f.GDPandPop['City'] == i]['Population']).to_string(index=False)
    set_average.loc[i, 'GDP of the city']= (f.GDPandPop.loc[f.GDPandPop['City'] == i]['GDP(billion)']).to_string(index=False)
    
print(set_average.tail())

TimeandCars = set_average[['Average time to park', 'Percent of small cars', 'Percent of Multi-purpose Vehicles',
'Percent of Light Duty Trucks', 'Percent of Medium Duty Trucks', 'Percent of Heavy Duty Trucks',
'Percent of unknown vehicles']]

TimeCarsMatrix = TimeandCars.corr()

sn.heatmap(TimeCarsMatrix, annot=True)
plt.title("Correlation matrix of  Average Time to park and types of car")
plt.show()
#for i in list_city:
 #   population = (f.GDPandPop.loc[f.GDPandPop['City'] == i]['Population']).to_string(index=False)
  #  print('please work', population)

print(pd.DataFrame(set_average))

states = list(set_average['State'])
print(states)
print(f.USAPop.loc[f.USAPop['Name'].isin(states)]['Pop_2019'])

USAStatepopulation = []
for i in states:
    USAPopu = (f.USAPop.loc[f.USAPop['Name'] == i]['Pop_2019']).to_string(index=False)

    USAStatepopulation.append(USAPopu)  

print(USAStatepopulation)

set_average['Population of state'] = USAStatepopulation

print(pd.DataFrame(set_average))

set_average = set_average.reset_index()

set_average.plot(x ='City', y='Average time to park', kind = 'bar')
plt.xlabel('Average time to park')
plt.show()

set_average['Population of state']= pd.to_numeric(set_average['Population of state'], downcast="float")
set_average['GDP of the city']= pd.to_numeric(set_average['GDP of the city'], downcast="float")
set_average['Population of the city']= pd.to_numeric(set_average['Population of the city'], downcast="float")

set_average['Population of state'] = set_average['Population of state'].replace(0,set_average['Population of state'].mean())

corrTimePop = set_average['Average time to park'].corr(set_average['Population of the city'])
corrTimeGDP = set_average['Average time to park'].corr(set_average['GDP of the city'])

set_average.plot(x ='Average time to park', y='Population of the city', kind = 'scatter')
plt.title(corrTimePop);
plt.show()

set_average.plot(x ='Average time to park', y='GDP of the city', kind = 'scatter')
plt.title(corrTimeGDP);
plt.show()

print(corrTimePop)

print(set_average)
print(set_average.describe())

corrMatrix = set_average.corr()

sn.heatmap(corrMatrix, annot=True)
plt.title("Correlation matrix of  Time to park")
plt.show()