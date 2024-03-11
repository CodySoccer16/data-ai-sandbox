import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/PremierLeague/squad_pl_stats3.csv')
df.dropna(inplace=True)
#print(df)

newdf = df[["Squad", "Wins", "Win%", "Poss"]]
print(list(newdf['Squad']))

x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
y = np.array(list(df['Win%']))
my_xticks = list(newdf['Squad'])
plt.xticks = (x, my_xticks)
plt.plot(x, y)
plt.xlabel('Team')
plt.ylabel('Win Percentage')
plt.title('Win Percentage of Premier League Teams')
plt.show()
"""
x = np.array([0,1,2,3])
y = np.array([20,21,22,23])
my_xticks = ['John','Arnold','Mavis','Matt']
plt.xticks(x, my_xticks)
plt.plot(x, y)
plt.show()
"""

#Working without label
"""
x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
y = np.array(df['Win%'])
my_xticks = newdf['Squad']
plt.xticks = (x, my_xticks)
plt.plot(x, y)
plt.xlabel('Team')
plt.ylabel('Win Percentage')
plt.title('Win Percentage of Premier League Teams')
plt.show()
"""