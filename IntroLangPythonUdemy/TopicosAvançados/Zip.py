#Zip: Forma de concatenar arrays em um só

lista_1 = [1, 2, 3, 4]
lista_2 = ["bola", 'abacate', 'cachorro', 'dinheiro']
lista_3 = ["R$10.2","R$2.2","R$110.2","R$230.2",]

for numero, nome, valor in zip(lista_1, lista_2, lista_3):
    print(numero, nome, valor)


