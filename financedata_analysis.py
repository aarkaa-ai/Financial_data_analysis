import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
def load_data(file_path):
    """Load financial data from a CSV file."""
    try:
        data = pd.read_csv(r'C:\\Users\\Aryan\\Downloads\\sp500_trends.csv')
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Data Preprocessing
def preprocess_data(data):
    """Clean and preprocess the data."""
    data.dropna(inplace=True)  # Remove missing values
    data['Date'] = pd.to_datetime(data['Date'])  # Ensure date is in datetime format
    data.sort_values('Date', inplace=True)  # Sort by date
    print("Data preprocessing complete.")
    return data

# Data Summary
def data_summary(data):
    """Generate summary statistics."""
    print("Data Summary:")
    print(data.describe())
    print("\nColumn Data Types:")
    print(data.dtypes)

# Visualizations
def plot_time_series(data):
    """Plot time-series data for all numerical columns."""
    numerical_columns = data.select_dtypes(include=[np.number]).columns
    for column in numerical_columns:
        plt.figure(figsize=(10, 6))
        plt.plot(data['Date'], data[column], label=column)
        plt.title(f"Time Series of {column}")
        plt.xlabel('Date')
        plt.ylabel(column)
        plt.legend()
        plt.grid(True)
        plt.show()

def plot_correlation_matrix(data):
    """Plot a heatmap of the correlation matrix."""
    correlation = data.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

# Analysis
def calculate_moving_averages(data, window=30):
    """Calculate and plot moving averages for all numerical columns."""
    numerical_columns = data.select_dtypes(include=[np.number]).columns
    for column in numerical_columns:
        data[f'{column}_MA_{window}'] = data[column].rolling(window=window).mean()
        plt.figure(figsize=(10, 6))
        plt.plot(data['Date'], data[column], label='Original Data', color='blue')
        plt.plot(data['Date'], data[f'{column}_MA_{window}'], label=f'{window}-Day MA', color='orange')
        plt.title(f'{window}-Day Moving Average of {column}')
        plt.xlabel('Date')
        plt.ylabel(column)
        plt.legend()
        plt.grid(True)
        plt.show()

# Main Execution
def main():
    file_path = r'C:\\Users\\Aryan\\Downloads\\sp500_trends.csv'  # Replace with your file path
    data = load_data(file_path)
    if data is not None:
        data = preprocess_data(data)
        data_summary(data)

        # Visualizations
        plot_time_series(data)
        plot_correlation_matrix(data)

        # Moving Average Analysis
        calculate_moving_averages(data)

if __name__ == "__main__":
    main()
