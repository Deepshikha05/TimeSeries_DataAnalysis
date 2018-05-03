import pandas as pd
import argparse
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
from math import factorial
from scipy.signal import savgol_filter


def weekly_report(city):
    # Set frequency as below to get weekly data picked up. 
    # It is set like this because ((24hrs * 60 mins)/(1min- the interval for what data has been taken)) * (7days- for the weekly report)
    decompfreq = ((24*60)/1)*7
    decompfreq = int(decompfreq)

    asd = pd.to_datetime(data.DateTime)
    data.DateTime = asd
    data.set_index('DateTime', inplace=True)

    # Seasonal decompose to get the trend, seasonality, residual and observed data.
    # Additive model is used because the dataset contain values as zero and so the multiplicative model cannot be used because then it would generate the value = 0
    res = sm.tsa.seasonal_decompose(data[city].interpolate(), freq=decompfreq, model='additive')
    resplot = res.plot()
    plt.title('Weekly Report of ' + city)
    plt.show()
    

def daily_report(city):
    # Set frequency as below to get daily data picked up. 
    # It is set like this because ((24hrs * 60 mins)/(1min- the interval for what data has been taken)) * (1 day- for the daily report)
    decompfreq = ((24*60)/1)*1
    decompfreq = int(decompfreq)

    asd = pd.to_datetime(data.DateTime)
    data.DateTime = asd
    data.set_index('DateTime', inplace=True)

    res = sm.tsa.seasonal_decompose(data[city].interpolate(), freq=decompfreq, model='additive')
    resplot = res.plot()
    plt.title('Daily Report of ' + city)
    plt.show()


def hourly_report(city):
    # Set frequency as below to get hourly data picked up. 
    # It is set like this because ((24hrs * 60 mins)/(1min- the interval for what data has been taken)) * (1/24 hour- for the hourly report)
    decompfreq = ((24*60)/1)*(1/24)
    decompfreq = int(decompfreq)

    asd = pd.to_datetime(data.DateTime)
    data.DateTime = asd
    data.set_index('DateTime', inplace=True)

    res = sm.tsa.seasonal_decompose(data[city].interpolate(), freq=decompfreq, model='additive')
    resplot = res.plot()
    plt.title('Hourly Report of ' + city)
    plt.show()

# To set keyword arguments; -c used to take argument for the city; -r is used to take argument for the kind of report to be generated
parser = argparse.ArgumentParser(description='Generating Reports')
parser.add_argument('-c', '--city_name', default='all', help="City Name")
parser.add_argument('-r', '--report_type', default='all', help="Report Type")

args = parser.parse_args()

if args.city_name:
    City = args.city_name

# Reading the corresponding input file
path = City+'.csv'
data = pd.read_csv(path, header=0, names=['DateTime', City], date_parser=True)
import pdb; pdb.set_trace()

# To drop all the Nan in the dataset
city_data = pd.Series.to_frame(data[City]).dropna(axis=0, how='all')
# Convert city_data type to numpy.ndarray
city_data = city_data.values
# Convert it to a 1D array
city_data = city_data.ravel()
# Applying savgol_filter to the data 
city_data = savgol_filter(city_data, 51, 3, mode='nearest')
city_data = pd.Series(city_data)

# asd = pd.to_datetime(data.DateTime)
# data.DateTime = asd
# data.set_index('DateTime', inplace=True)

# Passing input arguments to the data
data[City] = city_data

# Checking for the type of report requested and then calling the corresponding function for the type of report
if args.report_type:
    ReportType = args.report_type

    if ReportType == 'weekly':
        weekly_report(City)

    elif ReportType == 'daily':
        daily_report(City)

    elif ReportType == 'hourly':
        hourly_report(City)

    else:
        print('Wrong input')
else:
    print('Enter report type')



