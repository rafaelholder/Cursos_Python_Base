#Objetos, instancias e métodos:

import random #importação que da acesso a classe Random. É pelas classes que podemos criar objetos.

ClasseRandom = random.Random() #instancia de um objeto/Criação de um novo objeto
num_random = ClasseRandom.randint(10, 20) #uso de métodos(funções) da classe instanciada
print(num_random)

x = 1
while x <= 8:
    num_random = ClasseRandom.randint(0, 20) #uso de métodos(funções) da classe instanciada
    print("Numero", str(x), "da mega sena: ", str(num_random))
    if x == 8:
        print("E aí, ganhou?")
    x += 1
