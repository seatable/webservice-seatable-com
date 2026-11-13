---
title: 'A Fórmula Countlinks'
date: 2023-01-11
lastmod: '2023-01-24'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/pt/ajuda/countlinks-formula-seatable'
aliases:
    - '/pt/ajuda/die-countlinks-formel'
seo:
    title: 'Countlinks no SeaTable: quantificar vínculos fáceis'
    description: 'Com Countlinks, conte automaticamente as entradas ligadas a uma linha. Ideal para listas de participantes, análises ou qualquer tipo de ligação múltipla.'

---

A fórmula Countlinks conta o número de entradas ligadas do tipo de coluna **Ligação a outras entradas** na respectiva linha.

{{< warning  headline="A ligação de tabelas é um requisito básico" >}}

Só pode criar uma coluna com a fórmula Countlinks se tiver ligado duas tabelas. Leia [aqui como criar uma tal ligação]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}).

{{< /warning >}}

## Âmbito da Fórmula Countlinks

A **fórmula Countlinks** deve ser sempre utilizada quando pretender exibir o **número de entradas ligadas a uma linha**.

Por exemplo, ao planear um workshop, é possível exibir o número de participantes registados a partir de uma tabela separada. A [coluna de ligação]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) registaria assim os nomes de todos os participantes.

![A Fórmula Countlinks.](images/countlinks-2.png)

A utilização da fórmula Countlinks só faz sentido se a opção **Limitar as ligações a uma linha no máximo** estiver desativada nas definições de uma coluna de ligação. Se a opção estivesse ativada, o campo da fórmula Countlinks mostraria sempre um 1 (= uma única linha ligada).

## Criação de uma Fórmula Countlinks

![A Fórmula Countlinks.](images/countlink.gif)

1. Criar uma nova coluna do tipo **Fórmula para links**.
2. Dar à coluna um **nome** adequado.
3. Defina a opção **Countlinks** como a fórmula.
4. Agora seleccione a **coluna de ligação** cujas entradas deseja contar na coluna **Seleccionar** ligação **neste** campo da **tabela**.
5. Clique em **Submeter**.
