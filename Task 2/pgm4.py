import pandas as pd

df = pd.read_csv(r"/home/srisha/Downloads/matches(2).csv")

print("Max winner = ",df['toss_winner'].value_counts().idxmax())
print("Min winner = ",df['toss_winner'].value_counts().idxmin())