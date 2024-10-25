import pandas as pd

df = pd.read_csv(r"/home/srisha/Downloads/matches(2).csv")

print(df['result'].value_counts())