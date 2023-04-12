#Tratamento de exceptions



a = input("Digite 10: ")
b = input("Digite 0: ")
try:
    print(int(a) / int(b))
except:
    print("Não é permitida a divisão por zero")