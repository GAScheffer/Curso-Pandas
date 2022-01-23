"""
FAZENDO COLETA USANDO FLTROS BOOLEANOS
"""


import pandas as pd
import numpy as np

datas = pd.date_range('20180101', periods=20, freq='D')

df = pd.DataFrame(np.random.randn(20, 5), index=datas, columns=list("ABCDE"))

print(df.index)

print(f'\nFILTRANDO O DF USANDO A COLUNA A COMO REFERÊNCIA, FILTRANDO')
print(df[df.A > 0])
