# aggregate functions = reduces a set of values into a single summary value
#                       used to summarize and analyze data
#                       often used with the groupby() function

import pandas as pd

df = pd.read_csv("data.csv")

# tells pandas to find the mean of any columns that are numeric
print(df.mean(numeric_only=True))
# tells pandas to find the sum of any columns that are numeric
print(df.sum(numeric_only=True))
# tells pandas to find the minimum value from all numeric columns
print(df.min(numeric_only=True))