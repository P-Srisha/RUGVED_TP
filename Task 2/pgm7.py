import pandas as pd

df = pd.read_csv(r"/home/srisha/Downloads/matches(2).csv")

print(df.loc[df['result']=='tie'][['team1','team2','result']])