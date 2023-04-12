#Map em python: Uma forma de usar uma função em todos os elementos de um array

def triplo(x):
    return x*3

valor = [1, 2, 3, 4, 5, 6]

#Usar um map para triplicar todos os valores da lista
valor_triplicado = map(triplo, valor)
for i in valor_triplicado:
    print(i)

# #Convertendo de volta para um array:
# valor_triplicado = list(valor_triplicado)
# print(valor_triplicado)