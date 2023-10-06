import pandas as pd
import numpy as np

icantfindname = np.random.randint(0, 50, 6)
icantfindname2 = pd.Series(icantfindname,index=["a","b","c","d","e","f"])
print(icantfindname2)


abc = np.random.randint(0,25,(4,3))
df = pd.DataFrame(abc, columns = ["col1", "col2", "col3"])
print(df)


a = np.random.randint(10,size=5)
b = np.random.randint(10,size=5)
c = np.random.randint(10,size=5)
dict = {
    "col1":a,
    "col2":b,
    "col3":c,
}
df = pd.DataFrame(dict)
df

import seaborn as sns
import matplotlib as plt
