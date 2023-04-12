# Funções internas, nativas e instaladas
## internas: Funções como max() e round(). Já vem no python puro. Sem uso de import
## Nativas: Funções que tem que ser importadas. EX: from statistics import mean 
## Instaladas: Funções que precisam ser instaladas pelo pip. EX: python -m pip install numpy. 

#Nativa
import statistics

#instalada com pip

import numpy as np
a = np.random.random((8))
print(type(a))
print(a)

#Função interna
print(abs(-200))
