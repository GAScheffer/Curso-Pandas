"""
nerge.Dataframes

Fazer uma conexão entre os cadastros de duas lojas e
estruturar com o uso da função merge que auxilia a interpretar os dados

"""

import pandas as pd

# Cadastro da Loja A

cadastro_a = {'Id': ['AA2930', 'BB4563', 'CC2139', 'DE2521', 'GT3462', 'HH1158'],
              'Nome': ['Victor', 'Amanda', 'Bruno', 'Carlos', 'Ricardo', 'Maria'],
              'Idade': [20, 35, 40, 54, 30, 27],
              'CEP': ['00092-029', '11111-111', '88888-888', '00000-999', '88888-111', '77777-666']
              }

cadastro_a = pd.DataFrame(cadastro_a, columns= ['Id', 'Nome', 'Idade', 'CEP'])
print(f'Cadastro A:')
print(cadastro_a)

# Cadastro da loja b

cadastro_b = {'Id': ['CC9999', 'EF4488', 'DD9999', 'GT3462', 'HH1158'],
              'Nome': ['Marcos', 'Patricia', 'Ericka', 'Ricardo', 'Maria'],
              'Idade': [19, 30, 22, 30, 27],
              'CEP': ['90092-029', '55511-114', '11111-888', '88888-111', '75557-356']
              }

cadastro_b = pd.DataFrame(cadastro_b, columns=['Id', 'Nome', 'Idade', 'CEP'])
print(f'\nCadastro B:')
print(cadastro_b)

# Registro de compras de todas unidades
compras = {'Id': ['AA2930', 'EF4488', 'CC2139', 'EF4488', 'CC9999', 'AA2930', 'HH1158', 'HH1158'],
           'Data': ['2019-01-01', '2019-01-30', '2019-01-30', '2019-02-01', '2019-02-20', '2019-03-15', '2019-04-01',
                    '2019-04-10'],
           'Valor': [200, 100, 40, 150, 300, 25, 50, 500]
           }

compras = pd.DataFrame(compras, columns=['Id', 'Data', 'Valor'])

print(f'\nCompras:')
print(compras)

"""
# Sintaxe Básica da função: 
 pd.merge(tabela_da_esquerda, tabela_da_direita, on="coluna_coincidente", how="left|right|inner|outer)

"""

# INNER JOIN - é a intersecção entre dois conjuntos.
inner = pd.merge(cadastro_a, cadastro_b, on=["Id"], how="inner")
print(f'\nPRINT DO INNER:')
print(inner)

inner = pd.merge(cadastro_a, cadastro_b[['Id', 'Idade', 'CEP']], on=["Id"], how="inner")
print(f'\nPRINT DO INNER COM FILTRO.\nAQUI NO CASO, REMOVEU A COLUNA COM VALOR REPETIDO:')
print(inner)

# FULL JOIN

lojas = pd.concat([cadastro_a, cadastro_b], ignore_index=True)

# removendo duplicadas:
# joinfull.drop_duplicates(subset="id")

print(f'\nPRINT DO JOIN FULL:')
print(lojas)

print(f'\nPRINT DO JOIN FULL REMOVENDO DUPLICADAS:')
print(lojas.drop_duplicates(subset="Id"))


# LEFT/RIGHT JOIN
# Considera os valores repetidos entre tabela A e B e desconsidera os não repetidos na tabela B e descarta
left = pd.merge(cadastro_a, compras, how="left", on=["Id"])

print(f'\nLeftJoin:')
print(left)

print(f'\nLeftJoin somando os valores:')
print(left.groupby(['Id', 'Nome', 'Idade', 'CEP'])['Valor'].sum())


# OUTER - Ele junta todos os dados e atribuiu a um único dataframe

outer = pd.merge(cadastro_a, cadastro_b, how="outer", on=["Id"], indicator=True)
print(f'\nTABELA USANDO OUTER:')
print(outer)
