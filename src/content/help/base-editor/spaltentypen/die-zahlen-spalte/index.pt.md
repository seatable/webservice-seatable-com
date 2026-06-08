---
title: 'A Coluna de Números'
date: 2023-01-08
lastmod: '2023-11-08'
categories:
    - 'text-und-zahlen'
author: 'ssc'
url: '/pt/ajuda/coluna-de-numeros'
aliases:
    - '/pt/ajuda/die-zahlen-spalte'
seo:
    title: 'Coluna de números SeaTable – opções e validação'
    description: 'Use a coluna de números no SeaTable para somas, moedas, validação de valores e configurações personalizadas. Guia para iniciantes.'
---

No SeaTable pode utilizar a **coluna de números** de muitas maneiras para trabalhar com números de qualquer tipo (por exemplo, número de artigos, percentagens, ou preços em diferentes moedas).

## Área de aplicação da coluna de números

A utilização de **colunas de números** permite-lhe, por exemplo, **calcular valores** com fórmulas e criar **gráficos e estatísticas**. No entanto, não é adequada para guardar cadeias de caracteres de qualquer comprimento (por exemplo, números de conta), uma vez que ocorre um arredondamento com mais de 15 dígitos. Neste caso, deve utilizar [a coluna de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}).

Além disso, o SeaTable oferece outras colunas que por vezes se ajustam melhor aos seus valores dados.

- Duração e períodos = [coluna de duração]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}}) 
- Data e horas = [coluna de data]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
- Geo-informação = [coluna de geoposição]({{< relref "help/base-editor/spaltentypen/die-geopositions-spalte" >}})

## Acrescentar uma coluna de números

![Acrescentar uma coluna de números](images/hinzufuegen-einer-zahlenspalte.gif)

1. Clique no **símbolo de mais** à direita da última coluna.
2. Dê um **nome** à coluna.
3. Seleccionar **Número** como o tipo de coluna.
4. Decidir sobre um **formato** (por exemplo, número, percentagem ou moeda).
5. Também pode definir detalhes clicando em **Mais configurações**.
6. Adicionar a coluna com **Submeter**.

## Definições de formato

Também se pode editar e afinar o **formato do número** posteriormente. Para o fazer, primeiro abra o menu pendente com as **opções de coluna** através do triângulo {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} no cabeçalho da coluna e depois clique em {{< seatable-icon icon="dtable-icon-set-up" color="grey" >}} **Configurações do formato**.

Pode agora seleccionar um **formato** diferente, definir **separadores** **decimais** e de **milhar** e alterar o número de **casas decimais**.

### Formatos disponíveis da coluna de números

Estão disponíveis os seguintes formatos numéricos:

- **Número**

    Utilização de um número simples, por exemplo, para o número de artigos.

- **Porcentagem**

    Utilização de percentagens, por exemplo, para o progresso na conclusão das tarefas.

- **Moedas (Yuan, Dólar e Euro)**

    Utilização de diferentes moedas, por exemplo, para os preços dos produtos.

- **Moeda personalizada**

    Utilização de uma moeda personalizada onde o símbolo da moeda pode ser introduzido individualmente.

## Definir o valor predefinido e validar a entrada

Pode [definir o valor predefinido]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) para cada coluna de números, que é automaticamente introduzido em cada linha que adicionar à sua tabela.

Para identificar diretamente **erros** e **valores extremos**, pode também **validar** a **entrada**. Para o efeito, defina um **intervalo numérico** no qual os valores da coluna se devem situar; as células com um valor superior ou inferior são então destacadas a cores.

Estas definições podem ser efectuadas aquando da criação da coluna numérica ou posteriormente:

1. Abra o menu pendente com as **opções de coluna** através do triângulo {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} no cabeçalho da coluna.
2. Em seguida, clique em **Personalizar tipo de coluna**.
3. Clique em **Outras definições** e active as **barras deslizantes** correspondentes na parte inferior.

![Definições de formato das colunas de números](images/Format-settings-of-number-columns.png)
