# IPL Cricket Analytics
# By Vijaya Lakshmi

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('IPL IMB381IPL2013.csv')

print("IPL Dataset Loaded Successfully!")
print("Total Players:", len(df))

# Chart 1 - Top 10 Run Scorers
plt.figure(figsize=(12,6))
top_batsmen = df.groupby('PLAYER NAME')['T-RUNS'].sum().sort_values(ascending=False).head(10)
top_batsmen.plot(kind='bar', color='orange')
plt.title('Top 10 Run Scorers in IPL')
plt.xlabel('Player')
plt.ylabel('Total Runs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_batsmen.png')
plt.show()
print("Chart 1 saved!")

# Chart 2 - Top 10 Wicket Takers
plt.figure(figsize=(12,6))
top_bowlers = df.groupby('PLAYER NAME')['WKTS'].sum().sort_values(ascending=False).head(10)
top_bowlers.plot(kind='bar', color='green')
plt.title('Top 10 Wicket Takers in IPL')
plt.xlabel('Player')
plt.ylabel('Total Wickets')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_bowlers.png')
plt.show()
print("Chart 2 saved!")

# Chart 3 - Top 10 Most Expensive Players
plt.figure(figsize=(12,6))
top_expensive = df.groupby('PLAYER NAME')['SOLD PRICE'].max().sort_values(ascending=False).head(10)
top_expensive.plot(kind='bar', color='blue')
plt.title('Top 10 Most Expensive IPL Players')
plt.xlabel('Player')
plt.ylabel('Sold Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_expensive.png')
plt.show()
print("Chart 3 saved!")

print("\nIPL Analysis Complete!")