---
title: 'A vista da linha de tempo'
date: 2026-03-31
lastmod: '2026-03-31'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/pt/ajuda/vista-da-linha-de-tempo'
aliases:
    - '/pt/ajuda/guia-plugin-timeline'
    - '/pt/ajuda/anleitung-zum-timeline-plugin'
seo:
    title: 'Vista de linha de tempo: Visualize períodos de tempo no SeaTable'
    description: 'A vista de linha de tempo dá-lhe uma visão geral clara dos períodos de tempo e das suas sobreposições.'
weight: 15
---

A **Vista de linha de tempo** permite-lhe visualizar diferentes períodos de tempo numa **linha temporal**. Isto é muito útil, por exemplo, se quiser visualizar a sequência de processos ou ver se os períodos de tempo se **sobrepõem**. Assim, pode utilizar a vista de linha temporal para [planeamento de férias]({{< relref "templates/human-resources/holiday-request-management" >}}), [planos de projeto]({{< relref "templates/projects/project-plan" >}}) ou a reserva de salas de conferência, entre outras coisas.

![a vista da linha de tempo](images/timeline-view.jpg)

{{< warning type="warning" headline="Requirements" >}}

Este tipo de vista apresenta **intervalos de tempo**. Por conseguinte, necessita de **duas** [colunas de data]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) numa tabela que define o **início** e o **fim** dos períodos de tempo.

{{< /warning >}}

## Para criar uma vista de linha de tempo

1. Clique no **nome da vista atual**.
2. Clique em **Adicionar vista ou pasta** e selecione o **Tipo de vista** pretendido.

![crie uma vista de linha de tempo](images/create-timeline-view.png)

3. Atribua um **nome** à nova vista.
4. Active o cursor se a nova vista não deve ser visível para todos mas **privada**.
5. Confirme com **Submeter**.
6. Em seguida, especifique a **data de início e de fim** nas definições e o **período de tempo** que a linha de tempo deve abranger. A nova vista é então gerada automaticamente.
7. No campo de entrada superior, introduza a coluna da qual depende a **etiquetagem dos blocos**.

![crie uma vista de linha cronológica](images/create-timeline-view.gif)

## Opções de vista

Pode utilizar as seguintes opções numa vista de linha cronológica:
- [Bloquear vista]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrar]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) ou [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) por qualquer valor
- [Cor da linha]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Partilhar a vista com outros]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Imprimir vista]({{< relref "help/base-editor/ansichten/das-drucken-einer-ansicht" >}})

## Opções de visualização

Há um total de 5 opções de exibição para a escala da linha do tempo: **Ano**, **Trimestre**, **Mês**, **Semana** e **Dia**. Pode alternar facilmente entre estas opções. Basta clicar na opção correspondente no **menu suspenso** acima da linha do tempo.

![Opções de visualização da linha de tempo](images/display-options-timeline-view.jpg)

## Mostrar e ocultar informações

Clique em **Mostrar colunas** para mostrar mais ou menos informações, mostrando ou ocultando colunas. Active o **deslizador** das respectivas colunas para apresentar mais informações dos registos de dados na linha cronológica.

![mostre informações de outras colunas na linha de tempo](images/other-fields-shown-in-timeline-view.gif)

## Edite registos de dados na vista da cronologia

Faça duplo clique numa entrada e será aberta uma janela com os **Detalhes da linha**. Faça os ajustes desejados no registo de dados. As alterações são guardadas automaticamente quando fecha a janela.

## Prolongue, reduza ou desloque períodos de tempo

Para prolongar ou encurtar um período de tempo, mantenha premido o botão do rato e arraste **na margem esquerda ou direita de uma entrada**. Se pretender mover um período de tempo, mantenha premido o botão esquerdo do rato e mova a entrada **arrastando e largando** na direção pretendida. Os valores correspondentes nas colunas de datas ajustar-se-ão automaticamente.

![Alterar períodos de tempo na vista de linha de tempo](images/change-records-in-timeline-view.gif)