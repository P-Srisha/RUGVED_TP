import pandas as pd

df = pd.read_csv(r"/home/srisha/Downloads/matches(2).csv")

print(df['player_of_match'].value_counts() > 3)