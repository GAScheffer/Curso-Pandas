import pandas as pd
import numpy as np

df = pd.DataFrame({'Col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
                   'Col2': [2, 1, 9, 8, 7, 4],
                   'Col3': [0, 1, 9, 4, 2, 3]})

print(df)

""" ORDENDANDO POR ORDEM """

df1 = df.sort_values(by=['Col3'], ascending=False)
print(df1)
