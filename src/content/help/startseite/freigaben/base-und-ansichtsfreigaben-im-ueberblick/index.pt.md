---
title: 'Partilhar bases e vistas'
date: 2023-01-13
lastmod: '2023-02-22'
categories:
    - 'freigaben'
author: 'cdb'
url: '/pt/ajuda/compartilhar-base-visualizacao'
aliases:
    - '/pt/ajuda/base-und-ansichtsfreigaben-im-ueberblick'
seo:
    title: 'Compartilhar bases e vistas em SeaTable: tipos, permissões e gestão'
    description: 'Veja como usar todas as opções de compartilhamento no SeaTable, dar direitos individuais e administrar acessos de forma detalhada por base, tabela ou visualização.'
star: true
weight: 1
---

Organizou a sua informação numa **base**, **tabela** ou **vista** e quer **partilhá-la** com outros ou trabalhar nela em conjunto? No SeaTable, isto é feito de forma fácil e rápida com uma **partilha**. Desta forma, pode conceder acesso aos seus dados a um único **utilizador**, a um **grupo** ou a **pessoas externas**.

Neste artigo de explicação e panorâmica, aprenderá sobre as **opções de partilha** disponíveis no SeaTable e como utilizá-las eficazmente para colaborar com outros.

## Permissões para partilhas

No SeaTable, tem a opção de dar a **pessoas ou grupos específicos** acesso a bases, tabelas e vistas para trabalharem com os dados em conjunto. Embora isto tenha muitas vantagens para o **trabalho em equipa**, pode haver **informação confidencial** a que não quer que todos os membros da equipa tenham acesso.

É por isso que o SeaTable lhe permite definir permissões por níveis em cada partilha. Ao especificar se deve ser uma partilha **apenas de leitura**, uma partilha de **leitura e escrita** ou uma [partilha personalizada]({{< relref "help/startseite/freigaben/benutzerdefinierte-freigabe-erstellen" >}}), mantém o controlo total sobre quem **está** **autorizado** a fazer o quê na sua base, tabela ou vista. Isto significa, claro, que também tem a capacidade de **alterar** e **revogar** as permissões.

## Funcionalidade e tipos de partilhas

Com uma partilha, concede a outras pessoas **acesso a** uma base, tabela ou vista. Os utilizadores autorizados verão a partilha como uma base separada na página inicial, com o utilizador que partilha também mencionado. Dependendo do tipo de partilha, os outros utilizadores só podem ver ou também editar os seus dados.

A partilha pode ser feita ao nível de uma **base** ou de uma **visão**. Se partilhar uma opinião, o utilizador autorizado só tem acesso aos dados nessa opinião. As linhas e colunas que estão ocultas pelas definições da vista, bem como outras tabelas na base, permanecem ocultas ao utilizador.

A cada partilha - seja para uma base, tabela ou vista - é dado um nível de permissão. As duas permissões básicas são **apenas de leitura** e partilha **com** permissões de **leitura e escrita**.

- **Partilha com direitos de leitura**: As permissões de leitura permitem aos utilizadores visualizar tabelas e dados e alterar configurações de visualização, tais como filtros e agrupamentos. No entanto, os utilizadores não podem fazer alterações a tabelas e dados com esta permissão.
- **Partilha com direitos de leitura e escrita**: Em caso de partilha com direitos de leitura e escrita, os utilizadores autorizados podem fazer alterações às tabelas e dados, mas não podem instalar plug-ins ou partilhar a base ou a vista com outras pessoas ou grupos.

Para lhe dar ainda mais opções ao partilhar uma base do que no caso das duas permissões básicas, o SeaTable também oferece [permissões de partilha definidas pelo utilizador]({{< relref "help/startseite/freigaben/benutzerdefinierte-freigabe-erstellen" >}}) para bases. Com uma permissão de partilha personalizada, pode **partilhar** **várias tabelas e vistas** numa base ao mesmo tempo, incluindo diferentes níveis de permissão.

Cada partilha, independentemente da autorização atribuída, pode ser **terminada** a qualquer momento pelo proprietário ou por um administrador.

## Partilhas para Bases

A Partilha de uma base pode ser feita a diferentes grupos de pessoas:

- [Partilha para utilizadores]({{< relref "help/startseite/freigaben/anlegen-einer-benutzerfreigabe" >}})
- [Partilha para grupo]({{< relref "help/startseite/freigaben/eine-base-an-eine-gruppe-freigeben" >}})
- [Partilha através de link de convite]({{< relref "help/startseite/freigaben/einladungs-link-erklaert" >}})
- [Partilha através de ligação externa]({{< relref "help/startseite/freigaben/externer-link-erklaert" >}})

Ao partilhar com um utilizador ou grupo, partilha a base **dentro da sua equipa**. O link de partilha por convite permite-lhe dar acesso a uma base a pessoas **fora da sua equipa** (mas dentro da SeaTable). Com a ligação externa, partilha bases ou opiniões externamente, independentemente de alguém ter ou não uma conta SeaTable.

Todas estas partilhas são feitas através do **diálogo de** **partilha** - uma janela a que se pode aceder através do **ícone de partilha** {{< seatable-icon icon="dtable-icon-share" >}} nas opções de base ou através da página **inicial do** SeaTable. Mova o ponteiro do rato para a **base** que pretende partilhar e clique nos **três pontos** que aparecem à direita. Pode então abrir o diálogo de partilha clicando em **Partilhar**.

## Gerir partilhas de base

A administração das suas partilhas de base é feita da mesma forma que a sua criação através do diálogo de partilhas. As partilhas ou links existentes são aí exibidos sob as respectivas opções de partilha.

Uma Partilha existente para um utilizador ou grupo pode ser prolongada ou restringida em qualquer altura através da alteração da autorização de Partilha. Para o fazer, clicar no **ícone do lápis** {{< seatable-icon icon="dtable-icon-rename" >}}. Clicar no **símbolo x** para terminar uma partilha ou apagar uma ligação. Todas as alterações entram em vigor imediatamente. A protecção da palavra-passe, data de expiração e URL **não podem** ser alterados para uma ligação existente.

> Pode também obter uma visão global de todos os partilhas e ligações a uma base sob [Bases na administração da equipa]({{< relref "help/teamverwaltung/bases/bases-in-der-teamverwaltung" >}}), desde que seja um administrador de equipa.

## Partilhas para tabelas

Se não quiser [partilhar]({{< relref "help/startseite/freigaben/einzelne-tabellenblaetter-einer-base-freigeben" >}}) uma base inteira, mas apenas [tabelas individuais]({{< relref "help/startseite/freigaben/einzelne-tabellenblaetter-einer-base-freigeben" >}}), isto também é naturalmente possível. A [partilha personalizada]({{< relref "help/startseite/freigaben/benutzerdefinierte-freigabe-erstellen" >}}) permite-lhe partilhar várias tabelas e opiniões de uma só vez e enviá-las a membros de equipas ou grupos inteiros.

## Partilhas para vistas

Cria-se a partilha de um ponto de vista na tabela aberta. Quando estiver na vista a ser partilhada, clique no **ícone de partilha** {{< seatable-icon icon="dtable-icon-share" >}} nas opções de vista. Não confunda isto com o ícone de partilha de Base.

![Partilha de ícones numa base](images/share-icons-new-1.png)

Aterra então no **diálogo** familiar de partilha, onde também pode criar as suas partilhas de pontos de vista da mesma forma que para as bases. Um ponto de vista pode ser partilhado com três grupos de pessoas:

- [Partilha a um membro da equipa]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Partilha para um grupo]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-eine-gruppe" >}})
- [Partilha através de ligação externa]({{< relref "help/startseite/freigaben/externen-link-fuer-eine-ansicht-erstellen" >}})

Assim que clicar no botão **Submeter** para uma opção de partilha, a pessoa ou grupo seleccionado pode aceder à vista com a permissão concedida. Para partilhar uma vista com vários utilizadores ou grupos, repita este processo.

Tal como nas bases, é possível criar uma **ligação externa** para partilhar publicamente a visão. A visão partilhada é sempre apresentada a utilizadores autorizados como **base** na página **inicial**.
