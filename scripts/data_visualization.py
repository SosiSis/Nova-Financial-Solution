import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_data(df, date_column='date', stock_value_column='stock_value', title='Stock Value Over Time'):
    """
    Plots stock value over time from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.
    - date_column (str): The name of the date column in the CSV file (default is 'date').
    - stock_value_column (str): The name of the stock value column in the CSV file (default is 'stock_value').
    - title (str): Title for the plot (default is 'Stock Value Over Time').
    """

    df[date_column] = pd.to_datetime(df[date_column], errors='coerce', format='%Y-%m-%d %H:%M:%S')

    df.dropna(subset=[date_column], inplace=True)

    plt.figure(figsize=(10, 6))
    plt.plot(df[date_column], df[stock_value_column], label=stock_value_column, color='b')

    plt.xlabel('Date')
    plt.ylabel('Stock Value')
    plt.title(title)

    plt.xticks(rotation=45)

    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

def time_series_analysis(data_frame):
    # Convert 'date' column to datetime
    data_frame['date'] = pd.to_datetime(data_frame['date'], format="mixed", errors="coerce")
    
    # Drop rows with invalid dates
    data_frame = data_frame.dropna(subset=['date'])
    
    # Group by daily counts
    daily_counts = data_frame.groupby(data_frame['date'].dt.date).size()
    
    # Plot the time series
    plt.figure(figsize=(12, 6))
    plt.plot(daily_counts.index, daily_counts.values, marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Counts')
    plt.title('Time Series Analysis')
    plt.grid(True)
    plt.show()



def publishing_times(data_frame):

    data_frame['date'] = pd.to_datetime(data_frame['date'], format="%Y-%m-%d %H:%M:%S", errors="coerce")

    
    # Drop rows where 'date' conversion failed
    data_frame = data_frame.dropna(subset=['date'])
    
    # Extract the hour
    data_frame['hour'] = data_frame['date'].dt.hour
    
    # Count occurrences per hour
    hourly_counts = data_frame['hour'].value_counts().sort_index()
    
    # Plot the data
    plt.bar(hourly_counts.index, hourly_counts.values)
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Publications')
    plt.title('Publishing Times')
    plt.show()
