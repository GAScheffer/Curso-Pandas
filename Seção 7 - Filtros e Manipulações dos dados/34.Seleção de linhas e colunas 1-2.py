"""
Selecionar parte dos dados, slice, coleta de colunas e linhas do dataframe

"""

import pandas as pd
import numpy as np

datas = pd.date_range('20180101', periods=600, freq='D')

df = pd.DataFrame(np.random.randn(600,5), index = datas, columns= list("ABCDE"))

# df.head(2) define aprsentar apenas duas linhas no topo
print('PRINT DA DF COMPLETO.')
print(df)

print(f'\nDEFININDO QUE SEJA MOSTRADO APENAS AS DUAS PRIMEIRAS COLUNAS COM DF.HEAD(2):')
print(df.head(2))

print(f'\nDEFININDO QUE SEJA MOSTRADO APENAS AS CINCO PRIMEIRAS COLUNAS COM DF.HEAD(5) E'
      f'\nQUE ESPECIFIQUE POR COLUNA df["D"]:')
print(df['D'].head(2))

# OBTER LINHAS EM ESPECÍFICOS - EX - DA LINHA Nº 2 ATÉ LINHA x
print(F'\nOBTER LINHAS EM ESPECÍFICOS DF[index_Inicial:index_FINAL]: '
      F'\n(EX: df.[1:4] - vai mostrar apenas três linhas, começando da segunda coluna.')
print(df[1:4]) # do indice 1 até o 4

print(f'\nESPECIFICANDO POR INTERVALOS DE DATAS ([periodo_incial : periodo_final, ["Colunas1(A)", "Colunas2(E)"])')
print(df.loc['20180301': '20180401', ['A', 'E']])

f = df.loc['20180301': '20180901', ['A', 'E']]
print(f'\nPRINT DE F, onde F contém Xs linhas:')
print(len(f))

# OBTENDO TODOS OS VALORES DE UMA LINHA.
print(f'\nOBTENDO TODOS OS VALORES DE UMA LINHA.'
      f'\n df.loc[1] [1] é qual linha deseja pegar os valores, considerando Zero como linha 1')
print(df.head(5))
print(df.iloc[1])    # [1] é qual linha deseja pegar os valores, considerando Zero como linha 1

print(f'\nFAZENDO FATIAÇÕES, DE UM GRUPO DE LINHAS E COLUNAS. df.iloc["linhas","colunas"]:')
print(df.iloc[0:5, 0:5])

print(f'\nFAZENDO FATIAÇÃO COM df.iloc[[1,3,5],[0,3]] ESPECIFICA QUAIS LINHAS E COLUNAS QUER, USANDO VIRGULA:')
print(df.iloc[[1,3,5],[0,3]])


# 36. Filtros booleanos
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
