---
title: 'Exemplo de fórmula: fundir colunas de texto com a ajuda de uma fórmula'
date: 2023-01-28
lastmod: '2023-09-18'
categories:
    - 'formeln'
author: 'nsc2'
url: '/pt/ajuda/exemplo-formula-juntar-colunas-texto'
aliases:
    - '/pt/ajuda/formelbeispiel-zusammenfuehren-von-text-spalten-mit-hilfe-einer-formel'
seo:
    title: 'Exemplo de fórmula: juntar colunas de texto SeaTable'
    description: 'Veja como usar fórmulas SeaTable para unir textos de múltiplas colunas em um só campo, útil para nomes completos ou frases customizadas.'
---

As fórmulas SeaTable oferecem-lhe várias formas de trabalhar com os dados das suas tabelas. Uma delas é a fusão de conteúdos de diferentes [colunas de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}). Com a ajuda de uma fórmula correspondente, pode fundir qualquer número de conteúdos de diferentes colunas numa coluna de fórmula.

## Fusão de colunas de texto

No exemplo concreto, o objetivo é utilizar uma fórmula para fundir o conteúdo (apelido, nome próprio e título) das três primeiras colunas num **nome completo**.

![Exemplo de tabela para fundir diferentes conteúdos numa única coluna de fórmula](images/example-table-zusammenfuehren-von-inhalten-mit-Formel.png)

Para o fazer, comece por adicionar uma **coluna de fórmula** à tabela, em cujo editor pode então inserir a fórmula.

![Acrescentar uma fórmula no campo de texto previsto para o efeito](images/insert-formular-example-1.png)

Para fundir conteúdos de diferentes colunas de texto numa única coluna, deve referir sempre os **nomes das colunas** nas quais os conteúdos correspondentes podem ser encontrados na sua tabela. É particularmente importante que os nomes das colunas sejam enquadrados **entre parênteses rect** os, caso contrário o SeaTable **não consegue** reconhecer quais os conteúdos que devem ser fundidos.

{{< warning  headline="Dica"  text="Os **nomes das colunas** na tabela aberta são apresentados à esquerda no **editor de fórmulas** e podem ser inseridos na fórmula com um **duplo clique**." />}}

![Quando se referir a nomes de colunas nas suas tabelas, rodeá-las sempre com parênteses encaracolados](images/verweis-auf-spaltennamen-in-formel-beispiel-2.png)

Para fundir o conteúdo das colunas de texto numa coluna de fórmula, primeiro organize os nomes das colunas na **ordem** desejada na fórmula e separe cada um deles com um **símbolo &**, que encontrará no editor de fórmulas com os **operandos**.

![Organizar os diferentes nomes de colunas na ordem desejada na fórmula e separá-los com um & símbolo](images/insert-symbols.png)

Para separar os diferentes conteúdos com um **espaço**, adicione um **símbolo &** e **duas vírgulas invertidas (acima)** **após os** dois primeiros nomes de coluna.

![Adição de um símbolo adicional e duas vírgulas invertidas após os nomes das duas primeiras colunas](images/insert-and-22-22-to-the-formular.png)

Depois de confirmar a fórmula introduzida, os conteúdos das colunas de texto são automaticamente fundidos e o **resultado** aparece automaticamente na coluna da fórmula.

![Coluna Fórmula após confirmação da fórmula introduzida.](images/table-example-2-after-formular.png)

{{< warning  headline="Dica profissional" >}}

Sempre que utilizar colunas de texto numa fórmula e estas colunas também puderem estar vazias, recomenda-se a utilização da função trim _( )_. Esta função remove os espaços no início e no fim de um texto. A fórmula completa é então, por exemplo

```
trim( {Title} & " " & {Surname} & " " & {Name} )
```

{{< /warning >}}
