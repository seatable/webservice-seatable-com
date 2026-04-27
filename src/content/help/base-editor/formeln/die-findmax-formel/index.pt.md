---
title: 'A Fórmula Findmax'
date: 2023-02-13
lastmod: '2023-02-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/pt/ajuda/formula-findmax-seatable'
aliases:
    - '/pt/ajuda/die-findmax-formel'
seo:
    title: 'Fórmula Findmax no SeaTable: calcule o valor máximo entre registros vinculados'
    description: 'Veja como a fórmula Findmax do SeaTable encontra o maior valor numérico entre vários registros conectados, com exemplos práticos para gestão de dados.'
---

A **fórmula Findmax** procura o **valor máximo** entre as entradas da coluna ligada e devolve-o. Isto é útil se houver **várias entradas** na tabela ligada que se referem ao mesmo registo (por exemplo, de uma pessoa) noutra tabela.

A fórmula Findmax só funciona com **valores numéricos**, razão pela qual o conteúdo da coluna ligada deve também consistir em valores numéricos. Além disso, a utilização da fórmula Findmax só faz sentido se o selector **Permitir a ligação a várias linhas** for activado ao criar a coluna **Ligação a outras entradas**. Se a opção estivesse desligada, a fórmula Findmax conteria sempre o mesmo número que na coluna ligada.

## Para que precisa da fórmula Findmax

A **função Findmax** deve ser utilizada quando se pretende **cruzar** valores numéricos armazenados em diferentes tabelas. Digamos que utiliza SeaTable para recolher as **horas de trabalho** dos seus empregados, onde uma tabela armazena os empregados e outra tabela armazena a actividade diária. Pode então ligar cada registo de empregado às horas de trabalho introduzidas.

![fórmula findmax](images/findmax-1.png)

Para saber quando um empregado fez o último login, pode usar a **fórmula Findmax** para mostrar o **maior valor** - neste caso a última vez - a partir do total de tempos de login numa coluna.

![A fórmula findmax](images/findmax2-1.png)

Pode usar a fórmula Findmax com todos os valores numéricos para representar o **valor máximo**.

## Para utilizar a fórmula Findmax

### Acrescentar uma ligação de tabela

Ver o artigo [How to Link Tables in SeaTable]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) para informações sobre como criar uma coluna do tipo **Link to Other Entries**. Este é um requisito básico para se poder utilizar a fórmula Findmax.

### Adicionar uma coluna com fórmula Findmax

![fórmula findmax](images/findmax.gif)

1. Criar uma nova coluna do tipo **Fórmula para links**.
2. Defina a opção **Findmax** como a fórmula.
3. Seleccione a coluna previamente criada do tipo **Link para outras entradas** nesta tabela.
4. No campo **Selecionar coluna de pesquisa na tabela ligada "..."**, defina a coluna da outra tabela que pretende ligar à coluna aqui.
5. Clique em **Submeter**.

{{< warning  headline="Atenção"  text="A fórmula Findmin só funciona com **valores numéricos**, pelo que a coluna ligada deve conter valores numéricos." />}}
