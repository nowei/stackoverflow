# import pandas as pd
import pandas as pd
  
# list of strings
lst = [2006, 2007,2008,2009,2010,2012,2014,2016,2017]
  
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df.columns)
print(df)
rows = (df[0] >= 2008) & (df[0] <= 2016)
print(rows)