import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/baby_names/merged.csv')

# gregory = df[df['Name'] == 'Gregory']

# gregory_by_year = gregory.groupby('Year').sum()

# plt.plot(gregory_by_year.index, gregory_by_year['Count'])
# plt.xlabel('Year')
# plt.ylabel('Count')
# plt.title('Gregory by Year')
# plt.show()


# # Create a new column for the first letter of each name
# df['FirstLetter'] = df['Name'].str[0]

# # Group by the first letter and sum the counts
# grouped = df.groupby('FirstLetter').sum()

# # Plot the data
# plt.figure(figsize=(10, 6))
# plt.bar(grouped.index, grouped['Count'])
# plt.xlabel('First Letter of Name')
# plt.ylabel('Count')
# plt.title('Count of Names Grouped by Starting Letter')
# plt.show()


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
plt.title('Count of Names Grouped by Starting Letter Over the Years')
plt.show()