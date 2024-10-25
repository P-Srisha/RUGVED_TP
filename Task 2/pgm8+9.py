import pandas as pd

df = pd.read_csv(r"/home/srisha/Downloads/matches(2).csv")

print("Most runs winner = ", df.iloc[df['win_by_runs'].idxmax()]['winner'])
print("Least runs winner = ", df.iloc[df['win_by_rows'].idxmin()]['winner'])