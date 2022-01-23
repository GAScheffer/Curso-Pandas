import pandas as pd
import numpy as np

datas = pd.date_range('20200101', periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=["A", "B", "C", "D"])

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'Python',
                    'G': [2, 2, 4, 4],
                    'H': [np.nan, 2, 4, np.nan]})


print(df2)
# DTYPES SERVE PARA VER O TIPO DE DADOS

print(df2.dtypes)
# A           float64 - como padrão, nº flutuantes vem como float64, tendo maior capacidade de armazenamento
# B    datetime64[ns]
# C           float32
# D             int32
# E          category
# F            object
# dtype: object

""" SUMUARIO USANDO describe() """
"""describe """
print(f'\nFAZENDO RESUMO DAS COLUNAS: (print(df2.describe()))')
print(df2)
print(df2.describe())

print(f'\nAdicionando valor em uma coluna. Neste caso, colocando valor 1, nas linhas 0 e 1 na nova coluna criada:')
print(f'\nTABELA DF SEM ALTERAÇÃO: \n{df}')
df1 = df.reindex(index=datas[0:4], columns=list(df.columns) + ['E'])

dfE = df1.loc[datas[0]:datas[1], 'E'] = 1    # .loc é a localização, antes da virgula é linhas, depois é coluna.
print(f'\nTABELA DF COM ALTERAÇÃO: \n{df1}')
