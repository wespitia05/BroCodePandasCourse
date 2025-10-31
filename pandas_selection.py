import pandas as pd

df = pd.read_csv("data.csv")

# SELECTION BY COLUMN
# print(df["Name"])
# print(df["Height"])
# print(df["Weight"])
# prints the selected columns
print(df[["Name", "Height", "Weight"]])