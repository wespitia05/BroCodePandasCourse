# data cleaning = the process of fixing/removing:
#                 incomplete, incorrect or irrelevant data
#                 ~75% of work dont with pandas is data cleaning

import pandas as pd

df = pd.read_csv("data.csv")

# 1. drop irrelevant columns
df = df.drop(columns=["Legendary"])

print(df)