import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from IPython import display

df = pd.read_csv('./Searching_for_parking_NA.csv', index_col=False)
USAPop = pd.read_csv('./USA population.csv')
GDPandPop = pd.read_csv('./Top 30 Population GDP.csv')

def getAverageColumn(city, column):
    #INPUT: Name of the city[to select specific rows] and Column name from Searching_for_parking_NA.csv
    # Output: Average of the column[column] and selected rows[city] 
    city_df = df.loc[df['City'] == city]
    average = city_df[column].mean()
    return average


def getAvgTimetoPark(city):
    city_df = df.loc[df['City'] == city]
    average = city_df["AvgTimeToPark"].mean()
    return average