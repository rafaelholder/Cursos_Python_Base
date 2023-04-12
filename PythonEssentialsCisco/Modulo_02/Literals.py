# Literals: Dados cujos valores são determinados pelo próprio literal.
## EX: / 1906 / é um literal, mas / c / não 

## Printando Números octal: EX: print(0o123). Se usa o prefixo 0o(zero-o)
numOctal = 0o234
numDecimal = 156
if numOctal == numDecimal:
    print("True")
    print(str(numOctal), str(numDecimal), sep=" ")

## Printando Números hexadecimal: EX: print(0x456). Se usa o prefixo 0x(zero-x)
numHexadecimal = 0x456
numDecimal = 1110
if numHexadecimal == numDecimal:
    print("True")
    print(str(numHexadecimal), str(numDecimal), sep=" ")

## INTEIROS E FLOATS:
### int(): EX: 4, 3, 1874, ...  float(): EX: 3.14, 9.8, 0.6, ...
### 4 =/= 4.0. O primeiro é inteiro e o segundo é float
inteiro = 6
floatPoint = 1.9
print(inteiro, floatPoint, sep='---')
print(type(inteiro), type(floatPoint), sep="---")

## Representando expoentes com python
### EX: O número 10 elevado a oitava potencia ficaria: 10E-8
### O Python escolhe sempre a forma mais econômica de apresentação do número
expoentePython = 10E8
expoenteNumero = 1000000000
if(expoentePython == expoenteNumero):
    print(True)
    print(int(expoentePython)) 


## VALORES BOOLEANOS:
'''
    - O nome vem de George Boole (1815-1864), autor da obra fundamental, 
    As Leis do Pensamento, que contém a definição de álgebra Booleana 
    uma parte da álgebra que faz uso de apenas dois valores distintos: 
    True e False, denotado como 1 e 0.
    True = 1; False = 0; então True(1) > False(0)
''' 
print(True > False)
print(True < False)

print("\"I'm\"", "\"\"Learning\"\"", "\"\"\"Python\"\"\"", sep="\n")


#RESUMO:
'''
    1. Os literais são notações para representar alguns valores fixos em código. 
    O Python tem vários tipos de literais - por exemplo, um literal pode ser um número 
    (literais numéricos, por exemplo, 123), ou uma string (literais de string, por exemplo, “Eu sou um literal.“).

    2. O sistema binário é um sistema de números que emprega 2 como base. Portanto, 
    um número binário é composto apenas por 0s e 1s, por exemplo, 1010 é 10 em decimal.

    Os sistemas de numeração octal e hexadecimal, do mesmo modo, empregam 8 e 16 como suas bases, respetivamente. 
    O sistema hexadecimal utiliza os números decimais e seis letras extra(0123456789abcdef).
    
    3. Inteiros (ou simplesmente ints) são um dos tipos numéricos suportados pelo Python. 
    São números escritos sem um componente fracionário, por exemplo, 256, ou -1 (inteiros negativos).

    4. Números de floating-point (ou simplesmente floats) são outro dos tipos numéricos suportados 
    pelo Python. São números que contêm (ou são capazes de conter) um componente fracionário, 
    por exemplo 1.27.

    5. Para codificar uma apóstrofe ou uma aspa dentro de uma string, pode usar o caratere de escape, 
    por exemplo, 'I\'m happy.', ou abrir e fechar a string utilizando um conjunto de símbolos opostos aos que deseja codificar, 
    por exemplo "I'm happy." codificar uma apóstrofe, e 'He said "Python", not "typhoon"' para codificar umas aspas (duplas).

    6. Valores booleanos são os dois objetos constantes True e False usado para representar valores de verdade 
    (em contextos numéricos 1 é True, enquanto 0 é False).

    EXTRA

    Há mais um literal especial que é usado em Python: o literal None . 
    Este literal é um chamado NoneType objeto, e é utilizado para representar a ausência de um valor. 
    

    Exercício  

    Qual é o valor decimal do seguinte número binário?

    1011

    
    É 11, porque (2**0) + (2**1) + (2**3) = 11

'''