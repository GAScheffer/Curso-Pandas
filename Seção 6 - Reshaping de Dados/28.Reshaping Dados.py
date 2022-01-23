"""
Reshape é a reformulação dos dados para aprimorar na engenharia de dados

"""

import pandas as pd
import numpy as np

datas = pd.date_range('20200101', periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=['Var A', 'Var B','Var C', 'Var D'])

print(df)


# INVERTENDO COLUNAS E LINHAS (usa o comando ".T")
dft = df.T
print(f'\ndft')    # ou print(df.T)

# COMPARAR OS FORMATOS COM SHAPE
print(f'\nCOMPARAR FORMATOS COM SHAPE:')
print(df.shape)

# EXTRAINDO OS DADOS
print(f'\nEXTRAINDO OS DADOS:')
valor = dft.values
print(valor)

# QUAL O TAMANHO?
print(f'\nQual o tamanho?')
tamanho = np.size(dft.values)
print(tamanho)

# RESHAPE
print(f'\nRESHAPE')
print(valor.reshape(2, 12))
print(f'\n----------------')
print(valor.reshape(4, 6))
