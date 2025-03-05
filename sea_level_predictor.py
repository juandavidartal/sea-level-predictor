import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit

    # Calculate first line of best fit (entire dataset)
    result_full = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_full_extended = pd.Series(range(1880, 2051))
    sea_levels_full = result_full.slope * years_full_extended + result_full.intercept
    
    plt.plot(years_full_extended, sea_levels_full, label="Best Fit Line 1")

    # Calculate second line of best fit (data from 2000 onwards)
    recent_df = df.loc[df["Year"] >= 2000]
    
    result_recent = linregress(recent_df["Year"], recent_df["CSIRO Adjusted Sea Level"])
    years_recent_extended = pd.Series(range(2000, 2051))
    sea_levels_recent = result_recent.slope * years_recent_extended + result_recent.intercept
    
    plt.plot(years_recent_extended, sea_levels_recent, label="Best Fit Line 2")

    # Add labels and title

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()