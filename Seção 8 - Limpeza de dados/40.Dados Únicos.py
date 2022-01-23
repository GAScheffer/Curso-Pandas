"""
IDENTIFICANDO VALORES REPETIDOS

nunuque() conta quantas vezes um valor determinado se repete, podendo verificar em axis ou columns (linha ou coluna)
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'Python',
                    'G': [2, 2, 4, 4],
                    'H': [np.nan, 2, 4, np.nan]})

print(df)
"""
df2 = df.nunique(axis=1, dropna=False) # axis 0 para linha e 1 para coluna
print(f'\nUSANDO NUNIQUE() PARA FILTRAR:')
print(df2)
"""
############################################################
############### AULA 41.REMOVENDO DUPLICATAS ###############
############################################################

df3 = df.drop_duplicates(subset='E', keep='last')
print(f'\nREMOVENDO DUPLICATAS:')
print(df3)
