---
title: 'Erros típicos ao trabalhar com fórmulas'
date: 2023-05-03
lastmod: '2023-05-03'
categories:
    - 'formeln'
author: 'nsc2'
url: '/pt/ajuda/erros-formulas-seatable'
aliases:
    - '/pt/ajuda/typische-fehler-beim-arbeiten-mit-formeln'
seo:
    title: 'Principais erros com fórmulas no SeaTable: soluções'
    description: 'Identifique e corrija erros comuns em fórmulas do SeaTable: use corretamente aspas, parênteses, vírgulas e referências de colunas.'

---

A [coluna de fórmulas]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) abre-lhe muitas possibilidades para trabalhar com os seus dados. Com a ajuda de fórmulas, pode, por exemplo, relacionar valores de diferentes colunas entre si e efetuar cálculos com eles. No entanto, uma vez que o trabalho com fórmulas mais complexas pode ser difícil, sobretudo no início, neste artigo apresentamos-lhe **soluções para os problemas mais conhecidos**.

## Faltam aspas nos elementos de texto

Cada elemento de texto nas suas fórmulas **tem de** ser obrigatoriamente colocado entre aspas para que seja reconhecido pelo editor de fórmulas. Se um texto **não** estiver entre aspas, pode aparecer a seguinte **mensagem de erro**:

![Mensagem de erro que aparece quando faltam aspas à volta de elementos de texto](images/Fehlermeldung-fehlende-Anfuehrungszeichen-bei-Textelementen.png)

#### Entrada incorreta:

![Introdução incorreta de elementos de texto](images/fehlerhafte-eingabe-anfuehrungszeichen.png)

#### Entrada correta:

![Introdução correta de elementos de texto](images/richtige-eingabe-anfuehrungszeichen.png)

{{< warning  headline="Dica"  text="Os elementos de texto são sempre marcados a **vermelho** numa fórmula e podem assim ser distinguidos de outros elementos. Se um elemento de texto **não** estiver marcado a **vermelho** no editor de fórmulas, isso significa que foi introduzido **incorretamente**." />}}

## Os parênteses das funções estão em falta ou mal colocados

No editor de fórmulas, **cada função** tem de ser seguida primeiro por um **parêntese de abertura** antes de adicionar outros elementos. Depois de adicionar à fórmula todos os elementos de uma função, esta tem também de terminar com um **parêntese de fecho**. Se **não** forem colocados parênteses, o editor de fórmulas **não** consegue reconhecer a função e podem aparecer as seguintes mensagens de erro:

![Mensagem de erro que aparece se não for colocado um parêntese de abertura após uma função](images/Fehlermeldung-bei-fehlender-Klammer-nach-einer-Funktion.png)

![Mensagem de erro que aparece quando os parênteses de uma função são colocados incorretamente](images/fehlermeldung-klammern-bei-funktion-falsch-gesetzt.png)

#### Entrada incorreta:

![Introdução incorreta de uma função](images/fehlerhafte-eingabe-funktion-1.png)

#### Entrada correta:

![Introdução correta de uma função](images/korrekte-eingabe-funktion-1.png)

{{< warning  headline="Dica"  text="As funções são sempre marcadas a **azul** numa fórmula. Se clicar num parêntese de abertura ou de fecho no editor de fórmulas, **o parêntese correspondente é realçado**. Assim, pode detetar mais facilmente parênteses em falta ou incorretos ao introduzir funções." />}}

## Colocação incorreta de parênteses e chavetas em geral

A colocação correta de parênteses e chavetas é um dos maiores desafios ao introduzir fórmulas. Quer se trate de **parênteses ou de chavetas**, têm de ser sempre colocados no **sítio certo** de uma fórmula para que esta seja reconhecida pelo editor de fórmulas.

### Parênteses

A **secção anterior** deste artigo explica como colocar corretamente os parênteses ao introduzir funções.

### Chavetas

Utilize chavetas quando pretender fazer referência a determinadas **colunas da tabela**. O **nome** da coluna pretendida tem de estar sempre rodeado por **duas chavetas**. Se **não** forem colocadas chavetas ou se forem colocadas chavetas **incorretas**, o editor de fórmulas **não** consegue reconhecer a referência à coluna e podem aparecer as seguintes mensagens de erro:

![Mensagem de erro que aparece se não forem colocadas chavetas ao fazer referência a nomes de colunas](images/fehlermeldung-keine-geschweiften-klammern.png)

![Mensagem de erro que aparece quando as chavetas são colocadas incorretamente ao fazer referência a nomes de colunas](images/fehlermeldung-geschweifte-klammern-falsch-gesetzt-1.png)

#### Entrada incorreta:

![Introdução incorreta de chavetas ao fazer referência a nomes de colunas](images/fehlerhafte-eingabe-geschweifte-klammern-1.png)

#### Entrada correta:

![Introdução correta de chavetas ao fazer referência a nomes de colunas](images/korrekte-eingabe.geschweifte-klammern.png)

### Referências a colunas dentro de funções

Se pretender fazer referência a nomes de colunas dentro de uma função, tem de prestar especial atenção à colocação correta dos parênteses e das chavetas. Tenha em conta as regras específicas para as funções e as referências a colunas. Se não tiver a certeza de que um par de parênteses ou chavetas está completo, lembre-se de que o segundo sinal é sempre realçado quando clica num deles no editor de fórmulas.

#### Entrada incorreta:

![Introdução incorreta de uma função com referência a uma coluna](images/fehlerhafte-eingabe-einer-funktion-mit-spaltenverweis.png)

#### Entrada correta:

![Introdução correta de uma função com referência a uma coluna](images/korrekte-eingabe-einer-funktion-mit-spaltenverweis.png)

## Encadear várias funções

Se pretender incluir **várias funções** na sua fórmula, tem de ter o cuidado de separar sempre as diferentes funções com uma **vírgula**.

Além disso, tem de terminar as fórmulas que contêm várias funções com **vários parênteses de fecho**. Se a sua fórmula contiver, por exemplo, três funções, tem também de terminar com três parênteses de fecho no editor de fórmulas.

Se estes pontos **não** forem respeitados, o editor de fórmulas **não** consegue reconhecer a fórmula introduzida e podem aparecer as seguintes mensagens de erro:

![Mensagem de erro que aparece quando uma fórmula que contém várias funções não termina com o número necessário de parênteses de fecho](images/fehlermeldung-zu-weinge-klammern-am-ende-der-formel.png)

![Mensagem de erro que aparece se não forem colocadas vírgulas entre as várias funções de uma fórmula ou se forem colocadas incorretamente](images/fehlermeldung-falsche-kommasetzung.png)

#### Entrada incorreta:

![Introdução incorreta de uma fórmula em que foram encadeadas várias funções](images/fehlerhafte-eingabe-einer-formel-mit-mehreren-funktionen.png)

#### Entrada correta:

![Introdução correta de uma fórmula em que foram encadeadas várias funções](images/korrekte-eingabe-formel-mit-mehreren-funktionen.png)

{{< warning  headline="Dica"  text="Em fórmulas mais complexas, trabalhe sempre com **espaços e quebras de linha** para poder ver separadamente as diferentes funções da sua fórmula e detetar erros mais facilmente." />}}

## Concatenar vários elementos de texto numa fórmula

Para concatenar vários elementos de texto na sua fórmula, tem de separar os diferentes elementos de texto uns dos outros com um **símbolo &**. Se **não** forem adicionados **símbolos &** entre os elementos de texto, o editor de fórmulas **não** consegue reconhecer a fórmula introduzida e aparece a seguinte mensagem de erro:

![Mensagem de erro que aparece quando vários elementos de texto numa fórmula não estão separados por &.](images/Fehlermeldung-bei-fehlendenen-zwischen-Textelementen.png)

#### Entrada incorreta:

![Introdução incorreta de vários elementos de texto numa fórmula](images/fehlerhafte-Eingabe-mehrere-Textelemente.png)

#### Entrada correta:

![Introdução correta de vários elementos de texto numa fórmula](images/korrekte-Eingabe-mehrere-Textelemente.png)

{{< warning headline="Dica" text="Para que os vários elementos de texto fiquem separados por um espaço, insira **dois símbolos &** e **duas aspas (em cima)** entre cada um dos elementos de texto." />}}

![Edição da fórmula de modo a que os elementos de texto fiquem separados por um espaço](images/Leerzeichen-zwischen-Textelementen.png)
