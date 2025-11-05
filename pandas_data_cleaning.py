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
# df = df.fillna({"Type2": "None"})

# 3. fix inconsistent values
# changes any value of Grass with GRASS, Fire with FIRE and Water with WATER
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                    "Fire": "FIRE",
#                                    "Water": "WATER"})

# 4. standardize text
# makes all names lowercase
# df["Name"] = df["Name"].str.lower()

# 5. fix data types
# changes legendary data type to boolean rather than 0 or 1
# df["Legendary"] = df["Legendary"].astype(bool)

# 6. remove duplicate values
df = df.drop_duplicates()

print(df.to_string())