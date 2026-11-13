---
title: 'A Fórmula Rollup'
date: 2023-01-24
lastmod: '2026-11-12'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/pt/ajuda/formula-rollup-seatable'
aliases:
    - '/pt/ajuda/die-rollup-formel'
seo:
    title: 'Fórmula rollup SeaTable: soma, média, ligação de dados'
    description: 'Veja como usar o rollup: some, calcule média, min/máx, concatene registros de colunas vinculadas, ajustes de formato e análise de relacionamentos.'
---

Com a ajuda da fórmula de roll-up do tipo de coluna **Fórmula para ligações**, é possível definir vários valores numéricos de uma coluna ligada em relação umas às outras e efectuar cálculos estatísticos simples.

## Âmbito de aplicação da fórmula de rollup

Com a **fórmula de rollup** é possível determinar as relações entre os valores numéricos. Por exemplo, no [planeamento orçamental]({{< relref "templates/finance/budget-plan" >}}) pode **somar** as despesas de uma categoria, calcular o **valor** **máximo** ou **mínimo** gasto ou mesmo a **média**.

Primeiro é necessária uma coluna do tipo [Ligação a outras entradas]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}). Certifique-se de que a opção **Limitar as ligações a uma linha no máximo** está desativada, pois só assim poderá ligar várias linhas.

A coluna [Fórmula para ligações]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen" >}}) mostra-lhe então a relação selecionada dos valores numéricos dentro da coluna de ligação utilizando a fórmula de rollup. Neste exemplo, escolhemos o método de avaliação **Soma**:

![A fórmula de rollup](images/rollup-formel.png)

## Criar uma coluna com a fórmula de rollup

Leia no artigo [da coluna de ligação]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) como criar uma coluna do tipo **Ligação a outras entradas**. Este é um requisito básico para se poder utilizar a fórmula de enrolamento.

{{< warning headline="São necessárias várias linhas ligadas" >}}

A utilização da fórmula de rollup só faz sentido se a opção **Limitar as ligações a uma linha no máximo** estiver desativada nas definições de uma coluna de ligação. Se a opção estivesse ativada, a fórmula de rollup mostraria sempre o mesmo valor que a única linha ligada.

{{< /warning >}}

![A fórmula de rollup](images/rollup-formel.gif)

1. Criar uma nova coluna do tipo **Fórmula para links**.
2. Defina a opção **Rollup** como a fórmula.
3. Seleccione a **coluna de ligação** que liga à tabela desejada.
4. Decida agora, no campo **Seleccionar a coluna a fundir** na **tabela ligada**, qual a coluna da tabela desejada que pretende ligar e avaliar.
5. Definir o **método de avaliação**. Tem média, mínimo, máximo, soma e concatenação à escolha.
6. Clique em **Submeter**.

## Definições de formato

Pode definir com precisão o **formato** em que os valores numéricos são apresentados. Para tal, clique no **símbolo de menu pendente** triangular da coluna de rollup e selecione a opção **Definições de formato**. Para além de números, também pode utilizar **moedas**, **percentagens** e **durações** como formato. Além disso, pode definir os **separadores decimais e de milhares**, bem como o número de **casas decimais**.

## Alterações posteriores

Naturalmente, pode ajustar a fórmula de rollup posteriormente, por exemplo, alterar o método de avaliação de soma para média. Clique no **símbolo de menu pendente** triangular à direita do nome da coluna e depois em **Personalizar tipo de coluna**. Aí encontra as mesmas definições que na criação da coluna.
