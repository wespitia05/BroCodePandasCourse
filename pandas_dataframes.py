# dataframe = a tabular data structure with rows AND columns (2 dimensional)
#             similar to an excel spreadsheet

import pandas as pd

# create our dictionary
data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
    }
# calls pandas to convert into a dataframe
df = pd.DataFrame(data)
# prints our datafram
print(df)