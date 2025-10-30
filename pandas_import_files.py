# csv = comma separated values
# json = javascript object notation

import pandas as pd

df = pd.read_csv("data.csv")

# prints first 5 and last 5 (if csv file is too big)
print(df)
# prints entire csv
print(df.to_string())