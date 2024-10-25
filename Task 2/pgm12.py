import pandas as pd

df = pd.read_csv(r"/home/srisha/Downloads/matches(2).csv")

print("Most runs venue = ", df.loc[df['win_by_runs'].idxmax()]['city'])
print("Least runs venue = ", df.loc[df['win_by_runs'].idxmin()]['city'])