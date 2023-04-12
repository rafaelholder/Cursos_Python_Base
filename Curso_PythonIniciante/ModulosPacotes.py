# Modulos, imports e pacotes
## import nome_do_modulo

import statistics as stat #Import com alias
from statistics import median #Import de uma função especifica

z = [10, 20, 30, 20, 40]
x = stat.mean(z) #Media aritimetica
y = median(z) #Mediana
print("Lista: " + str(z))
print("A media aritimetica é: " + str(x))
print("A mediana da lista é: " + str(y))