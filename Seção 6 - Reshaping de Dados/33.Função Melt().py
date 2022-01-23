"""

"""

import pandas as pd

data = {
    "localizacao": ['CidadeA', 'CidadeB'], "Temperatura": ["Prevista", "Atual"],
    "Set-2019": [30, 32],
    "Out-2019": [45, 43],
    "Nov-2019": [24, 22]}

# print(data)

df = pd.DataFrame(data, columns=['localizacao', 'Temperatura', 'Set-2019', 'Out-2019', 'Nov-2019'])
print(f'PRINT DO DF:')
print(df)

# RESULTADO
# PRINT DO DF:
#   localizacao Temperatura  Set-2019  Out-2019  Nov-2019
# 0     CidadeA    Prevista        30        45        24
# 1     CidadeB       Atual        32        43        22

df2 = pd.melt(df, id_vars=["localizacao", "Temperatura"], var_name="Data", value_name="GRAUS")
print(f'\nPRINT DF2')
print(df2)
# RESULTADO
# PRINT DF2
#   localizacao Temperatura      Data  GRAUS
# 0     CidadeA    Prevista  Set-2019     30
# 1     CidadeB       Atual  Set-2019     32
# 2     CidadeA    Prevista  Out-2019     45
# 3     CidadeB       Atual  Out-2019     43
# 4     CidadeA    Prevista  Nov-2019     24
# 5     CidadeB       Atual  Nov-2019     22
