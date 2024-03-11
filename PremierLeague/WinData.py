import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/PremierLeague/epl_results_2022-23.csv')


clean_df = df[['HomeTeam', 'AwayTeam', 'HomeGoals', 'AwayGoals', 'WinningTeam']]
print(clean_df.head())

TeamWins = clean_df['WinningTeam'].value_counts()
#TeamWins = TeamWins["Man City", "Arsenal", "Man United", "Liverpool", "Newcastle", "Tottenham", "Brighton", "Aston Villa", "Fulham", "Brentford", "Crystal Palace", "Chelsea", "Bournemouth", "West Ham", "Wolves", "Nottingham", "Leicester", "Everton", "Leeds", "Southampton"]

TeamWinPercent = (TeamWins / 38) * 100
print(TeamWins, TeamWinPercent)


"""
TeamWinPercent.plot(kind='bar', legend=True)
plt.xlabel('Team')
plt.ylabel('Win Percentage')
plt.title('Win Percentage of Premier League Teams')
plt.show()
"""