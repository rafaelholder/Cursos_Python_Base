#   Reduce em python: 
# Forma de aplicar uma função sobre todos os valores do array. 
# Começando pelo primeiro index e indo até o ultimo

from functools import reduce #import do reduce

def multiply (x, y):
    return x * y

lista = [1, 3, 5, 10]

soma = reduce(multiply, lista) #Uso do reduce para multiplicar todos os valores do array
print(soma)