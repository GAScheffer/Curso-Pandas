"""
Estrutuda de Dados tipo Dataframe
 - Datafreme é um local para guardar dados
 - Auxilia no desenvolvimento de analise de dados.
 - Para Python, dataframe é um OBJETO
    - Estrutura primária de funcionamento do Dataframe

"""

import pandas as pd
import numpy as np

#########################################################################
###################              AULA 12              ###################
#########################################################################

# Série são formas de estruturar dados, Panda oferece uma maneira simples de gerenciar as séries

#########################################################################
###################              AULA 13              ###################
#########################################################################

# series são formas de estruturar dados, panda oferece uma forma menos complicado de estrururar

series = pd.Series([7, 4, 2, np.nan, 6, 9])    # np.nan é a representação de um numero não especificado

# print(type(series))    # Resultado: <class 'pandas.core.series.Series'>
"""
print(series)
# Resultado 
0    7.0
1    4.0
2    2.0
3    NaN
4    6.0
5    9.0
dtype: float64
"""

# OBTENDO DATAS
datas = pd.date_range('20180125', periods=60, freq='d')    # data = aaaammdd
# print(datas)

#########################################################################
###################              AULA 14              ###################
#########################################################################
df = pd.DataFrame(np.random.randn(60, 5), index=datas, columns=list("ABCDE"))

# df4 = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=['Sorteio 1', 'Sorteio 2', 'Sorteio 3', 'Sorteio 4'])
# print(f'\n PRINT DO DF4:\n')
# print(df4)
#
# df2 = pd.DataFrame({"A": 7,
#                     "B": pd.Timestamp(20190101),
#                     "C": pd.Series(1, index=list(range(4)), dtype='float32'),
#                     "D": np.array([3] * 4, dtype='int32'),
#                     "E": pd.Categorical(["test", "train", "test", "train"]),
#                     "F": 'Gustavo'})
# print(f'\n PRINT DO DF2:\n')
# print(df2)

#########################################################################
###################              AULA 15              ###################
#########################################################################

# ADICIONAR COLUNAS NOVAS
"""
Usando o comando abaixo, já listado no topo:
# datas = pd.date_range('20180125', periods=60, freq='d') 
# df.shape fornece a quantidade de linhas e columas
    (60, 5)
1) Pegar o DataFrama, abre e fecha conhcetes e adicionar uma sequência:
    df['F'] = 1 
    - assim, ele vai adicionar uma coluna que será chamada de F e terá valor 1 nas linhas
    - pode ser adicionado elemenos, é necessário ter a mesma quantidade. 
        df['G'] = [10, 6, 7, 5] # assim vai dar erro, pq não ter o mesmo valor
    
"""
df['F'] = 'mais uma coluna'
df['G'] = df['A'] + df['B']
#
# print(f'\n PRINT DO DF2 SOMANDO A COLUNA "A" COM A "B":\n')

print(df)


#########################################################################
###################              AULA 16              ###################
#########################################################################
"""
COMANDOS ESSÊNCIAIS

# Visualisar Dados:
"""
"""
# df.head ele vai mostrar as linhas de topo para baixo:
print('DF.HEAD(5)')
print(df.head(5))


# df.tail(2) vai mostrar as linhas de baixo para top
print('DF,TAIL(5)')
print(df.tail(5))
"""
# Observar somente os index de referencia do dataframe
# print(df.index)

# # MONSTRANDO SÓ AS COLUNAS
# print(df.columns)
#
# # mostrar somente os arrays na fomra de matriz, bom para trabalhar com métodos matemáticos
# df.to_numpy()
#
# # df.T inverto entre as colunas e linhas
# print(df.T)




