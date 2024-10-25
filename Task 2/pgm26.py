import pandas as pd

df = pd.read_csv(r"/home/srisha/Downloads/matches(2).csv")

print(df['toss_decision'].value_counts().groupby('toss_winner'))