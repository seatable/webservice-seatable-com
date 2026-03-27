---
title: 'Introdução ao trabalho com bases e mesas'
date: 2023-01-07
lastmod: '2023-03-24'
categories:
    - 'seatable-nutzen'
author: 'cdb'
url: '/pt/ajuda/guia-bases-tabelas-seatable'
aliases:
    - '/pt/ajuda/einfuehrung-in-die-arbeit-mit-bases-und-tabellen'
seo:
    title: 'Guia para Bases e Tabelas no SeaTable – primeiros passos'
    description: 'Saiba como usar Bases e Tabelas no SeaTable: Estrutura, vínculos, tipos de coluna e visualizações para organizar projetos e processos.'
---

Cada um dos ícones quadrados na sua página inicial representa uma **base**. É uma base de dados, comparável a uma pasta de trabalho numa folha de cálculo convencional e pode conter várias **tabelas** sobre diferentes tópicos.

![Vista geral da base em SeaTable](images/base-overview.png)

Uma Base representa uma **unidade** autónoma em SeaTable. Por conseguinte, deve conter toda a informação necessária para um projecto ou processo específico.

Por exemplo, a base do seu pipeline de vendas pode conter tabelas separadas para leads, empresas e oportunidades de negócio. Da mesma forma, pode utilizar uma base para planear um casamento e depois criar mesas separadas para potenciais locais, participantes e listas de afazeres.

## Criar uma nova base

A SeaTable oferece várias formas de criar uma nova base. Se é novo no SeaTable, recomendamos que comece com um **modelo** para que possa ver como uma Base é normalmente construída. Pode escolher um modelo existente adaptado ao seu caso de utilização na nossa galeria de modelos e depois adaptá-lo facilmente às suas próprias necessidades.

Se estiver familiarizado com a criação das suas próprias tabelas, colunas e vistas, pode começar com uma base vazia.

- [Criação de uma base utilizando um modelo]({{< relref "help/startseite/bases/anlegen-einer-base-mithilfe-einer-vorlage" >}})
- [Criar uma nova base]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [Importar ficheiros Excel para o SeaTable]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}})
- [Duplicar uma base existente]({{< relref "help/startseite/bases/duplizieren-einer-bestehenden-base" >}})

## Gerir bases

Depois de ter dominado com sucesso os primeiros passos e criado as suas primeiras bases, pode descobrir toda uma série de outras funções na página inicial e nas suas bases. Tudo o que precisa de saber sobre a gestão das suas bases pode ser encontrado no capítulo [Bases]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}).

## Tabelas e vistas numa base

A tabela é o nível mais importante em que pode organizar os seus dados em SeaTable, comparável a uma folha de cálculo numa folha de cálculo. Basicamente, **as tabelas** são o nível seguinte abaixo das bases na estrutura organizacional do SeaTable.

Uma vez que SeaTable é uma [base de dados relacional]({{< relref "posts/relationale-datenbank" >}}), é possível ligar informações em diferentes tabelas de uma base através de [ligações]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}), [automatizações]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}}) e outras funções.

Uma tabela é constituída por linhas e colunas. Todas as entradas numa **linha** formam um **conjunto de dados** coerente. Os [tipos de coluna]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) no SeaTable definem quais os **tipos de dados** que pode introduzir numa **coluna**.

Sempre que visualiza os seus dados numa tabela, visualiza-os através de uma [vista]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}). As vistas dão-lhe inúmeras opções para exibir os dados nas suas tabelas de forma diferente – para filtrar, ordenar, agrupar, esconder, etc.
