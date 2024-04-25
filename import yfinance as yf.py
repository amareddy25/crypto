import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Function to fetch Bitcoin data and plot
def fetch_and_plot_btc(start_date, end_date):
    data = yf.download("BTC-USD", start=start_date, end=end_date)

    plt.figure(figsize=(50, 15))
    plt.plot(data.index, data['Close'], marker='o', linestyle='-', color='b')
    plt.title('Bitcoin Prices')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.grid(True)
    plt.show()

# Calculates and prints the price from 3 days ago
    three_days_ago = (datetime.strptime(end_date, '%Y-%m-%d') - timedelta(days=3)).strftime('%Y-%m-%d')
    if three_days_ago in data.index.strftime('%Y-%m-%d'):
        price_three_days_ago = data.loc[three_days_ago, 'Close']
        print(f"The price of Bitcoin 3 days ago ({three_days_ago}): ${price_three_days_ago:.2f}")
    else:
        print("No data available for 3 days ago.")

#Enter your date range here:
start_date = "2008-04-15"
end_date = "2024-04-25"
fetch_and_plot_btc(start_date, end_date)