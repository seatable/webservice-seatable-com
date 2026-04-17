---
title: 'Ordenar entradas numa vista'
date: 2022-10-26
lastmod: '2025-12-05'
categories:
    - 'ansichtsoptionen'
author: 'kgr'
url: '/pt/ajuda/ordenar-entradas-vizualizacao-seatable'
aliases:
    - '/pt/ajuda/sortieren-von-eintraegen-in-einer-ansicht'
seo:
    title: 'Ordenar entradas em uma vista SeaTable'
    description: 'Ordene listas pelas colunas desejadas, crie hierarquia de critérios e conserve seus dados organizados nas diferentes vistas SeaTable.'
weight: 24
---

A função de ordenação permite exibir as entradas não ordenadas numa tabela, numa **sequência ordenada**.

## Ordenar as entradas numa vista

![Ordenação de entradas](images/Sortierung-von-Eintraegen-2.gif)

1. Crie uma [nova vista]({{< relref "help/base-editor/ansichten/anlegen-einer-neuen-ansicht" >}}) ou seleccione a vista que pretende ordenar.
2. Clique na opção **Ordenar** nas opções de visualização acima da tabela.
3. Ir para **Adicionar Ordenação**.
4. No campo vazio, seleccione a **coluna** pela qual pretende ordenar.
5. No segundo campo, decidir se os dados devem ser listados em ordem **ascendente** ou **descendente**.

Repita o processo para **ordenação de vários níveis**. Para **alterar a hierarquia das regras de ordenação**, mantenha premido o botão esquerdo do rato na área de aderência de seis pontos e arraste a regra para a posição pretendida.

A ordenação é efectuada **em tempo real**, ou seja, os registos de dados são ordenados antes de a janela ser fechada. Isto permite-lhe ver imediatamente se alcançou o resultado desejado e fazer quaisquer ajustes necessários.

## Comportamento de ordenação de acordo com o tipo de coluna

SeaTable suporta a ordenação por todos os [tipos de coluna]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) com exceção dos tipos de coluna **Texto formatado, Ficheiro, Imagem, Geoposição, Criador, Último editor, Botão e Assinatura digital**.

A ordenação baseia-se nos seguintes princípios de ordenação:

- Texto, Colaborador, Correio eletrónico, URL, Número de telefone: alfabético ou alfanumérico
- Número, Duração, Classificação, número automático: numérico
- Data, Criado, Última edição: cronológica
- Seleção única e múltipla: de acordo com a ordem das opções
- Caixa de verificação: dicotómica
- Fórmula: consoante o tipo de dados do resultado
- Ligação: consoante o tipo de dados da coluna referenciada

Todas as linhas **com células vazias na coluna de ordenação** são exibidas na parte inferior da vista.

## Remover uma ordem de ordenação

Pode eliminar uma ordenação criada clicando no símbolo **x**.

![Eliminar a ordenação das entradas numa vista](images/Sortieren-von-Eintraegen-in-einer-Ansicht.png)

## Acrescentar linhas recém-adicionadas

Uma ordenação activada é automaticamente aplicada às linhas recentemente adicionadas.

![Ordenação de entradas](images/Sortierung-von-Eintraegen-1-1.gif)

## Aplicar várias ordenações

Ao aplicar ordenações múltiplas, é possível ordenar registos que tenham a **mesma entrada** numa ordenação anterior. Por exemplo, pode começar por ordenar uma lista de empregados pelas opções "mulheres", "homens", "diversos" utilizando uma única coluna de seleção e, em seguida, ordenar os nomes das mulheres, dos homens e dos diversos por ordem alfabética utilizando uma coluna de texto.

![Vários sortimentos](images/Mehrere-Sortierungen.png)
