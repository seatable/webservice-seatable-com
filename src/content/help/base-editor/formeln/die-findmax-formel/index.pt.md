---
title: 'A Fórmula Findmax'
date: 2023-02-13
lastmod: '2026-11-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/pt/ajuda/formula-findmax-seatable'
aliases:
    - '/pt/ajuda/die-findmax-formel'
seo:
    title: 'Fórmula Findmax no SeaTable: determinar o valor máximo entre registos ligados'
    description: 'Saiba como usar a fórmula Findmax no SeaTable para obter o maior valor de várias entradas ligadas – com exemplos práticos e muito mais.'
---

A **fórmula Findmax** procura o **valor máximo** entre as entradas da coluna ligada e devolve-o. Isto é útil se houver **várias entradas** na tabela ligada que se referem ao mesmo registo (por exemplo, de uma pessoa ou categoria) noutra tabela.

## Para que pode utilizar a fórmula Findmax

Pode utilizar a fórmula Findmax com todos os valores alfanuméricos para determinar o **valor máximo**. Digamos que utiliza o SeaTable para o [planeamento orçamental]({{< relref "templates/finance/budget-plan" >}}), onde uma tabela armazena as despesas e outra tabela as categorias. Pode então ligar cada despesa a uma categoria. Para saber qual foi **a despesa mais alta por categoria**, pode usar a **fórmula Findmax** para mostrar o maior valor de todas as despesas ligadas.

![fórmula findmax](images/findmax.png)

## Para utilizar a fórmula Findmax

### Acrescentar uma ligação de tabela

Ver o artigo da [coluna de ligação]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) para informações sobre como criar uma coluna do tipo **Ligação a outras entradas**. Este é um requisito básico para se poder utilizar a fórmula Findmax.

{{< warning headline="São necessárias várias linhas ligadas" >}}

A utilização da fórmula Findmax só faz sentido se a opção **Limitar as ligações a uma linha no máximo** estiver desativada nas definições de uma coluna de ligação. Se a opção estivesse ativada, a fórmula Findmax mostraria sempre o mesmo valor que a única linha ligada.

{{< /warning >}}

### Adicionar uma coluna com fórmula Findmax

![fórmula findmax](images/findmax.gif)

1. Criar uma nova coluna do tipo **Fórmula para links**.
2. Defina a opção **Findmax** como a fórmula.
3. Seleccione a coluna previamente criada do tipo **Ligação para outras entradas** nesta tabela.
4. Defina agora a **coluna de pesquisa na tabela ligada** cujo registo com o valor máximo deve ser apresentado na coluna Findmax.
5. Selecione a **coluna de comparação na tabela ligada** na qual pretende determinar o valor máximo.
6. Clique em **Submeter**.
