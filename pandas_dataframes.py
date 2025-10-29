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

# adding a new column to our data (has to match same number of values in data)
df["Job"] = ["Frycook", "N/A", "Cashier"]
print(df)

# adding new rows to our data, easiest way is to create new dataframe then concatenate it
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}, 
                        {"Name": "Eugene", "Age": 56, "Job": "Manager"}],
                        index=["Employee 4", "Employee 5"])
# call the concat property, parameters is your dataframe and the new row you want to add
df = pd.concat([df, new_row])
print(df)