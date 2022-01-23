


# representar um vetor: V = [a1, a2, a3, ... an], onde o index de a1 é 0, a2 é 1, a3 é 2, e an é n-1.
from pandas import MultiIndex

v = [22, 55, 7, 9]

#
import pandas as pd

"""
PANDAS MULTIINDEX

a multi-level, or hierarchival, index object for pandas objects.

PARAMETROS: Levels, Codes, Labels, Sortorder, names, copy, verify_integrity.

    levels: sequência de matriz (arrays) 
            Um rótulo (labels) único para cada nível
    codes: sequencia de matriz  (arrays). 
            um número inteiro para cada nível designado que rotula em cada localização
    labels: sequencia de matriz (arrays) 
            um número inteiro para cada nível cada nível designando com rótilos cada localização 
"""
# EXEMPLO:

arrays = [[1, 4, 3, 2], ['red', 'blue', 'red', 'blue']]
print(pd.MultiIndex.from_arrays(arrays, names=('number', 'color')))
# RESULTADO
# MultiIndex([(1,  'red'),
#             (4, 'blue'),
#             (3,  'red'),
#             (2, 'blue')],
#            names=['number', 'color'])

# FROM PRODUCT
numeros = [0, 1, 2]
cores = ['verde', 'roxo']
print(f'\n# FROM PRODUCT:')
# print(pd.MultiIndex.from_product([numeros, cores], names=['numero', 'cores']))
print(pd.MultiIndex.from_product())