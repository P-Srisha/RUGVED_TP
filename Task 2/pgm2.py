import pandas as pd

df = pd.read_csv(r"/home/srisha/Downloads/matches(2).csv")
print("Max = ",df['city'].value_counts().idxmax())
print("Min = ",df['city'].value_counts().idxmin())