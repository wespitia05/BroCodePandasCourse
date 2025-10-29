# dataframe = a tabular data structure with rows AND columns (2 dimensional)
#             similar to an excel spreadsheet

import pandas as pd

# create our dictionary
data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
    }
# calls pandas to convert into a dataframe and change label for our indexes
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])
# prints our dataframe
print(df)

# using loc to locate our data value by label, prints it and the datatype
print("LOC PROPERTY")
print(df.loc["Employee 1"])
print(df.loc["Employee 2"])
print(df.loc["Employee 3"])

# using iloc to locate our data value by index, prints it and the datatype
print("ILOC PROPERTY")
print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[2])