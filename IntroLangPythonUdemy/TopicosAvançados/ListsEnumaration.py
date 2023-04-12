#Enumaration: Usado para ter acesso ao index e ao valor de um array


lista = ["abacate", "banana", "carambola", "diacono"]

for index, nome in enumerate(lista):
    print(index, nome, sep=' -- ')