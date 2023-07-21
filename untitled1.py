import pandas as pd

df = pd.read_csv('D:/Coding/python/datasets/real_interest_rate_by_country.csv')

df.sort_values(["value"],axis=0,ascending=[False],inplace=True)

print("\nAfter sorting:")
print(df)

