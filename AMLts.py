TIME SERIES
pip install pandas matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating a time series data
dates = pd.date_range(start='2024-01-01', end='2024-12-31')
data = np.random.randn(len(dates))  # Random data
ts = pd.Series(data, index=dates)

# Plotting the time series
plt.figure(figsize=(10, 6))
plt.plot(ts)
plt.title('Random Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()
