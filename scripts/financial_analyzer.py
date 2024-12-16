import yfinance as yf
import talib as ta
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pynance as pn


class FinancialAnalyzer:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def calculate_bollinger_bands(stock_data, window=20, num_std_dev=2):
        stock_data['BB_upper'], stock_data['BB_lower'] = pn.indicators.BBANDS(stock_data['Close'], window=window, num_std_dev=num_std_dev)
        return stock_data
    
    def retrieve_stock_data(ticker, start_date, end_date):

        return yf.download(ticker, start=start_date, end=end_date)
    
    def calculate_technical_indicators(data):
        # Ensure 'Close' column exists and is numeric
        if 'Close' not in data.columns or not pd.api.types.is_numeric_dtype(data['Close']):
            raise ValueError("'Close' column is missing or not numeric.")
        
        # Calculate indicators
        data['SMA'] = ta.SMA(data['Close'].to_numpy(), timeperiod=3)
        data['RSI'] = ta.RSI(data['Close'].to_numpy(), timeperiod=2)
        data['EMA'] = ta.EMA(data['Close'].to_numpy(), timeperiod=3)
        macd, macd_signal, _ = ta.MACD(data['Close'].to_numpy())
        data['MACD'] = macd
        data['MACD_Signal'] = macd_signal
        return data

    def plot_stock_and_sma(df):
        """Plot stock closing price and 14-day SMA"""
        plt.figure(figsize=(12, 6))
        plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
        plt.plot(df['Date'], df['SMA_14'], label='14-Day SMA', color='orange')
        plt.title('AAPL Stock Price and 14-Day Moving Average')
        plt.xlabel('Date')
        plt.ylabel('Price ')
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_rsi(df):
        """Plot RSI (Relative Strength Index)"""
        plt.figure(figsize=(12, 6))
        plt.plot(df['Date'], df['RSI'], label='RSI (14)', color='green')
        plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
        plt.axhline(30, color='blue', linestyle='--', label='Oversold (30)')
        plt.title('RSI (14) for AAPL Stock')
        plt.xlabel('Date')
        plt.ylabel('RSI')
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_macd(df):
        """Plot MACD and Signal Line"""
        plt.figure(figsize=(12, 6))
        plt.plot(df['Date'], df['MACD'], label='MACD', color='blue')
        plt.plot(df['Date'], df['MACD_signal'], label='MACD Signal', color='orange')
        plt.bar(df['Date'], df['MACD_hist'], label='MACD Histogram', color='gray', alpha=0.3)
        plt.title('MACD and Signal Line for AAPL Stock')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.grid(True)
        plt.show()
