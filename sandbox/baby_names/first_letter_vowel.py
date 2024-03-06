import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/baby_names/merged.csv')

# Create a new column for the first letter of each name
df['FirstLetter'] = df['Name'].str[0]

filtered = df[df['FirstLetter'].isin(['A', 'E', 'I', 'O', 'U'])]

# Group by the first letter and year, then sum the counts
grouped = filtered.groupby(['Year', 'FirstLetter']).sum().reset_index()

# Pivot the data so that each column represents a letter and each row represents a year
pivot_df = grouped.pivot(index='Year', columns='FirstLetter', values='Count').fillna(0)

# Plot the data
pivot_df.plot(kind='line', legend=True)  # Set legend to False for a cleaner plot
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Count of Names Grouped by Starting Vowel Over the Years')
plt.show()