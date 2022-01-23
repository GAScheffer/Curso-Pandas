"""

"""

import pandas as pd

df = pd.DataFrame({'A': {0: "a", 1: "b", 2: "c"},
                   'B': {0: 1, 1: 3, 2: 5}, 'C': {0: 2, 1: 4, 2: 6}})

print(df)

# AQUI ELE VAI FUNDIR O "A" COM "B":
melt = pd.melt(df, id_vars=['A'], value_vars=['B', 'C'], var_name='LETRA', value_name='Nº')
print(melt)
