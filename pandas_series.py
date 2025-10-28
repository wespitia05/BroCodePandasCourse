# series = a pandas 1 dimensional labeled array that can hold any data type
# think of it like a single column in a spreadsheet (1D)

import pandas as pd

data = [100.1, 102.2, 104.3]

# call series function, takes data and puts it into a single column spreadsheet
# you can rename the indexes
series = pd.Series(data, index=["a", "b", "c"])

# when printed, prints numbers with indexes and datatype (64 bit integers, float, object, boolean, etc)
# 0   100
# 1   102
# 2   104
print(series)

# access specific data values at a specified index
# iloc = integer location
# loc  = location by label
print(series.loc["a"])
print(series.loc["b"])
print(series.loc["c"])
print(series.iloc[0])
print(series.iloc[1])
print(series.iloc[2])

# we can also change the data value at a specific index
series.loc["c"] = 200
print(series)