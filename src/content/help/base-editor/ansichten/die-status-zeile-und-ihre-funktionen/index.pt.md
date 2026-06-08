---
title: 'A barra de estado e as suas funções'
date: 2023-02-21
lastmod: '2023-02-21'
categories:
    - 'ansichtsoptionen'
author: 'nsc2'
url: '/pt/ajuda/barra-de-status-e-suas-funcoes'
aliases:
    - '/pt/ajuda/die-status-zeile-und-ihre-funktionen'
seo:
    title: 'Barra de status no SeaTable – contagem e cálculos'
    description: 'Saiba como funciona a barra de status do SeaTable: conte linhas, calcule somas, médias, medianas e estatísticas diretamente na base.'
weight: 30
---

A **barra de estado** está localizada na parte inferior das suas tabelas e cumpre basicamente duas funções diferentes, que são explicadas com mais detalhe neste artigo:

- **Função 1**: Contar as filas numa vista
- **Função 2**: Indicação de um valor calculado a partir de todas as entradas (por exemplo, soma, média, etc.) no caso de colunas baseadas em números

Graças à barra de estado, tem sempre em vista estes **valores estatísticos básicos** assim que abre uma tabela.

## Contando as filas numa vista

A barra de estado indica na margem inferior esquerda o número de todas as **filas** que estão na **vista da tabela** actualmente aberta. Se [filtrar numa vista]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}), a barra de estado conta apenas as restantes entradas da tabela.

![A barra de estado indica sempre o número de filas na vista da tabela actualmente aberta](images/status-cell-function-1.jpg)

Além disso, pode [seleccionar linhas]({{< relref "help/base-editor/zeilen/mehrere-zeilen-selektieren" >}}) individuais – depois a barra de estado refere-se apenas às entradas seleccionadas.

## Indicação de um valor calculado a partir de todas as entradas

Para **colunas baseadas em números**, a barra de estado para cada coluna dá um **valor** calculado a partir de todas as entradas.

![Valores calculados nas linhas de estado](images/the-status-cell-function-2-1.png)

## Opções de cálculo

Para colunas baseadas em números, estão disponíveis as seguintes **opções de cálculo** na barra de estado:

- Cálculo da **soma** de todas as entradas da coluna
- Cálculo do **valor médio** a partir de todas as entradas da coluna
- Cálculo da **mediana** a partir de todas as entradas da coluna
- Determinação do **valor máximo** a partir de todas as entradas da coluna
- Determinação do **valor mínimo** a partir de todas as entradas da coluna
- Nenhum cálculo

![Opções de cálculo da barra de estado](images/berechnungsoptionen-status-zeile.png)

## Tipos e formatos de colunas compatíveis

Para os seguintes tipos de colunas, a barra de estado reflecte um valor calculado:

- [Colunas numéricas]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})
    - Número
    - Porcentagem
    - Moeda
- [Colunas de duração]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}})
- [Colunas de avaliação]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}})
- Valores numéricos em [colunas de fórmula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})

Para os seguintes tipos de colunas, a barra de estado **não** reflecte um valor calculado, embora (possam) conter números:

- [Colunas de datas]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
- [Tempo criado]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) y [Último tempo modificado]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})
- [Número automático]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
- Números em [colunas de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}})
