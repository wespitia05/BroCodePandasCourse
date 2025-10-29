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
# prints our datafram
print(df)