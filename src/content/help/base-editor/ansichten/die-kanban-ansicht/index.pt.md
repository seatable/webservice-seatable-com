---
title: 'A vista Kanban'
date: 2025-12-03
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/pt/ajuda/a-vista-kanban'
aliases:
    - '/pt/ajuda/guia-plugin-kanban'
    - '/pt/ajuda/anleitung-zum-kanban-plugin'
seo:
    title: 'Criar e utilizar a vista Kanban no SeaTable'
    description: "Aprenda a configurar a visualização Kanban no SeaTable e a utilizá-la de forma optimizada para a visualização de processos"
weight: 14
---

Uma **vista Kanban** está predestinada a visualizar processos dinâmicos com diferentes fases. A este respeito, permite-lhe visualizar **fluxos de trabalho** e **progresso do projeto**, por exemplo. É particularmente útil para [planeamento de projectos]({{< relref "templates/projects/project-plan" >}}), [desenvolvimento de software]({{< relref "templates/it-engineering/bug-tracker" >}}) ou distribuição de tarefas dentro de uma equipa.

{{< warning type="warning" headline="Requisitos" >}}

Para poder utilizar a vista Kanban de uma forma significativa, precisa de pelo menos uma coluna na sua tabela que permita que as opções sejam claramente atribuídas. Os tipos de coluna [Seleção única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) ou [Colaborador]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) são adequados para este efeito.

{{< /warning >}}

**Neste vídeo tutorial, vamos mostrar-lhe, em apenas alguns minutos, como criar uma visualização Kanban no SeaTable (com legendas em português).**
{{< youtube C19DWHZzTbg >}}

## Estrutura de uma vista Kanban

Uma vista Kanban é constituída por **pilares** que representam diferentes passos ou fases de um processo. Num fluxo de trabalho, por exemplo, estes podem ser "ideia", "planeado", "em curso" e "concluído".

![Vista Kanban](images/kanban-view.jpg)

As colunas são rotuladas com **cartões móveis**, que pode mover tanto dentro de uma coluna como de uma coluna para a outra. Um cartão Kanban pode representar um pacote de trabalho ou uma tarefa, por exemplo.

![movimentos Kanban](images/move-records-in-kanban-view.gif)

## Como criar uma vista Kanban

![Criar uma vista Kanban](images/create-kanban-view.jpg)

1. Clique no **nome da vista atual**.
2. Clique em **Adicionar vista ou pasta** e selecione o **tipo de vista** pretendido.

![dê um nome a uma vista Kanban](images/name-kanban-view.jpg)

3. Atribua um **nome** à nova vista.
4. Active o cursor se a nova vista não deve ser visível para todos mas **privada**.
5. Confirme com **Submeter**.

![Agrupar uma vista Kanban](images/group-kanban-view.jpg)

6. Clique em **Adicionar Agrupamento** e especifique a **coluna** que pretende utilizar para o agrupamento, ou seja, a definição das colunas. A vista Kanban é então gerada automaticamente.

![Configurar uma vista Kanban](images/kanban-view-settings.jpg)

7. Vá às **configurações** e indique no campo **Título** a coluna com a qual deseja rotular os cartões Kanban.
8. Opcionalmente, também pode ativar os **controladores** para ativar determinadas funções.

Se pretender alterar algo mais tarde, clique no ícone **roda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} no canto superior direito e ajuste as configurações.

## Definições da vista Kanban

Pode utilizar as opções do cursor para alterar a apresentação visual da vista Kanban.

- Pode utilizar o seletor **Não mostrar valores vazios** para remover os espaços reservados a cinzento nos cartões Kanban.
- O seletor **Mostrar nomes das colunas** mostra os nomes das colunas acima de todas as informações activadas.
- O seletor **Texto embrulhado** formata os textos de modo a que fiquem totalmente legíveis nos cartões de quadro Kanban.

![definições da vista Kanban](images/show-other-fields-in-kanban-view.gif)

## Opções de vista

Pode utilizar as seguintes opções numa vista Kanban:
- [Bloquear vista]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrar]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) ou [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) por qualquer valor
- [Agrupar]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}) por apenas uma coluna
- [Ocultar colunas]({{< relref "help/base-editor/ansichten/ausblenden-und-verschieben-von-spalten" >}})
- [Partilhar a vista com outros]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})

## Mostrar e ocultar outras colunas

![Ocultar colunas na vista Kanban](images/hide-columns-in-kanban-view.jpg) 

Se pretender mostrar menos informação nos cartões, clique em **Ocultar** e desative os **controladores** das respectivas colunas. Ao reativar os controladores, as entradas dessas colunas voltam a ficar visíveis nos cartões.

{{< warning  headline="Nota"  text="Se os controladores **não estiverem ativados**, também não poderá ver nem editar os valores das colunas ocultas ao abrir os **detalhes da linha**." />}}

## Adicionar um novo registo na vista Kanban

![Adicionar um novo registo na visualização Kanban](images/add-record-in-kanban-view.jpg)

Clique em **Adicionar linha** na parte inferior de uma coluna. Abre-se uma nova janela. Crie um novo registo de dados em **Detalhes da linha** e introduza as informações necessárias. As alterações são guardadas automaticamente quando fecha a janela.

## Editar registos de dados na vista Kanban

Clique num **cartão Kanban** e abre-se uma janela com os **Detalhes da linha**. Faça os ajustes desejados no registo de dados. As alterações são automaticamente guardadas quando fecha a janela.
