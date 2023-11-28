import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from apple import fetch_dividend_data

api_key = 'LoFnR1KClYf85Nr4q66uMMCjXd502JAf'
stock_symbol = 'AAPL'


dividend_data = fetch_dividend_data(stock_symbol, api_key)
dividend_data = dividend_data.sort_index(ascending=False)
dividend_data['date'] = pd.to_datetime(dividend_data['date'])
dividend_data.set_index('date', inplace=True)

# Fit the ARIMA model
model = ARIMA(dividend_data['dividend'], order=(1, 1, 1))
model_fit = model.fit()

# Forecast the next 12 months
forecast = model_fit.get_forecast(steps=12)
forecast_mean = forecast.predicted_mean
conf_int = forecast.conf_int()

# Plot the historical dividends
plt.figure(figsize=(14, 7))
plt.plot(dividend_data.index, dividend_data['dividend'], label='Historical Dividends')

# Generate the future dates correctly from the last date of historical data
last_hist_date = dividend_data.index[-1]
forecast_dates = pd.date_range(start=last_hist_date, periods=13, freq='M')[1:]

# Plot the forecast with confidence intervals
plt.plot(forecast_dates, forecast_mean, color='orange', label='Forecast')
plt.fill_between(forecast_dates, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='grey', alpha=0.3)

plt.title('Dividend Forecast for AAPL')
plt.xlabel('Date')
plt.ylabel('Dividend Amount')
plt.legend()
plt.show()