 #forma de alterar o valor da lista inteira com loops e criando uma nova lista

lista_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#vamos elevar todos os valores da lista ao quadrado:
## lista_exemplo = [valor_a_adicionar condição]. EX: lista = [valor+1 for valor in lista]
lista_y = [valor**2 for valor in lista_x]

print(lista_x)
print("\nAgora usando list comprehension:")
print(lista_y)

#Vamos adicionar os números impares de lista_x em lista_z:
lista_z = [valor for valor in lista_x if(valor % 2 == 1)]
print("\nList comprehension usado para selecionar os números impares:")
print(lista_z)