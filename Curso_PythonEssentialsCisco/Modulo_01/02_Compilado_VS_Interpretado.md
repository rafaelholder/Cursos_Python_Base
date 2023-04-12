Compilação vs. interpretação
    A programação informática é o ato de compor os elementos da linguagem de programação selecionada pela ordem que provocará o efeito desejado. O efeito pode ser diferente em cada caso específico - depende da imaginação, conhecimento e experiência do programador.

É claro que tal composição tem de ser correta em muitos sentidos:

    alfabeticamente - um programa precisa de ser escrito num guião reconhecível, tal como romano, cirílico, etc.
    lexicalmente - cada linguagem de programação tem o seu dicionário e é preciso dominá-lo; felizmente, é muito mais simples e menor do que o dicionário de qualquer língua natural;
    sintaticamente - cada linguagem tem as suas regras, e estas devem ser obedecidas;
    semanticamente - o programa tem de fazer sentido.
    Infelizmente, um programador também pode cometer erros com cada um dos quatro sentidos acima referidos. Cada um deles pode fazer com que o programa se torne completamente inútil.

Vamos supor que tenha escrito um programa com sucesso. Como persuadir o computador a executá-lo? Tem de transformar o seu programa em linguagem de máquina. Felizmente, a tradução pode ser feita pelo próprio computador, tornando todo o processo rápido e eficiente.



Há duas formas diferentes de transformar um programa de uma linguagem de programação de alto nível em linguagem de máquina:

    COMPILAÇÃO - o source program é traduzido uma vez (no entanto, este ato deve ser repetido sempre que modificar o source code) obtendo um ficheiro (por exemplo, um ficheiro .exe se o código se destinar a ser executado no MS Windows) contendo o machine code; agora pode distribuir o ficheiro por todo o mundo; o programa que executa esta tradução chama-se compilador ou tradutor;

    INTERPRETAÇÃO - você (ou qualquer utilizador do código) pode traduzir o source program cada vez que este tem de ser executado; o programa que executa este tipo de transformação chama-se intérprete, pois interpreta o código cada vez que se pretende executá-lo; também significa que não pode simplesmente distribuir o source code tal como está, porque o utilizador final também precisa do intérprete para o executar.

    Devido a algumas razões muito fundamentais, uma linguagem de programação particular de alto nível foi concebida para se enquadrar numa destas duas categorias.

    Há muito poucas linguagens que possam ser compiladas e interpretadas. Normalmente, uma linguagem de programação é projetada com este fator na mente dos seus construtores - será ela compilada ou interpretada?