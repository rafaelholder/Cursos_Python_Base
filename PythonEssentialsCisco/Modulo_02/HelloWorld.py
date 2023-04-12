#Primeiro programa em Python
#Lista de funções internas do Python: https://docs.python.org/3/library/functions.html

##Função print()
print("HelloWorld")

'''
O que é uma função? 
Uma função (neste contexto) é uma parte separada do código do computador capaz de:
    - Causar um qualquer efeito (por exemplo, enviar texto para o terminal, criar um ficheiro, desenhar uma imagem, 
    reproduzir um som, etc.); isto é algo completamente inédito no mundo da matemática;
    - Avaliar um valor (por exemplo, a raiz quadrada de um valor ou o comprimento de um dado texto) e 
    devolvê-lo como o resultado da função; é isto que faz as funções Python serem os parentes dos conceitos matemáticos.
    Além disso, muitas das funções Python podem fazer as duas coisas acima juntamente.
'''

#Argumentos de função: Tudo que esta dentro dos parenteses (). EX: print("Sou" + "um argumento")

#Caracteres de escape:
'''
    A barra invertida (\) tem um significado muito especial quando usado dentro de strings - a isto chama-se o caratere de escape.

    A palavra escape deve ser entendida especificamente - significa que a série de caracteres na string escapa por um momento (um momento muito curto) para introduzir uma inclusão especial.

    Por outras palavras, a barra invertida não significa nada em si, mas é apenas uma espécie de anúncio de que o próximo caratere após a barra invertida também tem um significado diferente.

    A letra n colocada após a barra invertida vem da palavra newline (nova linha).

    Tanto a barra invertida como o 'n' formam um símbolo especial chamado um caractere de newline, que incita a consola a iniciar uma nova linha de output.
'''
print("Primeira linha \nSegunda linha usando \ n")


#Argumento de Keywords: EX: print("ola", end="")
'''
    - Um argumento de keyword consiste em três elementos: uma keyword identificando o argumento 
    (end aqui); um sinal de igual (=); e um valor atribuído a esse argumento;
    - Qualquer argumento de keyword tem de ser colocado após o último argumento posicional (isto é muito importante)

    - O comportamento padrão reflete a situação em que o argumento de 
    keyword end é implicitamente usado da seguinte maneira: end="\\n".
'''
print("My name is", "Python.", end=" ")
print("Monty Python") 
##Nesse exemplo não há a quebra de linha, pois o end padrão é: end="\n"

##Keyword sep="":
print("My", "name", "is", "Manual", sep="--")
'''
    - A função print() agora utiliza dois traços, em vez de um espaço, 
    para separar os argumentos de output.
'''

##Keywords sep= e end= juntas:
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")



print("     *\n",
      "   * *\n",
      "  *   *\n",
      " *     *\n",
      "***   ***\n",
      "  *   *\n",
      "  *   *\n",
      "  *****\n")

print("      **")
print("     *  *")
print("    *    *")
print("   *      *")
print("  *        *")
print(" *          *")
print("***        ***")
print("  *        *")
print("  *        *")
print("  **********")


# RESUMO:
'''
Key takeaways:
    1. A função print() é uma função incorporada. Imprime/faz output de uma mensagem especificada para a janela do ecrã/consola.

    2. As funções incorporadas, ao contrário das funções definidas pelo utilizador, estão sempre disponíveis e não têm de ser importadas. 
    O Python 3.8 vem com 69 funções incorporadas. Pode encontrar a sua lista completa fornecida em ordem alfabética na Biblioteca Padrão Python.

    3. Para chamar uma função (este processo é conhecido como invocação de função ou chamada de função), é necessário usar o nome da função seguido de parêntesis. 
    Pode passar argumentos para uma função, colocando-os dentro dos parêntesis. Deve separar os argumentos com uma vírgula, por exemplo, print("Hello,", "world!"). 
    Uma função “vazia” print() faz output de uma linha vazia para o console.

    4. As strings de Python são delimitadas com aspas, por exemplo, "I am a string" (aspas duplas), ou 'I am a string, too' (aspas simples).

    5. Os programas de computador são coleções de instruções. Uma instrução é um comando para executar uma tarefa específica quando executada, 
    por exemplo, para imprimir uma determinada mensagem no ecrã.

    6. Em strings de Python a barra invertida (\) é um caractere especial que anuncia que o próximo caractere tem um significado diferente, 
    por exemplo \n (the newline character) starts a new output line.

    7. Os argumentos posicionais são aqueles cujo significado é ditado pela sua posição, por exemplo, o segundo argumento 
    é apresentado após o primeiro, o terceiro é apresentado após o segundo, etc.

    8. Os argumentos de keyword são aqueles cujo significado não é ditado pela sua localização, 
    mas por uma palavra especial (keyword) utilizada para os identificar.

    9. Os loops end e sep podem ser usados para formatar o output da função print(). 
    O parâmetro sep especifica o separador entre os argumentos de output (por exemplo, o parâmetro print("H", "E", "L", "L", "O", sep="-"), 
    enquanto o parâmetro end especifica o que imprimir no final da declaração print.
'''


