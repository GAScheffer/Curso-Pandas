import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

var = plt.style.available
plt.style.use(var)
plt.rcParams['figure.figsize'] = (11, 7)

d = pd.read_csv('train.csv')
# print(d.head(10))

plt.plot()
plt.title('PASSAGEIROS DO TITANIC', size=24)
plt.xlabel('Passageiros', size=18)
plt.ylabel('Idade', size=18)
plt.show()

print(d)