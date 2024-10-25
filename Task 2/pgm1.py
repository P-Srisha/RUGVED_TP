import pandas as pd

df = pd.read_csv(r"/home/srisha/Downloads/matches(2).csv")
newdf = df[df['season']==2008]

result = len(newdf)
print(result)