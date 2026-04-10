---
title: 'A Coluna do Colaborador'
date: 2023-01-07
lastmod: '2024-02-14'
categories:
    - 'datum-dauer-und-personen'
author: 'ssc'
url: '/pt/ajuda/coluna-colaboradores-seatable'
aliases:
    - '/pt/ajuda/die-spalte-mitarbeiter'
seo:
    title: 'Coluna de colaboradores no SeaTable: atribuição, avisos e automações'
    description: 'Coluna de colaborador SeaTable: atribua tarefas, ative notificações e use de forma flexível para filtros e automações.'
---

Na **coluna do colaborador**, pode atribuir uma ou mais **pessoas** a uma linha. O SeaTable permite-lhe selecionar as pessoas que têm atualmente **acesso** à **base**, bem como todos os outros membros da equipa sem acesso.

![A coluna de pessoal em SeaTable](images/employee-column.png)

## Selecionar as pessoas com acesso à base

Se fizer **duplo clique** numa célula de uma coluna de colaboradores, aparece uma lista com todos os utilizadores que têm atualmente acesso à base. Seleccione uma ou mais destas **pessoas**. Também é possível utilizar o **campo de pesquisa** para encontrar um utilizador específico.

![Selecionar pessoas com acesso a uma base na coluna do colaborador](images/Personen-mit-Zugriff-auf-eine-Base-in-der-Mitarbeiter-Spalte-auswaehlen.png)

{{< warning  headline="Nota"  text="Se o acesso de um colaborador a uma base for **retirado**, mas ele for introduzido numa coluna de colaboradores, o valor permanece na coluna até ser eliminado manualmente. Após a eliminação, o colaborador deixa de estar disponível para seleção na lista." />}}

## Selecionar membros da equipa sem acesso à base

Se não conseguir encontrar um utilizador através do campo de pesquisa na coluna do colaborador, ele **não** tem atualmente **acesso** à base. No entanto, se for um **membro da sua equipa**, pode introduzi-lo na coluna do colaborador.

Clique no ícone {{< seatable-icon icon="dtable-icon-add\_members" >}} para adicionar membros da equipa sem acesso. Introduza o nome do utilizador no **campo de pesquisa**, seleccione o **membro da equipa** pretendido e confirme com **Adicionar**.

![Introduzir os membros da equipa sem acesso a uma base na coluna do colaborador](images/Teammitglieder-ohne-Zugriff-auf-eine-Base-in-die-Mitarbeiter-Spalte-eintragen.gif)

## Notificação do trabalhador ao acrescentar

Ao criar uma coluna de colaboradores, é possível **ativar** a **barra deslizante** para que os colaboradores recebam uma [notificação]({{< relref "help/startseite/benachrichtigungen/sinn-und-zweck-von-benachrichtigungen-in-seatable" >}}) quando outros os introduzem na coluna e, assim, os atribuem a uma linha.

![Habilitar notificações aos membros do pessoal acrescentadas a uma coluna de pessoal.](images/turn-on-notification-for-collaborateur-1.png)

Os colaboradores recebem então uma notificação correspondente no Base, à qual podem aceder através do **símbolo de sino** {{< seatable-icon icon="dtable-icon-notice" >}} no canto superior direito.

![Notificação quando um colaborador é adicionado](images/Benachrichtigung-wenn-Mitarbeiter-hinzugefuegt-wird.png)

## Definir valor por defeito

É possível definir um ou mais colaboradores como o [valor padrão]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) numa coluna de colaboradores. As opções **Usuário atual** ou **Usuários específicos** estão disponíveis para seleção. Sempre que alguém adiciona uma nova linha à tabela, o criador da linha ou as pessoas seleccionadas são automaticamente introduzidas na coluna de colaboradores.

![Definir valores predefinidos em colunas de colaboradores](images/Set-default-values-in-collaborator-columns.png)

## Selecionar colaboradores como destinatários de notificações automáticas

Ao enviar notificações através de [automatismos]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}), é possível selecionar todas as pessoas introduzidas na coluna do colaborador como destinatários da mensagem.

![Coluna do colaborador para notificações automáticas](images/Collaborator-column-for-automated-notifications.gif)

## A coluna do colaborador em aplicações

A coluna do colaborador é também uma vantagem na [aplicação]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}). Pode ativar a opção para que os membros da equipa sejam visíveis para todos os utilizadores na lista pendente nas [definições]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}}) da aplicação.

Se não quiser que os utilizadores da aplicação possam ver os registos de dados de outros utilizadores, defina **filtros predefinidos**: Se uma página for filtrada pela coluna do colaborador com a condição "inclui o utilizador atual", cada utilizador da aplicação só vê as entradas que lhe estão atribuídas na tabela.

![Coluna do colaborador na aplicação](images/Mitarbeiter-Spalte-in-der-Universellen-App.gif)
