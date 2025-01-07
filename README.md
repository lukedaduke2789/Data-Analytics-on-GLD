# Data-Analytics-on-GLD
Gold Price Analysis with yfinance
Overview

This project explores the historical price data of SPDR Gold Shares (GLD) using Python. I analyzed trends, volatility, and statistical relationships to uncover key insights into gold price behavior over time. The data spans from January 1, 2020, to January 1, 2023.
Contents
1. Dataset

Historical GLD price data, fetched using the yfinance library, includes:

    Date
    Open, High, Low, Close prices
    Volume

2. Python Script

The gld_analysis.py script performs:

    Data ingestion
    Cleaning and manipulation
    Visualizations
    Statistical analysis

3. Visualizations

    GLD Close Price Over Time (line plot)
    Distribution of GLD Daily Returns (histogram + KDE)

Steps Taken
Data Ingestion

I used yfinance to download GLD data and saved it as gld_data.csv for reproducibility.
Data Cleaning

    Checked for and removed missing values.
    Reformatted columns for consistency.

Data Manipulation

    Calculated Daily Returns to analyze day-to-day changes in closing prices.

Visualizations

    Close Price Trend: Highlighted the long-term price movements.
    Daily Returns Distribution: Showed the volatility and return frequency.

Statistical Analysis

    Descriptive stats: Mean, median, standard deviation, etc.
    Correlation: Explored the relationship between Daily Returns and Volume.

Key Insights

    Gold prices surged in 2020, followed by fluctuations in subsequent years.
    Daily returns exhibited moderate volatility with occasional spikes.
    Weak correlation between daily returns and trading volume.

How to Run

    Clone the repository:

git clone https://github.com/yourusername/your-repo-name.git

Install required libraries:

pip install pandas matplotlib seaborn yfinance

Run the script:

    python gld_analysis.py

Future Work

    Expand to analyze other financial assets.
    Apply predictive models for price forecasting.
