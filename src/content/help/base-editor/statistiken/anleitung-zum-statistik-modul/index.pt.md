---
title: 'Instruções para o módulo de estatísticas'
date: 2023-02-06
lastmod: '2024-03-18'
categories:
    - 'statistiken-und-datenanalyse'
author: 'vge'
url: '/pt/ajuda/modulo-estatisticas-tutorial-seatable'
aliases:
    - '/pt/ajuda/anleitung-zum-statistik-modul'
seo:
    title: 'Estatísticas e gráficos no módulo SeaTable: tutorial'
    description: 'Visualize seus dados em gráficos no SeaTable: organize dashboards, crie estatística e otimize relatórios com o módulo de análise visual e configurações práticas.'
weight: 1
---

O **módulo de estatísticas** permite-lhe visualizar os dados da sua tabela sob a forma de vários **gráficos** e **diagramas**. Isto é extremamente útil para o seu trabalho no SeaTable: graças aos **painéis de controlo**, tem sempre uma visão geral dos números e da evolução estatística da sua base.

![Módulo de estatísticas](images/erweitertes-statistik-plugin-release-notes.gif)

## Abrir o módulo de estatísticas

O módulo de estatísticas é configurado por defeito em todas as bases. Pode sempre aceder-lhe através do botão "Estatísticas" no **cabeçalho da base**.

![Módulo de estatísticas no cabeçalho de base](images/statistic-plugin-in-base-header.jpg)

## Criar um gráfico

1. Abra o módulo de estatísticas e clique no botão {{< seatable-icon icon="dtable-icon-add-table" >}} **Adicionar gráfico** no canto superior direito.

Tem a opção de escolher entre diferentes **tipos de** gráficos e gráficos. Percorrer a selecção ou clicar nos ícones rotulados na barra de opções para saltar directamente para o local desejado.

![Navegar no módulo de estatísticas.](images/Navigieren-im-Statistik-Plugin-1.png)

2. Seleccione o **tipo** apropriado para as suas estatísticas e clique em **Enviar**.

### Definições de dados

3. Determine de que **tabela** e **vista** o gráfico deve obter os dados.
4. Dependendo do gráfico, pode fazer diferentes **configurações de dados** – para um gráfico de barras, por exemplo, quais os valores que deseja exibir nos **eixos X e Y**.

![Criar um novo gráfico no módulo de estatísticas.](images/Dateneinstellungen.png)

Inicia-se o trabalho detalhado num gráfico de colunas, seleccionando a coluna que deve fornecer os **valores para o eixo X**. Clique no campo pendente correspondente e seleccione a **coluna**. Com um selector pode definir se pretende considerar **linhas vazias** no gráfico.

Depois escolher como os **valores** devem ser exibidos no **eixo Y**. Pode escolher entre o **número de** entradas que têm um determinado valor na coluna seleccionada e a opção de **campo Soma**, onde pode avaliar quer a soma, média, número de valores únicos, máximo ou mínimo em **colunas numéricas**. Para gráficos **agrupados** ou **empilhados**, pode especificar uma coluna de opções pelas quais pretende agrupar.

Todas as alterações de configuração são efectuadas **em tempo real**, ou seja, o diagrama é imediatamente **actualizado** com cada alteração de configuração. Desta forma é possível ver directamente se se atingiu o resultado desejado ou se é necessário reajustar.

### Definições de estilo

5. Dê um **título** ao gráfico. Para o fazer, clique no separador **Estilo do gráfico** e introduza o nome desejado.
6. Se o gráfico escolhido permitir **configurações de estilo**, pode configurar, por exemplo, **títulos dos eixos X e Y**, **cores** ou **etiquetas de dados**.

![Configurações ao adicionar um novo gráfico no módulo de estatísticas.](images/Stileinstellungen.png)

## Gráficos no Painel de instrumentos

7. Depois de fechar a janela de definições, o gráfico guardado aparece no seu **painel de instrumentos**.

Pode criar **vários painéis de instrumentos** e criar quantos gráficos quiser em cada painel. Para alterar a **ordem dos gráficos**, arraste-os **e largue-os** para o local desejado. Para o fazer, mover o ponteiro do rato sobre o **título de** um gráfico até aparecer uma **seta cruzada** e manter premido o **botão** do rato.

![Deslocar os gráficos no módulo de estatísticas.](images/Dashboard_Sortierung_Statistik-Plugin.gif)

## Opções para um gráfico

Quando se move o ponteiro do rato sobre um gráfico, aparece no canto superior direito um **símbolo de seta dupla** {{< seatable-icon icon="dtable-icon-open" >}} e um **símbolo de três pontos** {{< seatable-icon icon="dtable-icon-more-level" >}}. Seleccionar a seta dupla para exibir um gráfico em **modo de ecrã inteiro**. Pode aceder a todas as outras opções através dos três pontos:

- Editar gráfico
- Copiar gráfico
- Exportar como imagem
- Apagar gráfico

![Módulo de estatísticas Opções gráficas](images/Statistik-Plugin-Grafik-Optionen.gif)

## Outras opções de visualização

Se clicar em {{< seatable-icon icon="dtable-icon-full-screen" >}}, pode visualizar toda a janela do módulo de estatísticas em **modo de ecrã inteiro**.

![Modo de ecrã inteiro do módulo de estatísticas](images/Statistik-Plugin-Vollbildmodus.gif)

Pode alternar entre o **modo claro e escuro** usando os ícones {{< seatable-icon icon="dtable-icon-night-mode" >}} e {{< seatable-icon icon="dtable-icon-day-mode" >}}.

![Módulo de estatísticas do modo noturno](images/Statistik-Plugin-dark-mode.png)
