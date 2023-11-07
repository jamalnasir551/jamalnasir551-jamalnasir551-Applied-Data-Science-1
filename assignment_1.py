#IMPORTING THE REQUIRED LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#IMPORTING THE DATASET
athleteData = pd.read_csv("athlete_events_with_region.csv")


#1- VISUALIZATION USING LINEPLOT
def plot_medal_count_by_region_over_years(athleteData, regions):
    """
    Plot the number of medals by region over the years.

    Args:
        athleteData (pd.DataFrame): The Olympic athlete dataset.
        regions (list of str): List of region names to include in the plot.

    Returns:
        None (displays the line plot).
    """
    # Filter the data to include only rows with medalists (Gold, Silver, Bronze)
    medalists = athleteData[athleteData['Medal'].isin(['Gold', 'Silver', 'Bronze'])]

    # Group the data by region and year, and count the occurrences of each medal type
    medal_counts_by_region = medalists.groupby(['Year', 'region', 'Medal'])['ID'].count().unstack().fillna(0)

    # Calculate the total number of medals (Gold, Silver, Bronze) for each region in each year
    medal_counts_by_region['Total Medals'] = medal_counts_by_region.sum(axis=1)

    # Create a line plot for each region in the regions list
    plt.figure(figsize=(18, 6))

    for region in regions:
        if region in medal_counts_by_region.index.get_level_values('region'):
            region_medals = medal_counts_by_region[medal_counts_by_region.index.get_level_values('region') == region]
            plt.plot(region_medals.index.get_level_values('Year'), region_medals['Total Medals'], label=region)

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Total Medals')
    plt.title('Medal Count by Region Over the Years')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()


#2- VISUALIZATION USING STACKED BAR
def plot_medal_distribution_by_country_region(athleteData, top_n=10):
    """
    Plot the distribution of gold, silver, and bronze medals by country region.

    Args:
        athleteData (pd.DataFrame): The Olympic athlete dataset with region information.
        top_n (int): The number of top country regions to include in the plot.

    Returns:
        None (displays the stacked bar plot).
    """
    # Filter the data to include only rows with medalists (gold, silver, bronze)
    medalists = athleteData[athleteData['Medal'].isin(['Gold', 'Silver', 'Bronze'])]

    # Group the data by country region and medal type, and count the occurrences
    medal_counts = medalists.groupby(['region', 'Medal']).size().unstack().fillna(0)

    # Select the top N country regions with the most total medals
    top_regions = medal_counts.sum(axis=1).sort_values(ascending=False).head(top_n).index

    # Filter the data to include only the top country regions
    top_medal_counts = medal_counts.loc[top_regions]

    # Create a stacked bar plot with a color theme
    ax = top_medal_counts.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='viridis')

    # Set labels and title
    ax.set_xlabel('Country Region')
    ax.set_ylabel('Number of Medals')
    ax.set_title('Medal Distribution by Country Region')

    # Customize legend
    ax.legend(title='Medal Type')

    # Show the plot
    plt.tight_layout()  # Ensures the labels are not cut off
    plt.show()



#3- VISUALIZATION USING HISTOGRAM
def plot_age_distribution(athleteData, bins=20):
    """
    Plot the age distribution of Olympic athletes.

    Args:
        athleteData (pd.DataFrame): The Olympic athlete dataset with age information.
        bins (int): Number of bins to use in the histogram.

    Returns:
        None (displays the age distribution histogram).
    """
    # Filter out missing or invalid age values
    valid_ages = athleteData['Age'].dropna()

    # Create a histogram of athlete ages
    plt.figure(figsize=(10, 6))
    plt.hist(valid_ages, bins=bins, edgecolor='black', alpha=0.7, color='orange')
    
    # Set labels and title
    plt.xlabel('Age')
    plt.ylabel('Number of Athletes')
    plt.title('Age Distribution of Olympic Athletes')

    # Show the plot
    plt.show()


#CALLING EACH FUNCTION

# List of region names to include in the plot
regions_to_plot = ['Netherlands', 'Russia', 'Germany']

# Call the function to plot medal count by region over years
plot_medal_count_by_region_over_years(athleteData, regions_to_plot)
# Call the function to plot the medal distribution by country region
plot_medal_distribution_by_country_region(athleteData, top_n=10)
# Call the function to plot the age distribution
plot_age_distribution(athleteData)



