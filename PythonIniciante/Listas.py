# Listas // Arrays
## list = [1, 2, 3, true, [10, 20, 30], "Lista"]

print("Declarações de lista")
lista = [1, 2, 3]
lista2 = [1 , 2 , 3, "lista com string, boolean e numeros", True]
lista3 = [1 , 2 , 3, [10, 20, 30], 'Lista com string, numeros e outra lista dentro']
lista4 = list(range(0, 20)) #Lista com 20 itens

print("Trocando valores dos index da lista")
print(lista[0])
lista[0] = 19
print(lista[0])

print("Verificando quantos elementos a lista tem")
quantElements = len(lista)
print("Quantidade de elementos da lista 1: " + str(quantElements))

for n in range(0, len(lista3)):
    print(lista3[n])