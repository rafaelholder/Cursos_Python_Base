#loops com while e for

## Loops infinito
# x = 1
# while x < 10:
#     print(".")
x = 0
while  x < 10:
    print(x)
    x += 1

# Percorrendo listas com For
lista1 = [1,2,6,3,1]
lista2 = ['ola', True, 1, 20, 'mundo', 99.2, False]
for i in lista2:
    print(i)
# Percorrendo For e manipulando range(). range(num_inicial, num_limite, num_acrescentador)
for i in range(10,20,2):                # range(    10    ,     20   ,      2     )
    print(i)                            # resul = 10, 12, 14, 16, 18
