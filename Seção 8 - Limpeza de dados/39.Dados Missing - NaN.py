import pandas as pd
import numpy as np

datas = pd.date_range('20190101', periods = 60, freq='D')

df = pd.DataFrame(np.random.randn(60,5), index = datas, columns = list("ABCDE"))

df.head(3)
print(f'PRINT DO DF')
print(df)

df['F'] = df.A[df.A > 0]
print(f'\nPRINT DO DF, filtrando os valores na coluna A')
print(df.head(10))

df2 = df.copy()
df2 = df.dropna()    # drop significa remover.
print(f'\nPRINT DO DF, removendo os valores NaN')
print(df2.head(5))

# ao invez de remover, vamos adicionar a média da coluna A

df3 = df.fillna(np.mean(df.A))
print(f'\nPRINT DO DF, substituindo os valores NaN por média aritimética usando numpy')
print(df.head(10))
print(df3.head(10))