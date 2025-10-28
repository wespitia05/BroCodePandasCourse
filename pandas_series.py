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