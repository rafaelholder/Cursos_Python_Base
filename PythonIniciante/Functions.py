# Funções em python
## def nome_function():

def imprimir(parameter):
    print(parameter)

def potencia(num):
    return num * num

##Valores default
def print_intervalo(ini=0, fim=10):
    for ini in range(ini, fim+1):
        print(ini)

print("o quadrado de 3 é:" + str(potencia(3)))

print("\nFunção com valores marcados para inicio = 2 e fim = 20:\n ")
print_intervalo(ini=2, fim=20)
print("\nFunção com valores default:\n ")
print_intervalo() # chama a função com os valores default
 