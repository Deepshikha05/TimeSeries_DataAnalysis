#Time Series Data Analysis#



# README #

This project uses timeseries data of a particular city and the power consumption in mcu sampled over 1 second.

### The Working ###

* Data is first read from the csv file.
* Plot graph between datetime and power consumption to analyze the data.
* Make data stationary.
* Apply Dickey Fuller Test to check if the data is stationary or not.
* Plot ACF and PACF Graph and find optimal parameters.
* Build ARIMA Model to make predictions.

### Dependencies ###
`statsmodels`
`matplotlib`
`pandas`
`numpy`

 The exact dependencies can be downloaded by running `pip install -r requirements.txt`

* install requests using `pip install requests`


### Common Issues ###

* The most common issue seems to be stationarity of data. It is very important that the data is stationary before predictions can be made on it. That's because the basic assumption for linear regression is that the two parameters are not dependent on each other whereas in the the power consumption is dependent on date time.
* Using different lag values for making the data stationary. Many a times one has to try different lag values to make the data stationary and then plot ACF and PACF graph and also apply Dickey Fuller Test to check for stationarity of the data.
* Plotting graph of power against datetime requires datatime to be first changed into index.

### Make a virtual environment(optional) ###
* run `virtualenv -p python3 venv` inside the project directory
* run `install jupyter notebook` to install jupyter notebook
