# aggregate functions = reduces a set of values into a single summary value
#                       used to summarize and analyze data
#                       often used with the groupby() function

import pandas as pd

df = pd.read_csv("data.csv")

# THESE AGGREGATE FUNCTIONS APPLY TO WHOLE DATAFRAMES
# tells pandas to find the mean of any columns that are numeric
print(df.mean(numeric_only=True))
# tells pandas to find the sum of any columns that are numeric
print(df.sum(numeric_only=True))
# tells pandas to find the minimum value from all numeric columns
print(df.min(numeric_only=True))
# tells pandas to find the maximum value from all numeric columns
print(df.max(numeric_only=True))
# tells pandas to count the number of numeric values from each column
print(df.count(numeric_only=True))

# SINGLE COLUMN
# tells pandas to find the mean of the height column only
print(df["Height"].mean())
# tells pandas to find the sum of the height column only
print(df["Height"].sum())
# tells pandas to find the minimum value from the height column only
print(df["Height"].min())
# tells pandas to find the maximum value from the height column only
print(df["Height"].max())
# tells pandas to count the number of values from the height column only
print(df["Height"].count())

# GROUPBY FUNCTION
# groups by Type1
group = df.groupby("Type1")

print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())