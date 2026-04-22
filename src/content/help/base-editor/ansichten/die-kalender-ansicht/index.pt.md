---
title: 'A vista do calendário'
date: 2025-12-03
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/pt/ajuda/vista-do-calendario'
aliases:
    - '/pt/ajuda/anleitung-zum-kalender-plugin'
    - '/pt/ajuda/varios-calendarios-base-seatable'
    - '/pt/ajuda/mehrere-kalender-fuer-eine-base-anlegen'
    - '/pt/ajuda/criar-entradas-plugin-calendario-seatable'
    - '/pt/ajuda/neue-kalendereintraege-im-kalender-plugin-anlegen'
seo:
    title: 'Vista do calendário no SeaTable – utilize a vista cronológica'
    description: 'A vista do calendário no SeaTable apresenta os seus compromissos por ano, mês, semana, dia ou na agenda. Configuração completa e sugestões'
weight: 13
---

A vista de calendário mostra-lhe os dados de uma tabela sob a forma de **calendário**. Pode obter uma visão geral de **diferentes períodos de tempo (ano, mês, semana, dia)** ou apresentar compromissos como **agenda** em forma de lista.

Um exemplo é a visão geral mensal num calendário de férias:

![A vista do calendário](images/calendar-view.jpg)

{{< warning type="warning" headline="Requisitos" >}}

Para poder utilizar a vista de calendário de forma sensata, necessita de pelo menos uma [coluna de data]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) na sua tabela.

{{< /warning >}}

## Para criar uma vista de calendário

![Crie uma vista de calendário](images/create-calendar-view.jpg)

1. Clique no **nome da vista atual**.
2. Clique em **Adicionar vista ou pasta** e selecione o **tipo de vista** pretendido.

![Dê um nome a uma vista de calendário](images/name-calendar-view.jpg)

3. Dê um **nome** à nova vista.
4. Active o seletor se a nova vista não deve ser visível para todos mas **privada**.
5. Confirme com **Submeter**.

![criar uma vista de calendário](images/calendar-view-settings.jpg)

6. No campo **Título**, introduza a coluna com a qual gostaria de rotular as entradas do calendário.
7. Especifique qual a coluna de data que deve ser utilizada para a **Data de início**. A vista de calendário é então gerada automaticamente.
8. Opcionalmente, pode especificar uma coluna de data ou de duração para a **Data final**, que define o período das entradas de calendário.
9. Finalmente, selecione o dia da semana que deve ser utilizado como **primeiro dia da semana**.

Se pretender alterar algo mais tarde, clique no ícone da **roda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} no canto superior direito e ajuste as **configurações**.

## Opções da vista

Pode utilizar as seguintes opções numa vista de calendário:
- [Bloquear vista]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrar]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) ou [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) por qualquer valor
- [Cor da linha]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Partilhar a vista com outros]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Imprimir vista]({{< relref "help/base-editor/ansichten/das-drucken-einer-ansicht" >}})

## As opções de visualização em pormenor

Há um total de 5 opções de visualização: Pode apresentar os compromissos num calendário **anual**, **mensal** ou **semanal**, na **planeador diário** ou como **agenda** em forma de lista.

Pode alternar facilmente entre as cinco opções de visualização da vista de calendário. Basta clicar na opção correspondente no **botão** acima do calendário.

![Opções de visualização da vista de calendário](images/display-options-calendar-view.png)

### Visão geral do ano

Aqui pode ver o **ano** num relance. O **ponto** por baixo de uma data mostra-lhe que existe uma entrada para esse dia. Também tem a opção de clicar na data para aceder aos **detalhes da linha**.

![visão geral do ano na vista de calendário](images/year-overview-calendar-view.png)

### Visão geral mensal

Nesta vista, tem uma visão geral de todos os dias de um **mês**. Também pode chamar os **detalhes da linha** aqui, clicando numa das entradas do calendário.

### Visão geral semanal

Esta visualização mostra-lhe as **horas** no eixo vertical e os sete dias de uma **semana** da esquerda para a direita. Também pode abrir os **detalhes da linha** aqui, clicando numa das datas.

### Planeador diário

O planeador diário é particularmente adequado se pretender ter vários compromissos num **dia** no ecrã. Tal como a vista geral semanal, mostra-lhe as **horas** no eixo vertical. Também pode abrir os **detalhes da linha** aqui, clicando num dos compromissos.

### Visualização da agenda

A **Agenda** lista todos os compromissos dentro de um **mês** e oferece-lhe a opção de visualizar certas **informações** sobre os compromissos num relance.

Para o fazer, basta apresentar as **colunas** da tabela pretendidas nas **configurações** da vista de calendário - por exemplo, tópico, estado e tipo de publicação.

![Agenda na vista de calendário](images/calendar-view-agenda.jpg)

## Adicione um novo registo de dados na vista de calendário

Para adicionar **novos registos** na vista de calendário, tem várias opções.

### 1. Através do símbolo de mais

![Adicionar um novo registo na vista de calendário](images/add-new-record-in-calendar-view.jpg)

Clique no **círculo cor de laranja com o símbolo de mais** no canto inferior direito. Abrir-se-á uma nova janela. Crie um novo registo de dados em **detalhes da linha** e introduza os dados pretendidos. As alterações são automaticamente guardadas quando fecha a janela.

{{< warning type="warning" headline="Nota" text="Esta função está disponível para **todas** as opções de visualização no calendário." />}}

### 2. Através de um campo do calendário

![crie uma nova entrada de calendário na vista de calendário](images/add-record-in-monthly-calendar-view.jpg)

Mova o ponteiro do rato sobre um **campo** no calendário e clique no símbolo **Mais** que aparece no canto superior direito. Crie um novo registo de dados nos **detalhes da linha** e introduza os dados pretendidos. As alterações são guardadas automaticamente quando fecha a janela.

{{< warning type="warning" headline="Nota" text="Esta função só existe para as opções de visualização **mês** e **semana**." />}}

### 3. Duplo clique

Se fizer um **clique duplo** numa posição do calendário, os **detalhes da linha** também se abrem. Caso contrário, crie a entrada da mesma forma que com as outras opções.

{{< warning type="warning" headline="Nota" text="O duplo clique só funciona com as opções de visualização **mês**, **semana** e **dia**." />}}

### 4. Puxar marcações para baixo

Para esta função, precisa de **duas colunas de datas** que possam registar **horas**.

1. Crie duas colunas de data para a **hora de início e de fim** e active a opção **precisa ao minuto** em cada caso.
2. Abra a **vista do calendário** e selecione a **visão geral semanal ou diária**.
3. Nas **Configurações** (acessíveis através do ícone de roda dentada {{< seatable-icon icon="dtable-icon-set-up" >}}), selecione as duas colunas de datas para o calendário.
4. No calendário, clique na hora em que o compromisso deve começar, mantenha premido o **botão esquerdo do rato** e arraste a caixa para a hora em que o compromisso deve terminar.

![puxe para baixo os compromissos na vista geral semanal e diária](images/add-record-in-weekly-calendar-view.gif)

{{< warning type="warning" headline="Nota" text="Só pode adicionar marcações na **visão geral semanal ou diária**." />}}

## Mover marcações utilizando a função arrastar e largar

Pode mover facilmente as entradas na vista de calendário **arrastando e largando**. Isto altera automaticamente os valores correspondentes nas colunas de datas da sua tabela. Esta função está disponível para a visão geral **mensal**, **semanal** e **diária**.

![Mover entradas de calendário](images/move-record-in-weekly-calendar-view.gif)
