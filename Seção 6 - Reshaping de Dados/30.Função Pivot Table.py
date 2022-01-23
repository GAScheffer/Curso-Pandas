"""
DIFERENÇA É QUE PIVOT NÃO PODE USAR DE REFERENCIA O INDEX COM DADOS REPETIDOS,
PIVOT TABLE PODE USAR DADOS REPETIDOS, podendo fazer alguns tipos de operações matemáticas.

"""

import pandas as pd

carros = [7, 4, 3, 2, 8]

dias = pd.date_range('20190101', '20190101', periods=5)

vendedor = ['George', 'Vagner', 'Pedro', 'Vagner', 'George']

df = pd.DataFrame({'Vendas': carros, 'Data': dias, 'Vendedor': vendedor})
print(f'PRINT DO DATAFRAME COM OS DADOS QUE VÃO GERAR A TABELA:')
print(df)

"""
print(f'\nPRINT DO PIVO, QUE DEVE CAUSAR ERRO PQ TEM INDEX REPETIDOS:')
pivo = pd.pivot(df, index='Data', columns='Vendedor', values='Vendas')
# print(pivo)
# RESULTADO:     raise ValueError("Index contains duplicate entries, cannot reshape")
             # ValueError: Index contains duplicate entries, cannot reshape
"""

pivo = pd.pivot_table(df, index='Data', columns='Vendedor', values='Vendas', aggfunc='sum')
print(f'\n PIVOT_TABLE:')
print(pivo)
