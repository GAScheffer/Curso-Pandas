"""
é usada para manipular tabelas, dataframes, etc... Essenscial em tabelas comlexas e grandes,
tornando eles mais estruturados.

"""

import pandas as pd
import numpy as np

dias = pd.date_range(start='20220101', periods=12)
print(dias)

Pessoa = ['George', 'Victor', 'Lucas']

sorteio = np.random.choice(Pessoa)

print(sorteio)

Nome1 = []
Nome2 = []
Gasto = []
for i in range(12):
    Nome1.append(sorteio)
    Nome2.append(np.random.choice(Pessoa))
    Gasto.append(np.round(np.random.rand()*100, 2))

print(Nome1)
print(Nome2)
print(Gasto)

# GERANDO TABELA POR DATAFRAME USANDO OS DADOS ACIMA:
df = pd.DataFrame({'Dia': dias, 'Nome': Nome2, 'Gasto': Gasto})

print(f'\nTABELA GERADA USANDO DATAFRAME:')
print(df)

# UTILIZANDO A FUNÇÃO PIVOT

dfp = df.pivot(index='Dia', columns='Nome', values='Gasto')
print(f'\nPRINT DO DFP, USANDO A TABELA CRIADA REMOLDADO PARA PIVOT:')
print(dfp)
