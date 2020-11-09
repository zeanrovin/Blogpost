import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from IPython import display
import seaborn as sn
import functions as f

"""
This is a Udacity blogpost project

"""

#describe the df 
print(f.df.head())
print(f.df.shape)

print(f.USAPop.head())
print(f.GDPandPop.head())

no_null = set(f.df.columns[f.df.isnull().mean()==0])

#See columns if there are Nan values
print("Columns that has no nulls \n", no_null)

most_missing_cols = set(f.df.columns[f.df.isnull().mean()>.50])

print("Columns that has 75% nulls \n", most_missing_cols)

count_city = f.df.City.value_counts()

#Get top 30 recorded cities
most_city = count_city[:30]

print(most_city)

dict_city = dict(most_city)

list_city = list(dict_city.keys())

print(list_city)

count_country = f.df.Country.value_counts()


print("City with the most number of respondents: \n", most_city)

#First Graph: Number of records per city/Total number of records

(most_city/f.df.shape[0]).plot(kind="bar");
plt.title("Most Number of Data per City");
plt.show()
 
main_df = [] #The consolidated rows and columns that will be used for this project
# initialize list of lists 
data = [] 
  
for i in list_city:
    print("The average number of mins to park in", i, "is ",f.getAvgTimetoPark(i))
    state = (f.df.loc[f.df['City'] == i]['State']).to_string(index=False)
    state = state.split('\n')[0]
    state = state.strip()
    main_df.append([i, state])
    #main_df.append([i, f.getAvgTimetoPark(i)])

print(f.df.loc[f.df['City'].isin(list_city)]['State'])

state = f.df.loc[f.df['City'].isin(list_city)]['State']
print("Corresponding states of the cities: ", state)

main_df=list(main_df)

main_df = pd.DataFrame(main_df)

main_df.columns = ['City', 'State']


print(list(f.df.loc[f.df['City'].isin(list_city)]['State'])[1])
main_df.set_index('City', inplace=True)


print(pd.DataFrame(main_df))

for i in list_city:
    main_df.loc[i, 'Average time to park'] =  f.getAvgTimetoPark(i)
    print("The percentage of small car in ", i, "is ", f.getAverageColumn(i, 'PercentCar'))
    main_df.loc[i, 'Percent of small cars']= f.getAverageColumn(i, 'PercentCar')
    print("The percentage of Multi-purpose Vehicles in ", i, "is ", f.getAverageColumn(i, 'PercentMPV'))
    main_df.loc[i, 'Percent of Multi-purpose Vehicles']= f.getAverageColumn(i, 'PercentMPV')
    print("The percentage of Light Duty Trucks in ", i, "is ", f.getAverageColumn(i, 'PercentLDT'))
    main_df.loc[i, 'Percent of Light Duty Trucks']= f.getAverageColumn(i, 'PercentLDT')
    print("The percentage of Medium Duty Trucks in ", i, "is ",f.getAverageColumn(i, 'PercentMDT'))
    main_df.loc[i, 'Percent of Medium Duty Trucks']= f.getAverageColumn(i, 'PercentMDT')
    print("The percentage of Heavy Duty Trucks ", i, "is ", f.getAverageColumn(i, 'PercentHDT'))
    main_df.loc[i, 'Percent of Heavy Duty Trucks']= f.getAverageColumn(i, 'PercentHDT')
    print("The percentage of unknown vehicles in ", i, "is ", f.getAverageColumn(i, 'PercentOther'))
    main_df.loc[i, 'Percent of unknown vehicles']= f.getAverageColumn(i, 'PercentOther')
    print((f.GDPandPop.loc[f.GDPandPop['City'] == i]['Population']))
    main_df.loc[i, 'Population of the city']= (f.GDPandPop.loc[f.GDPandPop['City'] == i]['Population']).to_string(index=False)
    main_df.loc[i, 'GDP of the city']= (f.GDPandPop.loc[f.GDPandPop['City'] == i]['GDP(billion)']).to_string(index=False)
    
print(main_df.tail())

TimeandCars = main_df[['Average time to park', 'Percent of small cars', 'Percent of Multi-purpose Vehicles',
'Percent of Light Duty Trucks', 'Percent of Medium Duty Trucks', 'Percent of Heavy Duty Trucks',
'Percent of unknown vehicles']]

TimeCarsMatrix = TimeandCars.corr()

#Second Graph: Heatmap of Average time to park and different types of car
sn.heatmap(TimeCarsMatrix, annot=True)
plt.title("Correlation matrix of  Average Time to park and types of car")
plt.show()

print(pd.DataFrame(main_df))

states = list(main_df['State'])
print(states)
print(f.USAPop.loc[f.USAPop['Name'].isin(states)]['Pop_2019'])

USAStatepopulation = []
for i in states:
    USAPopu = (f.USAPop.loc[f.USAPop['Name'] == i]['Pop_2019']).to_string(index=False)

    USAStatepopulation.append(USAPopu)  

print(USAStatepopulation)

main_df['Population of state'] = USAStatepopulation

print(pd.DataFrame(main_df))

main_df = main_df.reset_index()

# Third graph: Bar graph of cities and their average time to park mean
main_df.plot(x ='City', y='Average time to park', kind = 'bar')
plt.xlabel('Average time to park')
plt.show()

# Parsing 'Population of state', 'GDP of the city' and 'Population of the city' columns to float
main_df['Population of state']= pd.to_numeric(main_df['Population of state'], downcast="float")
main_df['GDP of the city']= pd.to_numeric(main_df['GDP of the city'], downcast="float")
main_df['Population of the city']= pd.to_numeric(main_df['Population of the city'], downcast="float")

#Declare correlation of independent and dependent variables
corrTimePop = main_df['Average time to park'].corr(main_df['Population of the city'])
corrTimeGDP = main_df['Average time to park'].corr(main_df['GDP of the city'])

#Fourth graph: Scatter graph showing correlation of Average time to park to Population
main_df.plot(x ='Average time to park', y='Population of the city', kind = 'scatter')
plt.title(corrTimePop);
plt.show()

#Fourth graph: Scatter graph showing correlation of Average time to park to GDP
main_df.plot(x ='Average time to park', y='GDP of the city', kind = 'scatter')
plt.title(corrTimeGDP);
plt.show()

print(corrTimePop)

print(main_df)
print(main_df.describe())

corrMatrix = main_df.corr()

#Fifth graph: Heatmap of main_df, showing correlation of each table
sn.heatmap(corrMatrix, annot=True)
plt.title("Correlation matrix of  Time to park")
plt.show()

#Additional graphs: 
pd.plotting.scatter_matrix(main_df, diagonal='kde')
plt.show()
