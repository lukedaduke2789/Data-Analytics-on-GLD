# Project Title: Gold Price Analysis with yfinance
# Description: Analyze historical data of SPDR Gold Shares (GLD) to uncover trends and insights.
# Dataset: Historical price data fetched using yfinance.
# Author: [Luke Kimball]

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# Step 1: Data Ingestion
print("\n📥 Fetching historical data for GLD...\n")
gld_data = yf.download('GLD', start='2020-01-01', end='2023-01-01')
print("\n✅ Data successfully downloaded!\n")
gld_data.to_csv('gld_data.csv')  # Save to CSV for backup

# Step 2: Data Cleaning
print("🧹 Checking for missing values...\n")
missing_values = gld_data.isnull().sum()
print("Missing values in dataset:\n", missing_values)

print("\n🧼 Dropping missing values if any...\n")
gld_data.dropna(inplace=True)

# Flatten MultiIndex columns (if present)
if isinstance(gld_data.columns, pd.MultiIndex):
    gld_data.columns = gld_data.columns.get_level_values(0)

# Confirm cleaned data
print("\n✅ Data after cleaning:\n", gld_data.head())

# Step 3: Data Manipulation
print("\n🔄 Calculating daily returns...\n")
gld_data['Daily Return'] = gld_data['Close'].pct_change()
print("\n✅ Daily Returns calculated.\n")

# Step 4: Data Visualization
print("🎨 Generating visualizations...\n")

# Visualization 1: Line plot for Close price
plt.figure(figsize=(10, 6))
plt.plot(gld_data['Close'], label='GLD Close Price', color='gold')
plt.title('GLD Close Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.savefig('gld_price_trend.png')
plt.show()

# Visualization 2: Histogram of Daily Returns
plt.figure(figsize=(10, 6))
sns.histplot(gld_data['Daily Return'].dropna(), bins=50, kde=True, color='blue')
plt.title('Distribution of GLD Daily Returns')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('gld_daily_returns_hist.png')
plt.show()

# Visualization 3: Boxplot of Close Prices by Year
gld_data['Year'] = gld_data.index.year
plt.figure(figsize=(10, 6))
sns.boxplot(x='Year', y='Close', data=gld_data, palette='Set3')
plt.title('Yearly Distribution of GLD Close Prices')
plt.xlabel('Year')
plt.ylabel('Close Price (USD)')
plt.grid(True)
plt.savefig('gld_yearly_boxplot.png')
plt.show()

# Step 5: Statistical Analysis
print("\n📊 Performing statistical analysis...\n")
desc_stats = gld_data['Close'].describe()
correlation = gld_data[['Daily Return', 'Volume']].corr()

# Display results
print("📈 Descriptive Statistics for GLD Close Prices:\n", desc_stats)
print("\n🔗 Correlation between Daily Return and Volume:\n", correlation)

print("\n🎉 Analysis complete! Now go impress your friends with your newfound gold knowledge. 🏆")
