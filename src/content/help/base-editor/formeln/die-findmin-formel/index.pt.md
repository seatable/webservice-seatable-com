---
title: 'A Fórmula Findmin'
date: 2023-02-13
lastmod: '2026-11-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/pt/ajuda/formula-findmin'
aliases:
    - '/pt/ajuda/die-findmin-formel'
seo:
    title: 'Fórmula Findmin no SeaTable – determinar o menor valor ligado'
    description: 'Saiba como aplicar a fórmula Findmin no SeaTable para localizar o valor mínimo em registros vinculados e colunas numéricas.'
---

A **fórmula Findmin** procura o **valor mínimo** entre as entradas da coluna ligada e devolve-o. Isto é útil se houver **várias entradas** na tabela ligada que se referem ao mesmo registo (por exemplo, de uma pessoa ou categoria) noutra tabela.

## Para que pode utilizar a fórmula Findmin

Pode utilizar a fórmula Findmin com todos os valores alfanuméricos para determinar o **valor mínimo**. Digamos que utiliza o SeaTable para o [planeamento orçamental]({{< relref "templates/finance/budget-plan" >}}), onde uma tabela armazena as despesas e outra tabela as categorias. Pode então ligar cada despesa a uma categoria. Para saber qual foi **a despesa mais baixa por categoria**, pode usar a **fórmula Findmin** para mostrar o menor valor de todas as despesas ligadas.

![fórmula findmin](images/findmin.png)

## Para utilizar a fórmula Findmin

### Acrescentar uma ligação de tabela

Ver o artigo da [coluna de ligação]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) para informações sobre como criar uma coluna do tipo **Ligação a outras entradas**. Este é um requisito básico para se poder utilizar a fórmula Findmin.

{{< warning headline="São necessárias várias linhas ligadas" >}}

A utilização da fórmula Findmin só faz sentido se a opção **Limitar as ligações a uma linha no máximo** estiver desativada nas definições de uma coluna de ligação. Se a opção estivesse ativada, a fórmula Findmin mostraria sempre o mesmo valor que a única linha ligada.

{{< /warning >}}

### Adicionar uma coluna com fórmula Findmin

![fórmula findmin](images/findmin.gif)

1. Criar uma nova coluna do tipo **Fórmula para links**.
2. Defina a opção **Findmin** como a fórmula.
3. Seleccione a coluna previamente criada do tipo **Link para outras entradas** nesta tabela.
4. Defina agora a **coluna de pesquisa na tabela ligada** cujo registo com o valor mínimo deve ser apresentado na coluna Findmin.
5. Selecione a **coluna de comparação na tabela ligada** na qual pretende determinar o valor mínimo.
6. Clique em **Submeter**.
