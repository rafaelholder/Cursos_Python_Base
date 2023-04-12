# OPERADORES
## Operadores básicos:
'''
    Começaremos pelos operadores que estão associados às operações aritméticas mais amplamente reconhecidas:

    +, Adição
    -, Subtração
    *, Multiplicação
    /, Divisão
    //, Divisão Inteira(int)
    %, Modulo/Resto
    **, Exponenciação


    - quando TODOS os argumentos de uma expressão  são inteiros, 
    o resultado é também um inteiro; EX: print(2 * 2) = 4
    - quando pelo menos um argumento da expressão é um float, 
    o resultado é também um float. EX: print(2 * 2.0) = 4.0

    - Um sinal // (dupla barra) é um operador de divisão inteira. 
    Difere do operador padrão / em dois detalhes:
        - o seu resultado não tem a parte fracionada.
        Está ausente (para inteiros), ou é sempre igual a zero (para floats). 
        isto significa que os resultados são sempre arredondados para baixo;
        - Está em conformidade com a regra inteiro vs. float.
    EX: print(2 // 4) = 0
    EX: print(4 // 2.5) = 1.0

    - Um sinal %(percentagem) é o operador de modulo. Dá o valor que sobrou depois de 
    dividir um valor por outro para produzir um quociente inteiro.
    EX: print(14 % 4) = 2
        Como pode ver, o resultado é dois. Esta é a razão:
            14 // 4 = 3; → 3 é o quociente inteiro;
            3 * 4 = 12; → como resultado da multiplicação de quocientes e divisores;
            14 - 12 = 2; → 2 é o resto.

    - Como provavelmente sabe, a divisão por zero não funciona.
    Não tente:
        executar uma divisão por zero;
        executar uma divisão inteira por zero;
        encontrar um remainder de uma divisão por zero.

    - Operadores unários e binários:
    O operador de subtração é obviamente o sinal -(menos), 
    embora deva notar que este operador também tem outro significado 
    ele pode alterar o sinal de um número.

    Em aplicações de subtração, o operador menos espera dois argumentos: 
    o da esquerda (um minuendo em termos aritméticos) 
    e o da direita (um subtraendo).

    Por esta razão, o operador de subtração é considerado um dos operadores binários, 
    assim como os operadores de adição, multiplicação e divisão.

    Mas o operador menos pode ser usado de uma forma diferente (unária) 
    veja abaixo em baixo:
        print(-1.1). 
        Operador -(menos) esta sendo usado para declarar que o número 1.1 é negativo.

    Há também um operador + unário. Pode utilizá-lo assim:
        print(+2)

    - Os operadores e as suas prioridades
    Até agora, temos tratado cada operador como se não tivesse qualquer ligação com os outros. 
    Obviamente, uma situação tão ideal e simples é uma raridade na programação real.

    Considere a seguinte expressão:
        2 + 3 * 5 
        Primeiro deve multiplicar 3 por 5 e, mantendo o 15 na sua memória, 
        depois adicionar o 2, obtendo 17.

    O que faz alguns operadores agirem antes de outros é dito como a hierarquia de prioridades.
    O Python define com precisão as prioridades de todos os operadores, e assume que os operadores 
    maior/mais_alta prioridade realizam as suas operações antes dos operadores de menor prioridade.

    Portanto, se sabe que * tem uma prioridade maior do que +, 
    o cálculo do resultado é óbvio.


    - Os operadores e bindings
    O binding do operador determina a ordem dos cálculos efetuados por alguns operadores 
    com igual prioridade, colocados lado a lado numa só expressão.

    A maioria dos operadores de Python têm binding do lado esquerdo, 
    assim a expressão é lida da esquerda para a direita.
    Este exemplo simples mostrar-lhe-á como funciona. Veja:
        print(9 % 6 % 2)
        Há duas formas de resolver a expressão:
            da esquerda para a direita: primeiro 9 % 6 = 3, em seguida, 3 % 2 = 1;
            da direita para a esquerda: primeiro 6 % 2 = 0, em seguida, 9 = 0 que causa um erro fatal.

        O resultado deve ser 1. Este operador tem ligação do lado esquerdo. 
        Mas há uma exceção interessante...

    - Operadores e bindings: exponenciação
    Veja esse exemplo:
        print(2 ** 2 ** 3)
        Os dois resultados possíveis são:
            2 ** 2 → 4; 4 ** 3 = 64
            2 ** 3 → 8; 2 ** 8 = 256

    Execute o código na idle e veja o que acontece?
        exemplo_1 =(2 ** 2 ** 3)
        exemplo_2 = (2 ** (2 ** 3))
        if exemplo_1 == exemplo_2:
            print(exemplo_1, exemplo_2)
            print('As expressões são equivalentes')

    print(2 ** 2 ** 3) é a mesma coisa de print(2 ** (2**3)).

    O resultado mostra que o operador de exponenciação 
    utiliza o binding do lado direito. 
    Ou seja, o python lê as exponenciações da direita para a esquerda.
'''
exemplo_1 = (2 ** 2 ** 3)
exemplo_2 = (2 ** (2 ** 3))
if exemplo_1 == exemplo_2:
    print(exemplo_1, exemplo_2)
    print('As expressões são equivalentes')

