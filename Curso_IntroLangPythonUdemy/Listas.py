# Manipulando listas com python

minha_lista = [1, 4, 5, 6, 2, 3, 4, 6, 100, 22, 345, 21, 0]

#ordenando a lista 
minha_lista.sort() #Ou: minha_lista = minha_lista.sorted()
print(minha_lista)

op = int(input("Digite para ordenar a lista de tras p frente: \n    1 para .sort(reverse=True)\n    2 para .reverse()\n"))
if op == 1:
    minha_lista.sort(reverse=True)
elif op == 2:
    minha_lista.reverse()
else:
    print("Erro")
print(minha_lista)


