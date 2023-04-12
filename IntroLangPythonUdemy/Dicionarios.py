#   Em Python, dicionários são arrays associativos, ou seja, 
#um determinado valor passa a ser vinculado a uma chave. Exemplo:

# dicionarios em python
dicionario_sites = {"Rafael": "RafaelHolder.com"}


#No dicionário acima, a chave "Rafael" foi vinculado ao valor "RafaelHolder.com". 
# Assim, para imprimir o valor chame:

print(dicionario_sites['Rafael'])
# Sera impresso "RafaelHolder.com


meu_dicionario = {"a":"ameixa", "b":"bola", "c":"cachorro"}

for chave in meu_dicionario:
    print(chave + ":" + meu_dicionario[chave])

op = str(input("Digite: a, b ou c:\n"))
if op == 'a':
    print(meu_dicionario["a"])
elif op == 'b':
    print(meu_dicionario["b"])
elif op == 'c':
    print(meu_dicionario["c"])
else:
    print("OPÇÃO INVALIDA")

#Convertendo o dicionario para tupla: 
# Transformando as chaves e valores e um item só(Chave-Valor)
for i in meu_dicionario.items(): 
    print(i)