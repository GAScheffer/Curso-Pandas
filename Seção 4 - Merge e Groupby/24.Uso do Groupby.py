import pandas as pd
import numpy as np

"""
Se o objetivo for a partir de uma coleta de dados fazer a estatistica descritiva por grupos, 
o uso do groupby auxilia nisto.

"""
df = pd.DataFrame({'A': ['verdadeiro', 'falso', 'verdadeiro', 'falso',
                         'verdadeiro', 'falso', 'verdadeiro', 'falso'],
                   'B': ['um', 'um', 'dois', 'três', 'dois', 'dois', 'um', 'três'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})

print(df)

#fazendo agrupamento pela coluna A e fazer uma soma entre ela msm
print(df.groupby(['A']).sum())
"""
Foi filtrado pela soma dos valores falso e verdadeiro na coluna A
RESULTADO:
A                             
falso      -0.684171 -0.529708
verdadeiro  0.917034  3.410506"""

print(f'\nSOMA ENTRE A E B:')
print(df.groupby(['A', 'B']).sum())
