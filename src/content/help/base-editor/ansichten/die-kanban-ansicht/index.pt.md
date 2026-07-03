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

Uma **vista Kanban** está predestinada a visualizar processos dinâmicos com diferentes fases. A este respeito, permite-lhe visualizar **fluxos de trabalho** e **progresso do projeto**, por exemplo. É particularmente útil para [planeamento de projectos]({{< relref "templates/projects/project-plan" >}}), [desenvolvimento de software]({{< relref "templates/software-development/bug-tracker" >}}) ou distribuição de tarefas dentro de uma equipa.

{{< warning type="warning" headline="Requisitos" >}}

Para poder utilizar a vista Kanban de uma forma significativa, precisa de pelo menos uma coluna na sua tabela que permita que as opções sejam claramente atribuídas. Os tipos de coluna [Seleção única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) ou [Colaborador]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) são adequados para este efeito.

{{< /warning >}}

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

![criar uma vista Kanban](images/kanban-view-settings.jpg)

6. Especifique a coluna que pretende utilizar para o **agrupamento**, ou seja, a definição das colunas. A visão Kanban é então gerada automaticamente.
7. No campo **Título**, entrar a coluna com a qual deseja rotular os cartões Kanban.
8. Opcionalmente, também pode ativar os **controladores** para ativar determinadas funções ou exibir mais colunas.

Se pretender alterar algo mais tarde, clique no ícone **roda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} no canto superior direito e ajuste as **configurações**.

## Definições da vista Kanban

Pode utilizar as opções do cursor para alterar a apresentação visual da vista Kanban.

- Pode utilizar o seletor **Não mostrar valores vazios** para remover os espaços reservados a cinzento nos cartões Kanban.
- O seletor **Mostrar nomes das colunas** mostra os nomes das colunas acima de todas as informações activadas.
- O seletor **Texto embrulhado** formata os textos de modo a que fiquem totalmente legíveis nos cartões de quadro Kanban.

![definições da vista Kanban](images/show-other-fields-in-kanban-view.gif)

## Mostrar e ocultar outras colunas

Todas as **colunas** que criou na sua tabela estão listadas na secção inferior. Ao ativar os **controladores** individuais, as entradas nas respectivas colunas tornam-se visíveis como notas informativas nos cartões.

{{< warning  headline="Sugestão"  text="Abra os **detalhes da linha** clicando num cartão para ver toda a informação de uma linha, mesmo que os cursores não estejam activados." />}}

## Opções de vista

Pode utilizar as seguintes opções numa vista Kanban:
- [Bloquear vista]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrar]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) ou [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) por qualquer valor
- [Partilhar a vista com outros]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})

## Adicionar um novo registo na vista Kanban

![Adicionar um novo registo na visualização Kanban](images/add-record-in-kanban-view.jpg)

Clique em **Adicionar linha** na parte inferior de uma coluna. Abre-se uma nova janela. Crie um novo registo de dados em **Detalhes da linha** e introduza as informações necessárias. As alterações são guardadas automaticamente quando fecha a janela.

## Editar registos de dados na vista Kanban

Clique num **cartão Kanban** e abre-se uma janela com os **Detalhes da linha**. Faça os ajustes desejados no registo de dados. As alterações são automaticamente guardadas quando fecha a janela.
