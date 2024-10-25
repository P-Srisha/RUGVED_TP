import pandas as pd

df = pd.read_csv(r"/home/srisha/Downloads/matches(2).csv")

print(df['team1'].value_counts()+df['team2'].value_counts())