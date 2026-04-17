---
title: 'O que é uma vista?'
date: 2023-01-13
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/pt/ajuda/o-que-e-uma-visualizacao'
aliases:
    - '/pt/ajuda/was-ist-eine-ansicht'
seo:
    title: 'O que é uma vista no SeaTable?'
    description: 'Saiba o que é uma vista no SeaTable e como personalizar a visualização dos seus dados em tabelas.'
star: true
weight: 1
---

Sempre que visualiza os seus dados numa tabela, visualiza-os através de uma **vista**. Mesmo que tenha criado uma nova tabela, já está a visualizá-la na vista **"Default View"** fornecida como padrão.

## Para que são utilizadas as vistas?

Numa tabela convencional, vê sempre os dados da mesma forma. Embora possa adicionar ou eliminar linhas e colunas, não pode ver os mesmos dados de ângulos diferentes.

No SeaTable, pode criar vistas e utilizar **filtros, ordenação, agrupamento, ocultação, realce de cores e altura da linha** para determinar que secção dos seus dados pretende visualizar e como. Isto permite-lhe apresentar exatamente os dados que são relevantes para si, sem ter de alterar ou eliminar registos de dados.

Também pode selecionar determinados formatos de visualização para visualizar os dados de uma forma apelativa. Eis alguns exemplos de **tipos de vistas** que pode criar:

![Tipos de vista](images/create-table-view.jpg)

- Vista de tabela
- Vista Kanban
- Vista de calendário
- Vista de galeria
- Vista de linha do tempo
- Vista de árvore
- Vista de Big Data

É importante compreender que uma vista é apenas outra forma de ver **os mesmos dados subjacentes**! Isto significa que se editar os dados de uma tabela numa vista, esses dados são alterados em todas as vistas da tabela, uma vez que todas as vistas representam o mesmo conjunto de dados.

{{< warning type="warning" headline="Note" >}}

Pode utilizar outros formatos de visualização, como organogramas ou mapas, sob a forma de [plugins]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}}).

{{< /warning >}}

## A vista de tabela

A **vista de tabela** é o formato de visualização padrão num SeaTable Base. É muito semelhante a uma folha de cálculo, uma vez que os registos de dados estão organizados em linhas e colunas.

![Vista de tabela](images/table-view.jpg)

Se criar uma vista filtrada ou ocultar colunas, verá apenas a quantidade de dados de que necessita. Também pode organizar a vista de forma mais clara, ordenando ou agrupando de acordo com determinados princípios de ordenação.

## A vista Kanban

Se tiver **colunas com um número limitado de opções** na sua tabela, pode resumir as suas linhas em grupos. Uma forma especial de exibição é a **vista Kanban**. Ela é particularmente adequada para visualizar **processos com diferentes fases**.

![a vista Kanban](images/kanban-view.jpg)

Pode obter mais informações sobre este assunto no artigo sobre a [vista Kanban]({{< relref "help/base-editor/ansichten/die-kanban-ansicht" >}}).

## A vista de calendário

Se tiver uma tabela com **colunas de data**, pode criar uma vista de calendário que organiza todos os seus registos de dados **cronologicamente**.

![A vista de calendário](images/calendar-view.jpg)

Pode obter mais informações sobre este assunto no artigo sobre a [vista de calendário]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}).

## A vista de galeria

Se tiver uma tabela com uma coluna de **imagem**, pode criar uma vista de galeria para ilustrar os registos de dados com imagens de pré-visualização.

![A vista de galeria](images/gallery-view.jpg)

Pode obter mais informações sobre este assunto no artigo sobre a [vista de galeria]({{< relref "help/base-editor/ansichten/die-galerie-ansicht" >}}).

## A vista de linha do tempo

Se tiver uma tabela com **duas colunas de data**, pode criar uma vista de linha do tempo que visualiza vários períodos de tempo numa **linha cronológica**. É particularmente adequada para representar a sequência de processos ou verificar se os períodos de tempo **se sobrepõem** – por exemplo no planeamento de férias, planos de projeto ou reserva de salas.

![A vista de linha do tempo](images/timeline-view.jpg)

Pode obter mais informações sobre este assunto no artigo sobre a [vista de linha do tempo]({{< relref "help/base-editor/ansichten/die-zeitleisten-ansicht" >}}).

## A vista de árvore

Se tiver uma base com **pelo menos duas tabelas ligadas**, pode criar uma vista de árvore para apresentar registos ligados de forma **hierárquica**. É particularmente adequada para visualizar estruturas complexas como portfólios de projetos ou hierarquias organizacionais – com até três níveis no diagrama de árvore.

![A vista de árvore](images/tree-view.jpg)

Pode obter mais informações sobre este assunto no artigo sobre a [vista de árvore]({{< relref "help/base-editor/ansichten/die-baum-ansicht" >}}).

## A vista de Big Data

Se tiver ativado o **Armazenamento de Big Data** na sua Base, pode arquivar **grandes quantidades de dados** que não são imediatamente visíveis para todos os utilizadores. É necessária uma vista especial de Big Data para aceder aos dados no armazenamento de Big Data.

![a vista de Big Data](images/create-big-data-view.jpg)

Pode obter mais informações sobre este assunto no artigo sobre a [vista de Big Data]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}).

## Mais artigos sobre o tema de vistas

- [Criar uma nova vista]({{< relref "help/base-editor/ansichten/anlegen-einer-neuen-ansicht" >}})
- [Renomear uma vista]({{< relref "help/base-editor/ansichten/umbenennen-einer-ansicht" >}})
- [Apagar uma vista]({{< relref "help/base-editor/ansichten/loeschen-einer-ansicht" >}})
- [Duplicação de vistas]({{< relref "help/base-editor/ansichten/das-duplizieren-von-ansichten" >}})
- [Diferenças entre vistas privadas e normais]({{< relref "help/base-editor/ansichten/unterschiede-zwischen-privaten-und-normalen-ansichten" >}})
- [Imprimir uma vista]({{< relref "help/base-editor/ansichten/das-drucken-einer-ansicht" >}})
- [Alterar a ordem de vistas]({{< relref "help/base-editor/ansichten/die-reihenfolge-von-ansichten-aendern" >}})
- [Agrupar vistas em pastas]({{< relref "help/base-editor/ansichten/ansichten-in-ordnern-gruppieren" >}})
- [Filtragem de entradas numa vista]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}})
- [Ligação das regras de filtragem com AND e OR]({{< relref "help/base-editor/ansichten/filter-regeln-mit-und-und-oder-verknuepfen" >}})
- [Ordenar as entradas numa vista]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})
- [Agrupar entradas numa vista]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}})
- [Colorir células]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}})
- [Marcação a cores das células]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Ajustar a altura da fila]({{< relref "help/base-editor/ansichten/zeilenhoehe-anpassen" >}})
- [Ajustar o número de colunas fixas]({{< relref "help/base-editor/spalten/anzahl-der-fixierten-spalten-anpassen" >}})
- [Esconder e mover colunas]({{< relref "help/base-editor/ansichten/ausblenden-und-verschieben-von-spalten" >}})
- [Bloquear uma vista]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Partilhar uma vista com um membro da equipa]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Criar uma ligação externa para uma vista]({{< relref "help/startseite/freigaben/externen-link-fuer-eine-ansicht-erstellen" >}})
