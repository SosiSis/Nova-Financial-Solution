import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_data(df, date_column='date', stock_value_column='stock_value', title='Stock Value Over Time'):
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce', infer_datetime_format=True)
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
    data_frame['date'] = pd.to_datetime(data_frame['date'], errors='coerce', infer_datetime_format=True)
    data_frame.dropna(subset=['date'], inplace=True)

    daily_counts = data_frame.groupby(data_frame['date'].dt.date).size()

    plt.figure(figsize=(12, 6))
    plt.plot(daily_counts.index, daily_counts.values, marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Counts')
    plt.title('Time Series Analysis')
    plt.grid(True)
    plt.show()

def publishing_times(data_frame):
    data_frame['date'] = pd.to_datetime(data_frame['date'], errors='coerce', infer_datetime_format=True)
    data_frame.dropna(subset=['date'], inplace=True)

    data_frame['hour'] = data_frame['date'].dt.hour
    hourly_counts = data_frame['hour'].value_counts().reindex(range(24), fill_value=0)

    plt.bar(hourly_counts.index, hourly_counts.values, color='skyblue')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Publications')
    plt.title('Publishing Times')
    plt.grid(True, axis='y')
    plt.show()
