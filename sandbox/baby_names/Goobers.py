import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/baby_names/merged.csv')

# Create a new column for the first letter of each name


filtered = df[df['Name'].isin(['Cody', 'Drew', 'Colin', 'Samuel', 'Nicholas', 'Kolby', 'Collin', 'William', 'Jaxon', 'Blaise'])]

# Group by the first letter and year, then sum the counts
grouped = filtered.groupby(['Year', 'Name']).sum().reset_index()

# Pivot the data so that each column represents a letter and each row represents a year
pivot_df = grouped.pivot(index='Year', columns='Name', values='Count').fillna(0)

# Plot the data
pivot_df.plot(kind='line', legend=True)  # Set legend to False for a cleaner plot
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Popularity of Goobers Over the Years')
plt.show()