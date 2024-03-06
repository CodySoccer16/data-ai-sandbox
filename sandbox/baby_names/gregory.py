import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/baby_names/merged.csv')

gregory = df[df['Name'] == 'Cody']

gregory_by_year = gregory.groupby('Year').sum()

plt.plot(gregory_by_year.index, gregory_by_year['Count'])
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Cody by Year')
plt.show()