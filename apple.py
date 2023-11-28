import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
#latest commit from 1
#add a test comment for git
#add a test commit for git
#add another from 1
#add from 1
#add a commit from 2
#add a commit from 2




api_key = 'LoFnR1KClYf85Nr4q66uMMCjXd502JAf'
stock_symbol = 'AAPL'

def fetch_dividend_data(stock_symbol, api_key):
    url = f'https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/{stock_symbol}?apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data['historical'])

def fetch_latest_stock_price(stock_symbol, api_key):
    price_url = f'https://financialmodelingprep.com/api/v3/quote/{stock_symbol}?apikey={api_key}'
    price_response = requests.get(price_url)
    price_data = price_response.json()
    return price_data[0]['price']

def calculate_dividend_yield(dividend, stock_price):
  return dividend / stock_price * 100

#dividends_df['growth_rate'] = dividends_df['dividend'].pct_change()
#average_growth_rate = dividends_df['growth_rate'].mean() * 100

def calculate_payout_ratio(dividends, earnings):
  return dividends / earnings * 100


if __name__ == '__main__':
    dividend_data = fetch_dividend_data(stock_symbol, api_key)

    dividend_data['date'] = pd.to_datetime(dividend_data['date'])
    plt.figure(figsize=(12,6))
    plt.plot(dividend_data['date'], dividend_data['dividend'])
    plt.title(f'Dividend Trend for {stock_symbol}')
    plt.xlabel('Date')
    plt.ylabel('Dividend Amount')
    plt.grid(True)
    plt.show()
    plt.close()



    stocks = ['AAPL', 'MSFT', 'NVDA']
    yields = []

    for stock in stocks:
        latest_price = fetch_latest_stock_price(stock, api_key)
        dividend_data = fetch_dividend_data(stock, api_key)
        latest_dividend = dividend_data.iloc[0]['dividend'] if not dividend_data.empty else 0
        yield_value = (latest_dividend / latest_price * 100) if latest_price else 0
        yields.append(yield_value)

    plt.bar(stocks, yields)
    plt.title('Comparative Dividend Yields')
    plt.xlabel('Stock')
    plt.ylabel('Dividend Yield (%)')
    plt.show()
