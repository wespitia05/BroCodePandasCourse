# series = a pandas 1 dimensional labeled array that can hold any data type
# think of it like a single column in a spreadsheet (1D)

import pandas as pd

data = [100, 102, 104]

# call series function, takes data and puts it into a single column spreadsheet
series = pd.Series(data)

# when printed, prints numbers with indexes and datatype (64 bit integers)
# 0   100
# 1   102
# 2   104
print(series)