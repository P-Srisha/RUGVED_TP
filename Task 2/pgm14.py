import pandas as pd

df = pd.read_csv(r"/home/srisha/Downloads/matches(2).csv")

print((df['umpire1'].value_counts()+df['umpire2'].value_counts()+df['umpire3'].value_counts()).idxmax())