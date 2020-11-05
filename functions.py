import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from IPython import display

df = pd.read_csv('./Searching_for_parking_NA.csv', index_col=False)
USAPop = pd.read_csv('./USA population.csv')
GDPandPop = pd.read_csv('./Top 30 Population GDP.csv')

def getAvgPercentCar(city):
    city_df = df.loc[df['City'] == city]
    average = city_df["PercentCar"].mean()
    return average



def getAvgBigCar(city):
    city_df = df.loc[df['City'] == city]
    average = city_df["PercentMPV"].mean()
    return average

def getAvgLDTruck(city):
    city_df = df.loc[df['City'] == city]
    average = city_df["PercentLDT"].mean()
    return average

def getAvgMDTruck(city):
    city_df = df.loc[df['City'] == city]
    average = city_df["PercentMDT"].mean()
    return average

def getAvgHDTruck(city):
    city_df = df.loc[df['City'] == city]
    average = city_df["PercentHDT"].mean()
    return average

def getAvgOtherV(city):
    city_df = df.loc[df['City'] == city]
    average = city_df["PercentOther"].mean()
    return average

def getAvgTimetoPark(city):
    city_df = df.loc[df['City'] == city]
    average = city_df["AvgTimeToPark"].mean()
    return average