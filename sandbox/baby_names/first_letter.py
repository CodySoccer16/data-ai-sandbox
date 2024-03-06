import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/baby_names/merged.csv')

# Create a new column for the first letter of each name
df['FirstLetter'] = df['Name'].str[0]

# Group by the first letter and sum the counts
grouped = df.groupby('FirstLetter').sum()

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(grouped.index, grouped['Count'])
plt.xlabel('First Letter of Name')
plt.ylabel('Count')
plt.title('Count of Names Grouped by Starting Letter')
plt.show()