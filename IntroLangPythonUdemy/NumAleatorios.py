#Gerando números aleatorios usando o import Random

import random

#Gerando numero aleatorio com metodo randint()
numAleatorio = random.randint(0, 18)
print(numAleatorio)

#Escolhendo aleatoriamente um item de dentro de uma lista
listaChoice = [2, 34, 123, 902]
numChoice = random.choice(listaChoice)
print(numChoice)