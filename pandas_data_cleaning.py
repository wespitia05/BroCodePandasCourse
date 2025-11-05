# data cleaning = the process of fixing/removing:
#                 incomplete, incorrect or irrelevant data
#                 ~75% of work dont with pandas is data cleaning

import pandas as pd

df = pd.read_csv("data.csv")

# 1. drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"])

# 2. handle missing data, removes any rows with Nan (no data available)
# df = df.dropna(subset=["Type2"])
# fills any not available value with "None"
df = df.fillna({"Type2": "None"})

print(df.to_string())