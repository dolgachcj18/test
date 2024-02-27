import yfinance as yf
import mplfinance as mpf
import pandas as pd

# Fetch historical data for Tesla
tesla_data = yf.download('TSLA', start='2020-01-01', end='2024-01-01')

# Calculate the 50-day and 200-day moving averages
tesla_data['50_MA'] = tesla_data['Close'].rolling(window=50).mean()
tesla_data['200_MA'] = tesla_data['Close'].rolling(window=200).mean()

# Define the plot style
mpf_style = mpf.make_mpf_style(base_mpf_style='charles', rc={'font.size':8})

# Define additional plot parameters
add_plot = [
    mpf.make_addplot(tesla_data['50_MA'], color='blue', width=0.75),
    mpf.make_addplot(tesla_data['200_MA'], color='red', width=0.75)
]

# Plot the candlestick chart
mpf.plot(tesla_data, type='candle', style=mpf_style, addplot=add_plot, volume=True, title='Tesla Stock Price', ylabel='Price ($)')


