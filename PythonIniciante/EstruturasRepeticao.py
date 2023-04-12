# Estruturas de repetição
## for, while

print("\nEstruturas de repetição \n WHILE: ")
count = 1
while count <= 5:
    print("Este é um loop while. Repetição número: " + str(count))
    count += 1

print("\nEstruturas de repetição \n FOR: ")
for countFOR in range(5, 0, -1):
    print("Estrutura de repetição FOR com range(5 até 0, decrescendo -1). Repetição número: " + str(countFOR))

for countFORBreak in range(0, 5):
    if countFORBreak == 3:
        break
    print("\nEstrutura de repetição FOR com range(0 até 5, acrescentando 1, se contador for = a 3 ele para a execução do loop).\n Repetição número: " + str(countFORBreak))