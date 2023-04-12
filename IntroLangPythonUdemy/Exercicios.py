

print("\n---Verificador de maioridade---")
age = int(input("Digite sua idade:"))
if age >= 18:
    print("maior de idade")
elif age < 18:
    print("menor de idade")
else:
    print("erro")


print("\n---Ver se foi aprovado---")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("digite a segunda nota: "))
media = (nota_1 + nota_2) / 2
if media >= 6:
    print("parabens vc foi aprovado!")
else:
    print("vc foi reprovado")



print("\n---Resolver equação de segundo grau completa---")
from math import sqrt
def delta(a, b, c):
    return b * b - 4 * a * c

def raiz_com_mais(a, b, c):
    return (-b + sqrt(delta(a, b, c))) / 2 * a

def raiz_com_menos(a, b, c):
    return (-b - sqrt(delta(a, b, c))) / 2 * a

a = float(input("digite a: "))
b = float(input("digite b: "))
c = float(input("digite c: "))

try:
    resultado_com_mais = raiz_com_mais(a, b, c)
    resultado_com_menos = raiz_com_menos(a, b, c)
    
    print(resultado_com_mais)
    print(resultado_com_menos)
except:
    print('A equação não tem raízes reais.')



print("\n---Ordenando listas---")
lista = [19, 6, 24]
print("Lista crua: " + str(lista))

lista.sort()
print("Lista ordenada do menor ao maior: " + str(lista))
lista.sort(reverse=True)
print("Lista invertida. Ordenada do maior ao menor: " + str(lista))



print("---Calculadora Basica---")
try:
    x = float(input("Digite X: "))
    y = float(input("Digite Y: "))
    sinal = input("Digite o sinal(+, -, *, /): ")
    result = 0

    if sinal == '+': result = (x + y)
    elif sinal == '-': result = (x - y)
    elif sinal == '*': result = (x * y)
    elif sinal == '/': result = (x / y)
    else: print("Sinal invalido")

    print(result)
except:
    print("Erro")
# assert 64 == delta