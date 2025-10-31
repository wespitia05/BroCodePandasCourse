import pandas as pd

# sets the index for each row to be the pokemon's name
df = pd.read_csv("data.csv", index_col="Name")

# SELECTION BY COLUMN
# print(df["Name"])
# print(df["Height"])
# print(df["Weight"])
# prints the selected columns
# print(df[["Name", "Height", "Weight"]])

# SELECTION BY ROW
# print(df.loc["Pikachu"])
# print(df.loc["Charizard"])
# prints only those two columns
# print(df.loc["Mewtwo"], ["Height", "Weight"])
# prints information from charizard to blastoise
# print(df["Charizard":"Blastoise"])
# prints information from index 0 to index 11
# print(df.iloc[0:11:2, 0:3]) # last :2 means every second row, # 0:3 means only first 3 columns

pokemon = input("enter a pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")